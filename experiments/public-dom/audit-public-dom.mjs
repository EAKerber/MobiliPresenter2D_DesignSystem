// Public DOM/computed-style audit. Read-only. Runs outside product, no credentials.
import { mkdir, writeFile } from 'node:fs/promises';
import { dirname } from 'node:path';

const base = new URL(process.env.M2D_AUDIT_BASE_URL || 'https://casaemmodulos.casa/');
if (base.protocol !== 'https:' && !(base.protocol === 'http:' && ['127.0.0.1','localhost'].includes(base.hostname))) {
  throw new Error('Audit origin must be HTTPS or a local development server');
}
if (base.username || base.password || base.search || base.hash) throw new Error('Origin must not include credentials/query/fragment');
const widths = (process.env.M2D_AUDIT_WIDTHS || '390,1366').split(',').map(Number);
if (!widths.length || widths.length>6 || widths.some(w=>!Number.isInteger(w)||w<300||w>2560)) throw new Error('Invalid viewport widths');
const themes = (process.env.M2D_AUDIT_THEMES || 'light,dark').split(',');
if (themes.some(t=>!['light','dark'].includes(t))) throw new Error('Theme must be light or dark');
const routes = ['/', '/about/', '/how-it-works/', '/viewer/'];
const probes = {
  '/': ['.site-header','.brand','.hero','.benefit-item','.environment','.environment-feature','.ui-theme-toggle','.site-footer'],
  '/about/': ['.site-header','.about-hero','.about-chapter','.eyebrow','.ui-theme-toggle','.site-footer'],
  '/how-it-works/': ['.site-header','.how-hero','.foundation-item','.eyebrow','.ui-theme-toggle','.site-footer'],
  '/viewer/': ['.viewer-header','.viewer-heading','.viewer-block','.scene-stage','.scene-hotspot','.technical-view','.detail-panel','.ui-theme-toggle']
};
const report = {
  schemaVersion: 'M2DPublicDOMAudit 0.1',
  checkedAt: new Date().toISOString(),
  source: base.origin,
  scope: 'Anonymous public GET page loads. No auth, no admin, no clicks, no posts, no assertions of visual approval.',
  runner: { runtime: process.version, widths, themes, routes },
  observations: []
};
const { chromium } = await import('playwright');
const browser = await chromium.launch({headless:true});
try {
  for (const route of routes) for (const width of widths) for (const theme of themes) {
    const context = await browser.newContext({
      viewport:{width,height:900},colorScheme:theme,reducedMotion:'reduce',
      locale:'pt-BR',serviceWorkers:'block',
      // Deliberately no storageState, cookies, HTTP auth or admin credentials.
    });
    await context.addInitScript(({key,mode})=>{
      try { localStorage.setItem(key,mode); } catch {}
    }, {key:'casa-ui-theme-mode-v1',mode:theme});
    const page = await context.newPage();
    const item={route,width,theme,ok:false,httpStatus:null,loaded:false,note:null,failures:[],errors:[],snapshot:null};
    page.on('pageerror',e=>{if(item.errors.length<8)item.errors.push(String(e.message).slice(0,280))});
    page.on('response',response=>{
      if (item.failures.length>=15) return;
      const url=new URL(response.url());
      if (url.origin===base.origin && response.status()>=400) {
        // Never persist query strings or HTTP response bodies.
        item.failures.push({path:url.pathname,status:response.status()});
      }
    });
    try {
      const url=new URL(route,base);
      const resp=await page.goto(url.href,{waitUntil:'domcontentloaded',timeout:30000});
      item.httpStatus=resp?.status()??null;
      if(route==='/viewer/') {
        try {
          await page.waitForFunction(()=>{
            const root=document.querySelector('#viewerLayout');
            return root && (root.querySelector('.viewer-block')||root.querySelector('.viewer-public-error'));
          },null,{timeout:15000});
        } catch { item.note='Viewer never resolved to a block or a public error in 15s'; }
      } else if (route==='/') {
        try{await page.waitForSelector('#benefits .benefit-item',{timeout:7000})}
        catch{item.note='Landing benefits not mounted in 7s'}
      }
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
      item.snapshot=await page.evaluate(({selectors})=>{
        const keys=['display','position','color','backgroundColor','fontFamily','fontSize','fontWeight','lineHeight','borderRadius','borderColor','boxShadow','opacity','transform','outlineColor','outlineWidth'];
        const root=document.documentElement;
        const bySelector=Object.fromEntries(selectors.map(sel=>{
          const els=[...document.querySelectorAll(sel)];
          return [sel,{count:els.length,examples:els.slice(0,2).map(el=>{
            const style=getComputedStyle(el), rect=el.getBoundingClientRect(), props={};
            for (const key of keys) props[key]=style[key]??'';
            return {
              tag:el.tagName.toLowerCase(),classes:[...el.classList],id:el.id||null,
              aria:{label:el.getAttribute('aria-label'),expanded:el.getAttribute('aria-expanded'),pressed:el.getAttribute('aria-pressed'),current:el.getAttribute('aria-current')},
              hidden:el.hidden,
              rect:{x:Math.round(rect.x),y:Math.round(rect.y),w:Math.round(rect.width),h:Math.round(rect.height)},
              computed:props
            };
          })}];
        }));
        const classCounts={};
        for(const el of document.querySelectorAll('[class]'))for(const name of el.classList){classCounts[name]=(classCounts[name]||0)+1}
        const viewport={width:innerWidth,height:innerHeight,dpr:devicePixelRatio,scrollWidth:document.documentElement.scrollWidth};
        return {
          title:document.title,viewport,themeMode:root.getAttribute('data-theme-mode'),
          themeResolved:root.getAttribute('data-theme'),
          styleSheets:[...document.styleSheets].map(s=>{try{return s.href?new URL(s.href).pathname:'inline'}catch{return 'unknown'}}),
          elementCount:document.querySelectorAll('*').length,
          classCounts,
          dynamicRegions:{
            viewerLayout:document.querySelectorAll('#viewerLayout *').length,
            landingEnvironments:document.querySelectorAll('#environmentTrack *').length,
            landingBenefits:document.querySelectorAll('#benefits *').length,
            menu:document.querySelectorAll('[data-private-menu] *').length
          },
          selectors:bySelector,
          // No innerText, input values, cookies, storage content, request bodies or auth payload.
        };
      },{selectors:probes[route]});
      item.loaded=true;
      item.ok=item.httpStatus>=200&&item.httpStatus<400 && (route!=='/viewer/' || item.snapshot.selectors['.viewer-block']?.count>0);
    } catch(e) { item.note=String(e.message||e).slice(0,400); }
    report.observations.push(item);
    console.log(JSON.stringify({route,width,theme,ok:item.ok,httpStatus:item.httpStatus,elementCount:item.snapshot?.elementCount,failedResponses:item.failures.length,note:item.note}));
    await context.close();
  }
} finally { await browser.close(); }
const output=process.env.M2D_AUDIT_OUTPUT||'artifacts/public-dom-audit.json';
await mkdir(dirname(output),{recursive:true});
await writeFile(output,JSON.stringify(report,null,2)+'\n','utf8');
console.log('PUBLIC_DOM_AUDIT_OUTPUT '+output+' total='+report.observations.length+' ok='+report.observations.filter(x=>x.ok).length);
// Fail on navigation failures; a report artifact remains available for diagnosis.
if(report.observations.some(x=>!x.ok))process.exitCode=1;
