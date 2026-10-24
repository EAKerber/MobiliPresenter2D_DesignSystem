// Validates the scoped VIS-002C long-copy v0.3 candidate and its generated artifacts.
import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {readFile} from "node:fs/promises";

const read=path=>readFile(new URL("../"+path,import.meta.url),"utf8");
const blob=text=>createHash("sha1").update("blob "+Buffer.byteLength(text,"utf8")+"\0").update(text,"utf8").digest("hex");
const luminance=hex=>{
  const rgb=hex.slice(1).match(/.{2}/g).map(x=>parseInt(x,16)/255);
  const f=x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4;
  return .2126*f(rgb[0])+.7152*f(rgb[1])+.0722*f(rgb[2]);
};
const contrast=(a,b)=>{
  const x=luminance(a),y=luminance(b);
  return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);
};
const decisionsText=await read("decisions.json");
const mapping=JSON.parse(await read("docs/VIS002C_CONTEXTUAL_MAPPING_V0_3_0.json"));
const manifest=JSON.parse(await read("dist/vis002c-long-copy-light-v0.3.0.manifest.json"));
const css=await read("dist/vis002c-long-copy-light-v0.3.0.css");
const oldMap=JSON.parse(await read("docs/VIS002C_CONTEXTUAL_MAPPING_V0_2_0.json"));

assert.equal(blob(decisionsText),"63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa","Canonical decision source changed");
const decisions=JSON.parse(decisionsText);
const vis=decisions.decisions.find(x=>x.id==="VIS-002");
assert.equal(vis.approvedPalette.colors.textPrimary.light.toUpperCase(),"#292723");
assert.equal(mapping.status,"scoped-candidate-user-authorized-2026-10-24; canonical-decision-file-unchanged");
assert.equal(mapping.sourceDecisionGitBlob,"63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa");
assert.equal(mapping.roleRef,"VIS-002.approvedPalette.colors.textPrimary.light");
assert.equal(mapping.value.toUpperCase(),"#292723");
assert.equal(mapping.contexts.length,7);
assert.equal(mapping.constraints.globalUsage,false);
assert.equal(mapping.constraints.darkThemeMustStayUnchanged,true);
assert.equal(mapping.constraints.onlyMeasuredContexts,true);
assert.deepEqual(mapping.preservedMapping.contexts,oldMap.contexts.slice(0,3).map(({route,selector})=>({route,selector})));
assert.equal(mapping.preservedMapping.value,"#705C4B");
assert.equal(oldMap.version,"0.2.0");

const expected=[
  {route:"/",selector:".story-section > p:not(.eyebrow)",background:"#E8E3DC"},
  {route:"/",selector:".feature-copy > p:not(.eyebrow):not(.feature-availability)",background:"#F0EDE8"},
  {route:"/about/",selector:".about-closing > p:not(.eyebrow):not(.about-closing__signature)",background:"#F0EDE8"},
  {route:"/about/",selector:".about-scale__stat > span",background:"#F0EDE8"},
  {route:"/how-it-works/",selector:".finish-copy > p:not(.eyebrow):not(.finish-signature)",background:"#F0EDE8"},
  {route:"/how-it-works/",selector:".commercial-clarity > p:not(.eyebrow)",background:"#F0EDE8"},
  {route:"/how-it-works/",selector:".launch-card .launch-copy > p",background:"#F0EDE8"}
];
assert.deepEqual(mapping.contexts.map(({route,selector,background})=>({route,selector,background})),expected);
for(const c of mapping.contexts)assert.ok(contrast("#292723",c.background)>=4.5,"Contrast below threshold: "+c.selector);
assert.equal(manifest.version,"0.3.0");
assert.equal(manifest.status,"SCOPED_CANDIDATE_USER_AUTHORIZED");
assert.equal(manifest.token,"--ds-vis002c-long-copy-light");
assert.equal(manifest.value,"#292723");
assert.equal(manifest.roleRef,mapping.roleRef);
assert.equal(manifest.constraints.allowsGlobalUsage,false);
assert.equal(manifest.constraints.changesCanonicalDecision,false);
assert.equal(manifest.constraints.changesExistingV0_2Contexts,false);
assert.equal(manifest.contexts.length,7);
assert.deepEqual(manifest.contexts.map(({route,selector,background})=>({route,selector,background})),expected);

const selectors=expected.map(c=>'html[data-theme="light"] '+c.selector);
const expectedCss=[
  "/* GENERATED CANDIDATE — VIS-002C measured long-copy contexts only.",
  " * Mapping: docs/VIS002C_CONTEXTUAL_MAPPING_V0_3_0.json",
  " * Decision source blob: 63b60f8d87327c6fd1e80c8cdf4ff832c4089bfa",
  " * Does not change v0.2, global roles, text color declarations, or dark theme.",
  " */",
  selectors.join(",\n")+" {",
  "  --ds-vis002c-long-copy-light: #292723;",
  "}",
  ""
].join("\n");
assert.equal(css,expectedCss,"Generated CSS differs from the exact scoped projection");
assert.doesNotMatch(css,/\bcolor\s*:/i,"Artifact may not set text color directly");
assert.doesNotMatch(css,/:root\s*\{/,"Global token scope is not authorized");

console.log(`VIS002C_LONG_COPY_V03_PASS contexts=${mapping.contexts.length} dark=unchanged global=false`);
