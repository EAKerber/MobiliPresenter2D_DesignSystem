import test from 'node:test';
import assert from 'node:assert/strict';
import { createRegistry, compilePage, renderCompiled, CompositionError } from './registry.mjs';
import { manifest, sources, benefitStrip } from './landing-benefits.mjs';
const registry = () => createRegistry([benefitStrip]);
function changed(patch) { return { ...manifest, sections:[{...manifest.sections[0],...patch}] }; }
function failure(input, data, code) { assert.throws(() => compilePage(input,data,registry()),e => e instanceof CompositionError && e.code===code); }
test('valid fixture produces four benefit rows in source order', () => {
  const nodes=renderCompiled(compilePage(manifest,sources,registry()))[0].result;
  assert.equal(nodes.length,4);
  assert.equal(nodes[0].className,'benefit-item');
  assert.equal(nodes[0].children[0].attributes.alt,'');
  assert.equal(nodes[0].children[1].text,sources.landing.benefits[0].label);
});
test('unknown type is not rendered',()=>failure(changed({type:'editorial/missing@1'}),sources,'unknown-component'));
test('unknown variant is forbidden',()=>failure(changed({variant:'large'}),sources,'unsupported-variant'));
test('duplicate id is forbidden',()=>failure({...manifest,sections:[manifest.sections[0],manifest.sections[0]]},sources,'duplicate-id'));
test('missing source never invents defaults',()=>failure(changed({dataRef:'landing.missing'}),sources,'missing-reference'));
test('unsafe ref is forbidden',()=>failure(changed({dataRef:'landing.constructor'}),sources,'invalid-reference'));
test('style injection is not a manifest field',()=>failure({...manifest,sections:[{...manifest.sections[0],style:'color:red'}]},sources,'unsupported-field'));
test('external icon URL fails data validation',()=>failure(manifest,{landing:{benefits:[{label:'X',icon:'https://example.com/x.svg'}]}},'invalid-data'));
test('later error prevents ALL render calls',()=>{
  let called=0;
  const special={...benefitStrip,render(){called++;return [];}};
  const mixed={...manifest,sections:[manifest.sections[0],{...manifest.sections[0],id:'other',dataRef:'landing.absent'}]};
  assert.throws(()=>compilePage(mixed,sources,createRegistry([special])));
  assert.equal(called,0);
});
test('component registrations must be unique',()=>assert.throws(()=>createRegistry([benefitStrip,benefitStrip]),/duplicate component type/));
