import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { deriveContextualCSS,exportContext,TOKEN } from "../scripts/export-approved-contextual-text.mjs";
const decisions=await readFile("decisions.json","utf8");

test("only the three explicitly approved routes are emitted",()=>{
  const {css,manifest}=deriveContextualCSS(decisions),m=JSON.parse(manifest);
  assert.equal(m.value,"#705C4B"); assert.equal(m.theme,"light");
  assert.equal(m.contexts.length,3);assert.equal(m.constraints.allowsGlobalUsage,false);
  assert.deepEqual(m.contexts.map(c=>c.route),["/","/how-it-works/","/about/"]);
  assert.equal((css.match(/html\[data-theme="light"\]/g)||[]).length,3);
  assert.equal((css.match(new RegExp(TOKEN,"g"))||[]).length,1);
  assert.doesNotMatch(css,/\bcolor\s*:/i,"Generated file may only assign scoped custom property");
  assert.doesNotMatch(css,/:root\s*\{/,"Global token mapping is not approved");
});
test("CSS and manifest byte-for-byte match canonical source",async()=>{
  const expected=deriveContextualCSS(decisions);
  assert.equal(await readFile("dist/approved-contextual-support-text.css","utf8"),expected.css);
  assert.equal(await readFile("dist/approved-contextual-support-text.manifest.json","utf8"),expected.manifest);
  await exportContext({check:true});
});
test("changing source without new approval fails closed",()=>{
  assert.throws(()=>deriveContextualCSS(decisions.replace("#705C4B","#705C4C")),/Decision source changed/);
});
