import { SCHEMA } from './registry.mjs';
// Fixture values copied from product's current public Landing benefits; no API/admin schema changes.
export const manifest = {
  schemaVersion: SCHEMA, route: '/',
  sections: [{ id:'benefits', type:'landing/benefit-strip@1', variant:'standard', dataRef:'landing.benefits' }]
};
export const sources = { landing:{ benefits:[
  { label:'Qualidade de móvel planejado', icon:'/landing/assets/icons/ui/white/qualidade.svg' },
  { label:'Praticidade de um sistema modular', icon:'/landing/assets/icons/ui/white/modularidade.svg' },
  { label:'Preço pensado para o seu projeto', icon:'/landing/assets/icons/ui/white/preco.svg' },
  { label:'Entrega e instalação especializada', icon:'/landing/assets/icons/ui/white/entrega.svg' }
]}};
export const benefitStrip = {
  type:'landing/benefit-strip@1', variants:['standard'],
  validate(items) {
    return Array.isArray(items) && items.length>0 && items.length<=12 && items.every(x =>
      x && Object.getPrototypeOf(x)===Object.prototype && Object.keys(x).length===2 &&
      typeof x.label==='string' && x.label.trim().length>0 && x.label.length<=160 &&
      typeof x.icon==='string' && /^\/landing\/assets\/icons\/ui\/white\/[a-z0-9-]+\.svg$/.test(x.icon));
  },
  render(items) {
    // Mirrors the existing .benefit-item child structure, without touching browser DOM.
    return items.map(x => ({ tag:'div', className:'benefit-item', children:[
      { tag:'img', attributes:{src:x.icon,alt:''} }, { tag:'span',text:x.label }
    ]}));
  }
};
