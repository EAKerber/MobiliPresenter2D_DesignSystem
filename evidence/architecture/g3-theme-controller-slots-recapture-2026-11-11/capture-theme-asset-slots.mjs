import fs from "node:fs/promises";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("../MobiliPresenter2D-vis002c-tools/node_modules/playwright");
const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "..", "MobiliPresenter2D-g2-repro-exact-221b54b-20261112");
const appRoot = path.join(repo, "app");
const output = path.join(here, "result-v2.json");
const edge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const host = "http://g3-main.local";
const widths = [390, 1366];
const routes = ["/", "/how-it-works/", "/about/", "/viewer/", "/config/", "/admin.html", "/access/manage.html"];

const mime = {
  ".html": "text/html; charset=utf-8", ".js": "application/javascript; charset=utf-8",
  ".mjs": "application/javascript; charset=utf-8", ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8", ".png": "image/png", ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg", ".webp": "image/webp", ".svg": "image/svg+xml", ".ico": "image/x-icon"
};

async function main() {
  const browser = await chromium.launch({ headless: true, executablePath: edge });
  const rows = [];
  try {
    for (const routePath of routes) {
      for (const width of widths) {
        for (const theme of ["light", "dark"]) {
          const context = await browser.newContext({
            viewport: { width, height: 900 }, deviceScaleFactor: 1,
            colorScheme: theme, locale: "pt-BR", timezoneId: "America/Sao_Paulo"
          });
          await context.addInitScript(mode => localStorage.setItem("casa-ui-theme-mode-v1", mode), theme);
          const page = await context.newPage();
          const pageErrors = [], consoleErrors = [], httpErrors = [];
          page.on("pageerror", error => pageErrors.push(String(error)));
          page.on("console", message => { if (message.type() === "error") consoleErrors.push(message.text()); });
          page.on("response", response => { if (response.status() >= 400) httpErrors.push({status:response.status(),url:response.url()}); });
          await page.route(`${host}/**`, async route => {
            const request=route.request(), url=new URL(request.url());
            if (request.method()==="POST" && url.pathname==="/api/access/session")
              return route.fulfill({status:200,contentType:"application/json; charset=utf-8",body:JSON.stringify({authenticated:false})});
            if (url.pathname.startsWith("/api/")) return route.fulfill({status:404,body:""});
            let relative;
            try { relative=decodeURIComponent(url.pathname); } catch { return route.fulfill({status:400,body:"bad path"}); }
            if (relative.includes("\0") || relative.includes("..")) return route.fulfill({status:403,body:"forbidden"});
            if (relative.endsWith("/")) relative += "index.html";
            const file=path.resolve(appRoot,`.${relative}`);
            if(!file.startsWith(`${appRoot}${path.sep}`)) return route.fulfill({status:403,body:"forbidden"});
            try { return route.fulfill({status:200,contentType:mime[path.extname(file)]||"application/octet-stream",body:await fs.readFile(file)}); }
            catch { return route.fulfill({status:404,contentType:"text/plain; charset=utf-8",body:"not found"}); }
          });
          await page.goto(`${host}${routePath}`,{waitUntil:"domcontentloaded"});
          await page.locator("[data-ui-theme-toggle]").waitFor({state:"attached",timeout:12000});
          await page.waitForFunction(() => document.documentElement.dataset.theme && document.querySelector("img[data-brand-variant]"),null,{timeout:12000});
          const initial=await page.evaluate(()=>{
            const button=document.querySelector("[data-ui-theme-toggle]");
            const rect=e=>{const r=e.getBoundingClientRect();return {x:+r.x.toFixed(1),y:+r.y.toFixed(1),width:+r.width.toFixed(1),height:+r.height.toFixed(1)}};
            const pathOf=e=>{const parts=[];for(let n=e;n&&n.nodeType===1&&parts.length<6;n=n.parentElement){let x=n.tagName.toLowerCase();if(n.id)x+="#"+n.id;else if(typeof n.className==="string"&&n.className.trim())x+="."+n.className.trim().split(/\s+/).slice(0,2).join(".");parts.unshift(x)}return parts.join(" > ")};
            const brands=[...document.querySelectorAll("img[data-brand-variant]")].map(image=>{
              const style=getComputedStyle(image),theme=document.documentElement.dataset.theme,expected=image.getAttribute("data-src-"+theme);
              return {src:image.getAttribute("src"),currentSrc:image.currentSrc,expectedSrc:expected,sourceMatchesTheme:image.getAttribute("src")===expected,complete:image.complete,naturalWidth:image.naturalWidth,parent:pathOf(image.parentElement),rect:rect(image),display:style.display,visibility:style.visibility,objectFit:style.objectFit};
            });
            const logo=document.querySelector(".site-header img[data-brand-variant], .viewer-header img[data-brand-variant], [data-private-header] img[data-brand-variant]")||document.querySelector("img[data-brand-variant]");
            const bs=getComputedStyle(button),ls=getComputedStyle(logo);
            const theme=document.documentElement.dataset.theme;
            const expected=logo.getAttribute("data-src-"+theme);
            return {
              route:location.pathname,viewport:{width:innerWidth,height:innerHeight},
              requestedTheme:localStorage.getItem("casa-ui-theme-mode-v1"),
              rootTheme:theme,rootThemeMode:document.documentElement.dataset.themeMode||null,
              themeApiMode:window.CASA_UI_THEME?.getMode?.()||null,themeApiResolved:window.CASA_UI_THEME?.getResolved?.()||null,
              stylesheets:[...document.styleSheets].map(x=>x.href||"inline"),
              themeButton:{exists:Boolean(button),ariaLabel:button.getAttribute("aria-label"),title:button.title,mode:button.dataset.mode,parent:pathOf(button.parentElement),parentClass:typeof button.parentElement.className==="string"?button.parentElement.className:null,rect:rect(button),display:bs.display,visibility:bs.visibility,color:bs.color,background:bs.backgroundColor,border:bs.borderColor,minWidth:bs.minWidth,minHeight:bs.minHeight},
              brandImages:brands,headerBrand:{src:logo.getAttribute("src"),currentSrc:logo.currentSrc,expectedSrc:logo.getAttribute("data-src-"+theme),sourceMatchesTheme:logo.getAttribute("src")===logo.getAttribute("data-src-"+theme),complete:logo.complete,naturalWidth:logo.naturalWidth,rect:rect(logo),display:ls.display,visibility:ls.visibility,objectFit:ls.objectFit},
              privateHeader:Boolean(document.querySelector("[data-private-header]")),publicHeader:Boolean(document.querySelector(".site-header")),viewerHeader:Boolean(document.querySelector(".viewer-header"))
            };
          });
          const transition=[];
          for(let i=0;i<2;i++){
            await page.locator("[data-ui-theme-toggle]").click();
            await page.waitForTimeout(40);
            transition.push(await page.evaluate(()=>({mode:window.CASA_UI_THEME?.getMode?.()||null,resolved:window.CASA_UI_THEME?.getResolved?.()||null,rootTheme:document.documentElement.dataset.theme||null,brandSrcs:[...document.querySelectorAll("img[data-brand-variant]")].map(x=>x.getAttribute("src")),stored:localStorage.getItem("casa-ui-theme-mode-v1")})));
          }
          rows.push({id:`${routePath.replace(/[^a-z0-9]+/gi,"-")}-${width}-${theme}`,route:routePath,width,theme,browserVersion:browser.version(),initial,transition,pageErrors,consoleErrors,httpErrors});
          await context.close();
        }
      }
    }
  } finally { await browser.close(); }
  const report={
    generatedAt:new Date().toISOString(),
    productCommit:"221b54b2a41ecc8c338d1bf2cf67280cf165ce95",
    method:"Clean detached source checkout; local files routed through Playwright; theme mode set before navigation; CSSOM/DOM slot, visible brand asset and two real button transitions recorded; no remote services.",
    browser:"Microsoft Edge 157.0.4341.46",dpr:1,widths,routes,rows
  };
  await fs.writeFile(output,`${JSON.stringify(report,null,2)}\n`,"utf8");
  console.log(JSON.stringify({output,rows:rows.length,summary:rows.map(r=>({route:r.route,width:r.width,theme:r.theme,root:r.initial.rootTheme,api:r.initial.themeApiResolved,headerLogo:r.initial.headerBrand.src,brandCount:r.initial.brandImages.length,allAssetsMatch:r.initial.brandImages.every(x=>x.sourceMatchesTheme),slot:r.initial.themeButton.parent,button:r.initial.themeButton.rect,transitions:r.transition.map(x=>`${x.mode}/${x.resolved}`),pageErrors:r.pageErrors.length,httpErrors:r.httpErrors.length}))},null,2));
}

main().catch(error=>{console.error(error);process.exitCode=1;});
