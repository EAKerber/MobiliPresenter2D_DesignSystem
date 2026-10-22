import test from "node:test";
import assert from "node:assert/strict";
import { readFile, mkdtemp, rm } from "node:fs/promises";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { buildArtifacts, derive, exportPalette, gitBlobSha, SOURCE_GIT_BLOB } from "../scripts/export-approved-palette.mjs";

const input = await readFile(resolve("decisions.json"), "utf8");

test("VIS-002 source provenance is pinned to exact Git blob bytes", () => {
  assert.equal(gitBlobSha(input), SOURCE_GIT_BLOB);
});

test("palette export uses only approved reference pairs and focus treatment", () => {
  const {entries,authority}=derive(input);
  assert.equal(entries.length,16);
  assert.equal(authority.decisionId,"VIS-002");
  assert.equal(authority.implementationAuthorized,false);
  const byName=Object.fromEntries(entries.map(x=>[x.cssName,x.value]));
  assert.equal(byName["--ds-reference-canvas-light"],"#E8E3DC");
  assert.equal(byName["--ds-reference-surface-dark"],"#211F1C");
  assert.equal(byName["--ds-reference-text-secondary-light"],"#705C4B");
  assert.equal(byName["--ds-reference-focus-outline-dark"],"#D8BC7C");
  assert.equal(byName["--ds-reference-focus-outline-width"],"4px");
  assert.equal(byName["--ds-reference-focus-outline-offset"],"3px");
  assert.equal(Object.keys(byName).length,entries.length);
});

test("generated CSS cannot accidentally redefine current product roles", () => {
  const {css,manifest}=buildArtifacts(input);
  const model=JSON.parse(manifest);
  assert.equal(model.policy.generatedCssMayBeLinkedAtRuntime,false);
  assert.equal(model.policy.noSemanticAliasesForComponents,true);
  assert.match(css,/DO NOT LINK into app pages/);
  assert.doesNotMatch(css,/--(?:public|ui-theme|bg|accent|border|surface|text):/);
  assert.equal((css.match(/--ds-reference-/g)||[]).length,16);
  assert.equal(model.entries.length,16);
  assert.equal(model.source.gitBlobSha,SOURCE_GIT_BLOB);
});

test("generator is deterministic, checked outputs are byte-for-byte identical", async () => {
  assert.deepEqual(buildArtifacts(input),buildArtifacts(input));
  const dir=await mkdtemp(join(tmpdir(),"m2d-p-token-01-"));
  try {
    await exportPalette({outDir:dir});
    await exportPalette({outDir:dir,check:true});
    const css=await readFile(join(dir,"approved-palette-reference.css"),"utf8");
    assert.equal(css,buildArtifacts(input).css);
  } finally { await rm(dir,{recursive:true,force:true}); }
});

test("export fails closed on unapproved source changes", () => {
  const altered=input.replace("#E8E3DC","#E8E3DD");
  assert.notEqual(altered,input);
  assert.throws(()=>derive(altered),/source changed/);
});

test("tracked dist/ exports are in sync with source", async () => {
  await exportPalette({check:true});
});
