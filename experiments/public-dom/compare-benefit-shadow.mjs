// P2 shadow comparator: reads an anonymous public page, never mounts/replaces its DOM.
import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { createRegistry, compilePage, renderCompiled } from '../declarative-ui/registry.mjs';
import { manifest, sources, benefitStrip } from '../declarative-ui/landing-benefits.mjs';

const base = new URL(process.env.M2D_AUDIT_BASE_URL || 'https://casaemmodulos.casa/');
if (base.protocol !== 'https:' && !(base.protocol==='http:' && ['localhost','127.0.0.1'].includes(base.hostname))) {
  throw new Error('Only HTTPS or local origin allowed');
}
if (base.username || base.password || base.search || base.hash) throw new Error('Origin must be clean');
const expected = renderCompiled(compilePage(manifest,sources,createRegistry([benefitStrip])))[0].result;
const browser = await chromium.launch({headless:true});
try {
  const page = await browser.newPage({viewport:{width:1366,height:900},reducedMotion:'reduce',locale:'pt-BR'});
  const response = await page.goto(new URL('/',base).href,{waitUntil:'domcontentloaded',timeout:30000});
  assert.equal(response?.status(),200,'Landing GET must succeed');
  await page.waitForSelector('#benefits > .benefit-item',{timeout:10000});
  const actual=await page.locator('#benefits > .benefit-item').evaluateAll(elements=>elements.map(el=>({
    tag:el.tagName.toLowerCase(),className:el.className,
    children:[...el.children].map(child=>child.tagName.toLowerCase()==='img'
      ? {tag:'img',attributes:{src:child.getAttribute('src'),alt:child.getAttribute('alt')}}
      : {tag:child.tagName.toLowerCase(),text:child.textContent})
  })));
  try {
    assert.deepEqual(actual,expected);
    console.log('P2_SHADOW_EQUALITY '+JSON.stringify({
      route:'/',component:'landing/benefit-strip@1',rows:actual.length,
      domEquivalent:true,fields:'tag,className,child order,img src/alt,span text',
      liveDOMChanges:0
    }));
  } catch(error) {
    // Never print public content in CI, only a structural mismatch count.
    console.log('P2_SHADOW_EQUALITY '+JSON.stringify({
      route:'/',component:'landing/benefit-strip@1',rowsActual:actual.length,
      rowsExpected:expected.length,domEquivalent:false,
      firstMismatchedIndex:actual.findIndex((row,i)=>JSON.stringify(row)!==JSON.stringify(expected[i])),
      liveDOMChanges:0
    }));
    throw new Error('P2 DOM shadow equivalence failed');
  }
} finally { await browser.close(); }
