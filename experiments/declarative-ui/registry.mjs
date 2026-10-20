// Isolated P1 proof. Does not modify or import the product runtime.
export const SCHEMA = 'PageCompositionExperimental 0.1';
const KEY = /^[a-z][a-z0-9-]*$/;
const TYPE = /^[a-z][a-z0-9-]*\/[a-z][a-z0-9-]*@[1-9][0-9]*$/;
const FORBIDDEN = new Set(['__proto__','constructor','prototype']);
export class CompositionError extends Error {
  constructor(code, path) { super(code + ': ' + path); this.name = 'CompositionError'; this.code = code; this.path = path; }
}
function record(v) { return v !== null && typeof v === 'object' && !Array.isArray(v) && (Object.getPrototypeOf(v) === Object.prototype || Object.getPrototypeOf(v) === null); }
function fields(v, allowed, path) {
  if (!record(v)) throw new CompositionError('invalid-record', path);
  for (const key of Object.keys(v)) if (!allowed.includes(key)) throw new CompositionError('unsupported-field', path + '.' + key);
}
function resolve(source, path) {
  if (typeof path !== 'string') throw new CompositionError('invalid-reference', 'dataRef');
  const keys = path.split('.');
  if (!keys.length || keys.some(k => !KEY.test(k) || FORBIDDEN.has(k))) throw new CompositionError('invalid-reference', path);
  let current = source;
  for (const key of keys) {
    if (!record(current) || !Object.hasOwn(current,key)) throw new CompositionError('missing-reference', path);
    const own = Object.getOwnPropertyDescriptor(current,key);
    if (!own || !Object.hasOwn(own,'value')) throw new CompositionError('invalid-reference',path);
    current = own.value;
  }
  return current;
}
// Copy validated-input candidates as inert JSON values; no dependency on structuredClone.
function copyJson(v, seen = new Set(), depth = 0) {
  if (depth > 16) throw new TypeError('JSON nesting too deep');
  if (v === null || typeof v === 'string' || typeof v === 'boolean') return v;
  if (typeof v === 'number' && Number.isFinite(v)) return v;
  if (!record(v) && !Array.isArray(v)) throw new TypeError('not a JSON value');
  if (seen.has(v)) throw new TypeError('cyclic JSON value');
  seen.add(v);
  let copy;
  if (Array.isArray(v)) {
    if (v.length > 1000) throw new TypeError('JSON array too large');
    copy = v.map(item => copyJson(item, seen, depth + 1));
  } else {
    copy = {};
    for (const key of Object.keys(v)) {
      if (FORBIDDEN.has(key)) throw new TypeError('unsafe JSON key');
      const descriptor = Object.getOwnPropertyDescriptor(v, key);
      if (!descriptor || !Object.hasOwn(descriptor,'value')) throw new TypeError('JSON accessors disallowed');
      copy[key] = copyJson(descriptor.value, seen, depth + 1);
    }
  }
  seen.delete(v);
  return copy;
}
function freezeJson(value) {
  if (value && typeof value==='object') {
    for (const child of Object.values(value)) freezeJson(child);
    Object.freeze(value);
  }
  return value;
}
export function createRegistry(definitions) {
  if (!Array.isArray(definitions)) throw new TypeError('definitions must be array');
  const components = new Map();
  for (const def of definitions) {
    if (!record(def) || typeof def.type !== 'string' || !TYPE.test(def.type)
      || !Array.isArray(def.variants) || def.variants.length === 0
      || def.variants.some(v => typeof v !== 'string' || !KEY.test(v))
      || typeof def.validate !== 'function' || typeof def.render !== 'function') throw new TypeError('invalid definition');
    if (components.has(def.type)) throw new TypeError('duplicate component type');
    components.set(def.type, Object.freeze({ ...def, variants:Object.freeze([...def.variants]) }));
  }
  return Object.freeze({ get(type) { return components.get(type); }, types() { return [...components.keys()]; } });
}
export function compilePage(manifest, sources, registry) {
  fields(manifest, ['schemaVersion','route','sections'], 'manifest');
  if (manifest.schemaVersion !== SCHEMA) throw new CompositionError('unsupported-schema','schemaVersion');
  if (typeof manifest.route !== 'string' || !/^\/[a-z0-9\-/]*$/.test(manifest.route)) throw new CompositionError('invalid-route','route');
  if (!record(sources)) throw new CompositionError('invalid-sources','sources');
  if (!Array.isArray(manifest.sections) || manifest.sections.length > 50) throw new CompositionError('invalid-sections','sections');
  const ids = new Set();
  const sections = manifest.sections.map((item,index) => {
    const path = 'sections[' + index + ']';
    fields(item, ['id','type','variant','dataRef'],path);
    if (typeof item.id !== 'string' || !KEY.test(item.id)) throw new CompositionError('invalid-id',path+'.id');
    if (ids.has(item.id)) throw new CompositionError('duplicate-id',path+'.id');
    ids.add(item.id);
    const def = registry?.get?.(item.type);
    if (!def) throw new CompositionError('unknown-component',path+'.type');
    if (!def.variants.includes(item.variant)) throw new CompositionError('unsupported-variant',path+'.variant');
    let data;
    try { data = copyJson(resolve(sources,item.dataRef)); }
    catch (error) {
      if (error instanceof CompositionError) throw error;
      throw new CompositionError('invalid-data',path+'.dataRef');
    }
    let valid = false;
    try { valid = def.validate(data,item.variant) === true; } catch (_) { /* no data or stack leak */ }
    if (!valid) throw new CompositionError('invalid-data',path+'.dataRef');
    return Object.freeze({ id:item.id, type:item.type, variant:item.variant, data:freezeJson(data), def });
  });
  return Object.freeze({ route:manifest.route, sections:Object.freeze(sections) });
}
export function renderCompiled(compiled) {
  // This function returns descriptors from registered code; it does NOT mount a DOM.
  return compiled.sections.map(s => ({ id:s.id, type:s.type, result:s.def.render(s.data,{ id:s.id, variant:s.variant }) }));
}
