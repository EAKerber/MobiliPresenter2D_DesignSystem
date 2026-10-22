// P-TOKEN-02B: scope-limited, already-published VIS-002 contextual text pair.
// Generates only custom-property declarations on explicitly approved selectors.
// Does NOT authorize palette aliases on other components/contexts.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export const DECISION_BLOB = "63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa";
export const VERSION = "0.1.0";
export const TOKEN = "--ds-vis002-approved-support-text-light";
const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const EXPECTED_CONTEXTS = [
  { route: "/", selector: ".hero-description" },
  { route: "/how-it-works/", selector: ".how-hero-note" },
  { route: "/about/", selector: ".about-scale p:not(.eyebrow)" }
];
const shaBlob = text => createHash("sha1").update("blob "+Buffer.byteLength(text,"utf8")+"\0").update(text,"utf8").digest("hex");

export function deriveContextualCSS(content) {
  assert.equal(shaBlob(content),DECISION_BLOB,"Decision source changed; review authoritative VIS-002 approval first");
  const doc=JSON.parse(content);
  const decision=doc.decisions?.find(x=>x.id==="VIS-002");
  assert.ok(decision,"VIS-002 decision missing");
  assert.equal(decision.implementationAuthorized,false,"Decision status changed; review scope before export");
  const entry=decision.approvedRuntimePairs?.find(x=>x.candidateReplacement?.status?.includes("approved-palette-pair"));
  assert.ok(entry,"Approved pre-existing contextual text pair not found");
  const scoped=entry.routeSelectors || [];
  assert.deepEqual(scoped,EXPECTED_CONTEXTS,"Scope changed: do not export selectors without independent approval");
  const color=entry.candidateReplacement.foreground;
  assert.match(color,/^#[0-9a-fA-F]{6}$/);
  assert.equal(color.toUpperCase(),decision.approvedPalette.colors.textSecondary.light.toUpperCase(),
    "Context value and palette reference no longer coincide");
  assert.equal(entry.candidateReplacement.background,"#F0EDE8");
  const selectors=scoped.map(x=>'html[data-theme="light"] '+x.selector);
  const css=[
    "/* GENERATED — VIS-002.approvedRuntimePairs, exact contextual selectors only.",
    " * Decision Git blob: "+DECISION_BLOB,
    " * No global role assignment; no CSS color declaration; product owns use.",
    " * Do not broaden selector reach without new evidence and approval.",
    " */",
    selectors.join(",\n")+" {",
    "  "+TOKEN+": "+color.toUpperCase()+";",
    "}",""
  ].join("\n");
  const manifest={
    schema:"M2DApprovedContextualTextToken/0.1",version:VERSION,
    source:{repository:"EAKerber/MobiliPresenter2D_DesignSystem",decision:"VIS-002",
      gitBlobSha:DECISION_BLOB,decisionPath:"approvedRuntimePairs[0].candidateReplacement"},
    status:"EXACT_EXISTING_CONTEXT_ONLY",token:TOKEN,value:color.toUpperCase(),
    theme:"light",approvedBackground:entry.candidateReplacement.background,
    contexts:scoped,
    constraints:{allowsGlobalUsage:false,allowsDifferentColor:false,
      productUseRequiresExactSelectors:true,visualChangeAuthorized:false}
  };
  return {css,manifest:JSON.stringify(manifest,null,2)+"\n"};
}

export async function exportContext({check=false,outDir=join(ROOT,"dist")}={}) {
  const content=await readFile(join(ROOT,"decisions.json"),"utf8");
  const artifacts=deriveContextualCSS(content);
  for(const [name,data] of [["approved-contextual-support-text.css",artifacts.css],
    ["approved-contextual-support-text.manifest.json",artifacts.manifest]]){
    const target=join(outDir,name);
    if(check)assert.equal(await readFile(target,"utf8"),data,"Stale generated distribution "+name);
    else{await mkdir(dirname(target),{recursive:true});await writeFile(target,data,"utf8");}
  }
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  exportContext({check:process.argv.includes("--check")}).then(()=>
    console.log("P_TOKEN_02B_CONTEXT_"+(process.argv.includes("--check")?"CHECK":"EXPORT")+"_PASS"))
    .catch(e=>{console.error(e);process.exitCode=1;});
}
