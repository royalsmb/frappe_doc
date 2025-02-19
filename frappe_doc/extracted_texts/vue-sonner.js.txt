var At = Object.defineProperty;
var Mt = (r, o, e) => o in r ? At(r, o, { enumerable: !0, configurable: !0, writable: !0, value: e }) : r[o] = e;
var k = (r, o, e) => (Mt(r, typeof o != "symbol" ? o + "" : o, e), e);
import { openBlock as l, createElementBlock as f, createElementVNode as O, ref as p, watchEffect as W, defineComponent as gt, computed as b, onMounted as kt, onUnmounted as Ht, normalizeClass as F, normalizeStyle as Et, unref as it, createVNode as V, createCommentVNode as N, createBlock as X, resolveDynamicComponent as st, mergeProps as rt, Fragment as R, renderSlot as P, normalizeProps as Tt, createTextVNode as Bt, toDisplayString as nt, renderList as ft, useAttrs as Dt, nextTick as Lt, watch as $t, withCtx as K } from "vue";
function Ot(r) {
  if (!r || typeof document > "u")
    return;
  let o = document.head || document.getElementsByTagName("head")[0], e = document.createElement("style");
  e.type = "text/css", o.appendChild(e), e.styleSheet ? e.styleSheet.cssText = r : e.appendChild(document.createTextNode(r));
}
Ot("[data-sonner-toaster][dir=ltr],html[dir=ltr]{--toast-icon-margin-start:-3px;--toast-icon-margin-end:4px;--toast-svg-margin-start:-1px;--toast-svg-margin-end:0px;--toast-button-margin-start:auto;--toast-button-margin-end:0;--toast-close-button-start:0;--toast-close-button-end:unset;--toast-close-button-transform:translate(-35%, -35%)}[data-sonner-toaster][dir=rtl],html[dir=rtl]{--toast-icon-margin-start:4px;--toast-icon-margin-end:-3px;--toast-svg-margin-start:0px;--toast-svg-margin-end:-1px;--toast-button-margin-start:0;--toast-button-margin-end:auto;--toast-close-button-start:unset;--toast-close-button-end:0;--toast-close-button-transform:translate(35%, -35%)}[data-sonner-toaster]{position:fixed;width:var(--width);font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;--gray1:hsl(0, 0%, 99%);--gray2:hsl(0, 0%, 97.3%);--gray3:hsl(0, 0%, 95.1%);--gray4:hsl(0, 0%, 93%);--gray5:hsl(0, 0%, 90.9%);--gray6:hsl(0, 0%, 88.7%);--gray7:hsl(0, 0%, 85.8%);--gray8:hsl(0, 0%, 78%);--gray9:hsl(0, 0%, 56.1%);--gray10:hsl(0, 0%, 52.3%);--gray11:hsl(0, 0%, 43.5%);--gray12:hsl(0, 0%, 9%);--border-radius:8px;box-sizing:border-box;padding:0;margin:0;list-style:none;outline:0;z-index:999999999}[data-sonner-toaster][data-x-position=right]{right:max(var(--offset),env(safe-area-inset-right))}[data-sonner-toaster][data-x-position=left]{left:max(var(--offset),env(safe-area-inset-left))}[data-sonner-toaster][data-x-position=center]{left:50%;transform:translateX(-50%)}[data-sonner-toaster][data-y-position=top]{top:max(var(--offset),env(safe-area-inset-top))}[data-sonner-toaster][data-y-position=bottom]{bottom:max(var(--offset),env(safe-area-inset-bottom))}[data-sonner-toast]{--y:translateY(100%);--lift-amount:calc(var(--lift) * var(--gap));z-index:var(--z-index);position:absolute;opacity:0;transform:var(--y);touch-action:none;will-change:transform,opacity,height;transition:transform .4s,opacity .4s,height .4s,box-shadow .2s;box-sizing:border-box;outline:0;overflow-wrap:anywhere}[data-sonner-toast][data-styled=true]{padding:16px;background:var(--normal-bg);border:1px solid var(--normal-border);color:var(--normal-text);border-radius:var(--border-radius);box-shadow:0 4px 12px rgba(0,0,0,.1);width:var(--width);font-size:13px;display:flex;align-items:center;gap:6px}[data-sonner-toast]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast][data-y-position=top]{top:0;--y:translateY(-100%);--lift:1;--lift-amount:calc(1 * var(--gap))}[data-sonner-toast][data-y-position=bottom]{bottom:0;--y:translateY(100%);--lift:-1;--lift-amount:calc(var(--lift) * var(--gap))}[data-sonner-toast] [data-description]{font-weight:400;line-height:1.4;color:inherit}[data-sonner-toast] [data-title]{font-weight:500;line-height:1.5;color:inherit}[data-sonner-toast] [data-icon]{display:flex;height:16px;width:16px;position:relative;justify-content:flex-start;align-items:center;flex-shrink:0;margin-left:var(--toast-icon-margin-start);margin-right:var(--toast-icon-margin-end)}[data-sonner-toast][data-promise=true] [data-icon]>svg{opacity:0;transform:scale(.8);transform-origin:center;animation:sonner-fade-in .3s ease forwards}[data-sonner-toast] [data-icon]>*{flex-shrink:0}[data-sonner-toast] [data-icon] svg{margin-left:var(--toast-svg-margin-start);margin-right:var(--toast-svg-margin-end)}[data-sonner-toast] [data-content]{display:flex;flex-direction:column;gap:2px;transform:translateZ(0)}[data-sonner-toast] [data-button]{border-radius:4px;padding-left:8px;padding-right:8px;height:24px;font-size:12px;color:var(--normal-bg);background:var(--normal-text);margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end);border:none;cursor:pointer;outline:0;display:flex;align-items:center;flex-shrink:0;transition:opacity .4s,box-shadow .2s}[data-sonner-toast] [data-button]:focus-visible{box-shadow:0 0 0 2px rgba(0,0,0,.4)}[data-sonner-toast] [data-button]:first-of-type{margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end)}[data-sonner-toast] [data-cancel]{color:var(--normal-text);background:rgba(0,0,0,.08)}[data-sonner-toast][data-theme=dark] [data-cancel]{background:rgba(255,255,255,.3)}[data-sonner-toast] [data-close-button]{position:absolute;left:var(--toast-close-button-start);right:var(--toast-close-button-end);top:0;height:20px;width:20px;display:flex;justify-content:center;align-items:center;padding:0;background:var(--gray1);color:var(--gray12);border:1px solid var(--gray4);transform:var(--toast-close-button-transform);border-radius:50%;cursor:pointer;z-index:1;transition:opacity .1s,background .2s,border-color .2s}[data-sonner-toast] [data-close-button]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast] [data-disabled=true]{cursor:not-allowed}[data-sonner-toast]:hover [data-close-button]:hover{background:var(--gray2);border-color:var(--gray5)}[data-sonner-toast][data-swiping=true]:before{content:'';position:absolute;left:0;right:0;height:100%;z-index:-1}[data-sonner-toast][data-y-position=top][data-swiping=true]:before{bottom:50%;transform:scaleY(3) translateY(50%)}[data-sonner-toast][data-y-position=bottom][data-swiping=true]:before{top:50%;transform:scaleY(3) translateY(-50%)}[data-sonner-toast][data-swiping=false][data-removed=true]:before{content:'';position:absolute;inset:0;transform:scaleY(2)}[data-sonner-toast]:after{content:'';position:absolute;left:0;height:calc(var(--gap) + 1px);bottom:100%;width:100%}[data-sonner-toast][data-mounted=true]{--y:translateY(0);opacity:1}[data-sonner-toast][data-expanded=false][data-front=false]{--scale:var(--toasts-before) * 0.05 + 1;--y:translateY(calc(var(--lift-amount) * var(--toasts-before))) scale(calc(-1 * var(--scale)));height:var(--front-toast-height)}[data-sonner-toast]>*{transition:opacity .4s}[data-sonner-toast][data-expanded=false][data-front=false][data-styled=true]>*{opacity:0}[data-sonner-toast][data-visible=false]{opacity:0;pointer-events:none}[data-sonner-toast][data-mounted=true][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset)));height:var(--initial-height)}[data-sonner-toast][data-removed=true][data-front=true][data-swipe-out=false]{--y:translateY(calc(var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset) + var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=false]{--y:translateY(40%);opacity:0;transition:transform .5s,opacity .2s}[data-sonner-toast][data-removed=true][data-front=false]:before{height:calc(var(--initial-height) + 20%)}[data-sonner-toast][data-swiping=true]{transform:var(--y) translateY(var(--swipe-amount,0));transition:none}[data-sonner-toast][data-swipe-out=true][data-y-position=bottom],[data-sonner-toast][data-swipe-out=true][data-y-position=top]{animation:swipe-out .2s ease-out forwards}@keyframes swipe-out{from{transform:translateY(calc(var(--lift) * var(--offset) + var(--swipe-amount)));opacity:1}to{transform:translateY(calc(var(--lift) * var(--offset) + var(--swipe-amount) + var(--lift) * -100%));opacity:0}}@media (max-width:600px){[data-sonner-toaster]{position:fixed;--mobile-offset:16px;right:var(--mobile-offset);left:var(--mobile-offset);width:100%}[data-sonner-toaster] [data-sonner-toast]{left:0;right:0;width:calc(100% - 32px)}[data-sonner-toaster][data-x-position=left]{left:var(--mobile-offset)}[data-sonner-toaster][data-y-position=bottom]{bottom:20px}[data-sonner-toaster][data-y-position=top]{top:20px}[data-sonner-toaster][data-x-position=center]{left:var(--mobile-offset);right:var(--mobile-offset);transform:none}}[data-sonner-toaster][data-theme=light]{--normal-bg:#fff;--normal-border:var(--gray4);--normal-text:var(--gray12);--success-bg:hsl(143, 85%, 96%);--success-border:hsl(145, 92%, 91%);--success-text:hsl(140, 100%, 27%);--info-bg:hsl(208, 100%, 97%);--info-border:hsl(221, 91%, 91%);--info-text:hsl(210, 92%, 45%);--warning-bg:hsl(49, 100%, 97%);--warning-border:hsl(49, 91%, 91%);--warning-text:hsl(31, 92%, 45%);--error-bg:hsl(359, 100%, 97%);--error-border:hsl(359, 100%, 94%);--error-text:hsl(360, 100%, 45%)}[data-sonner-toaster][data-theme=light] [data-sonner-toast][data-invert=true]{--normal-bg:#000;--normal-border:hsl(0, 0%, 20%);--normal-text:var(--gray1)}[data-sonner-toaster][data-theme=dark] [data-sonner-toast][data-invert=true]{--normal-bg:#fff;--normal-border:var(--gray3);--normal-text:var(--gray12)}[data-sonner-toaster][data-theme=dark]{--normal-bg:#000;--normal-border:hsl(0, 0%, 20%);--normal-text:var(--gray1);--success-bg:hsl(150, 100%, 6%);--success-border:hsl(147, 100%, 12%);--success-text:hsl(150, 86%, 65%);--info-bg:hsl(215, 100%, 6%);--info-border:hsl(223, 100%, 12%);--info-text:hsl(216, 87%, 65%);--warning-bg:hsl(64, 100%, 6%);--warning-border:hsl(60, 100%, 12%);--warning-text:hsl(46, 87%, 65%);--error-bg:hsl(358, 76%, 10%);--error-border:hsl(357, 89%, 16%);--error-text:hsl(358, 100%, 81%)}[data-rich-colors=true] [data-sonner-toast][data-type=success]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true] [data-sonner-toast][data-type=success] [data-close-button]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true] [data-sonner-toast][data-type=info]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true] [data-sonner-toast][data-type=info] [data-close-button]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true] [data-sonner-toast][data-type=warning]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true] [data-sonner-toast][data-type=warning] [data-close-button]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true] [data-sonner-toast][data-type=error]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}[data-rich-colors=true] [data-sonner-toast][data-type=error] [data-close-button]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}.sonner-loading-wrapper{--size:16px;height:var(--size);width:var(--size);position:absolute;inset:0;z-index:10}.sonner-loading-wrapper[data-visible=false]{transform-origin:center;animation:sonner-fade-out .2s ease forwards}.sonner-spinner{position:relative;top:50%;left:50%;height:var(--size);width:var(--size)}.sonner-loading-bar{animation:sonner-spin 1.2s linear infinite;background:var(--gray11);border-radius:6px;height:8%;left:-10%;position:absolute;top:-3.9%;width:24%}.sonner-loading-bar:first-child{animation-delay:-1.2s;transform:rotate(.0001deg) translate(146%)}.sonner-loading-bar:nth-child(2){animation-delay:-1.1s;transform:rotate(30deg) translate(146%)}.sonner-loading-bar:nth-child(3){animation-delay:-1s;transform:rotate(60deg) translate(146%)}.sonner-loading-bar:nth-child(4){animation-delay:-.9s;transform:rotate(90deg) translate(146%)}.sonner-loading-bar:nth-child(5){animation-delay:-.8s;transform:rotate(120deg) translate(146%)}.sonner-loading-bar:nth-child(6){animation-delay:-.7s;transform:rotate(150deg) translate(146%)}.sonner-loading-bar:nth-child(7){animation-delay:-.6s;transform:rotate(180deg) translate(146%)}.sonner-loading-bar:nth-child(8){animation-delay:-.5s;transform:rotate(210deg) translate(146%)}.sonner-loading-bar:nth-child(9){animation-delay:-.4s;transform:rotate(240deg) translate(146%)}.sonner-loading-bar:nth-child(10){animation-delay:-.3s;transform:rotate(270deg) translate(146%)}.sonner-loading-bar:nth-child(11){animation-delay:-.2s;transform:rotate(300deg) translate(146%)}.sonner-loading-bar:nth-child(12){animation-delay:-.1s;transform:rotate(330deg) translate(146%)}@keyframes sonner-fade-in{0%{opacity:0;transform:scale(.8)}100%{opacity:1;transform:scale(1)}}@keyframes sonner-fade-out{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(.8)}}@keyframes sonner-spin{0%{opacity:1}100%{opacity:.15}}@media (prefers-reduced-motion){.sonner-loading-bar,[data-sonner-toast],[data-sonner-toast]>*{transition:none!important;animation:none!important}}.sonner-loader{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);transform-origin:center;transition:opacity .2s,transform .2s}.sonner-loader[data-visible=false]{opacity:0;transform:scale(.8) translate(-50%,-50%)}");
let pt = 0;
class Yt {
  constructor() {
    k(this, "subscribers");
    k(this, "toasts");
    // We use arrow functions to maintain the correct `this` reference
    k(this, "subscribe", (o) => (this.subscribers.push(o), () => {
      const e = this.subscribers.indexOf(o);
      this.subscribers.splice(e, 1);
    }));
    k(this, "publish", (o) => {
      this.subscribers.forEach((e) => e(o));
    });
    k(this, "addToast", (o) => {
      this.publish(o), this.toasts = [...this.toasts, o];
    });
    k(this, "create", (o) => {
      var v;
      const { message: e, ...a } = o, m = typeof o.id == "number" || o.id && ((v = o.id) == null ? void 0 : v.length) > 0 ? o.id : pt++, u = this.toasts.find((d) => d.id === m), g = o.dismissible === void 0 ? !0 : o.dismissible;
      return u ? this.toasts = this.toasts.map((d) => d.id === m ? (this.publish({ ...d, ...o, id: m, title: e }), {
        ...d,
        ...o,
        id: m,
        dismissible: g,
        title: e
      }) : d) : this.addToast({ title: e, ...a, dismissible: g, id: m }), m;
    });
    k(this, "dismiss", (o) => (o || this.toasts.forEach((e) => {
      this.subscribers.forEach(
        (a) => a({ id: e.id, dismiss: !0 })
      );
    }), this.subscribers.forEach((e) => e({ id: o, dismiss: !0 })), o));
    k(this, "message", (o, e) => this.create({ ...e, message: o, type: "default" }));
    k(this, "error", (o, e) => this.create({ ...e, type: "error", message: o }));
    k(this, "success", (o, e) => this.create({ ...e, type: "success", message: o }));
    k(this, "info", (o, e) => this.create({ ...e, type: "info", message: o }));
    k(this, "warning", (o, e) => this.create({ ...e, type: "warning", message: o }));
    k(this, "loading", (o, e) => this.create({ ...e, type: "loading", message: o }));
    k(this, "promise", (o, e) => {
      if (!e)
        return;
      let a;
      e.loading !== void 0 && (a = this.create({
        ...e,
        promise: o,
        type: "loading",
        message: e.loading,
        description: typeof e.description != "function" ? e.description : void 0
      }));
      const m = o instanceof Promise ? o : o();
      let u = a !== void 0;
      return m.then((g) => {
        if (g && // @ts-expect-error
        typeof g.ok == "boolean" && // @ts-expect-error
        !g.ok) {
          u = !1;
          const v = typeof e.error == "function" ? (
            // @ts-expect-error
            e.error(`HTTP error! status: ${response.status}`)
          ) : e.error, d = typeof e.description == "function" ? (
            // @ts-expect-error
            e.description(`HTTP error! status: ${response.status}`)
          ) : e.description;
          this.create({ id: a, type: "error", message: v, description: d });
        } else if (e.success !== void 0) {
          u = !1;
          const v = typeof e.success == "function" ? e.success(g) : e.success, d = typeof e.description == "function" ? (
            // @ts-expect-error
            e.description(g)
          ) : e.description;
          this.create({ id: a, type: "success", message: v, description: d });
        }
      }).catch((g) => {
        if (e.error !== void 0) {
          u = !1;
          const v = typeof e.error == "function" ? e.error(g) : e.error, d = typeof e.description == "function" ? (
            // @ts-expect-error
            e.description(g)
          ) : e.description;
          this.create({ id: a, type: "error", message: v, description: d });
        }
      }).finally(() => {
        var g;
        u && (this.dismiss(a), a = void 0), (g = e.finally) == null || g.call(e);
      }), a;
    });
    // We can't provide the toast we just created as a prop as we didn't create it yet, so we can create a default toast object, I just don't know how to use function in argument when calling()?
    k(this, "custom", (o, e) => {
      const a = (e == null ? void 0 : e.id) || pt++;
      return this.publish({ component: o, id: a, ...e }), a;
    });
    this.subscribers = [], this.toasts = [];
  }
}
const C = new Yt(), Nt = (r, o) => {
  const e = (o == null ? void 0 : o.id) || pt++;
  return C.create({
    message: r,
    id: e,
    type: "default",
    ...o
  }), e;
}, Ft = Nt, Fe = Object.assign(Ft, {
  success: C.success,
  info: C.info,
  warning: C.warning,
  error: C.error,
  custom: C.custom,
  message: C.message,
  promise: C.promise,
  dismiss: C.dismiss,
  loading: C.loading
}), G = (r, o) => {
  const e = r.__vccOpts || r;
  for (const [a, m] of o)
    e[a] = m;
  return e;
}, Rt = {}, Wt = {
  xmlns: "http://www.w3.org/2000/svg",
  width: "12",
  height: "12",
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  "stoke-width": "1.5",
  "stroke-linecap": "round",
  "stroke-linejoin": "round"
}, Ut = /* @__PURE__ */ O("line", {
  x1: "18",
  y1: "6",
  x2: "6",
  y2: "18"
}, null, -1), Vt = /* @__PURE__ */ O("line", {
  x1: "6",
  y1: "6",
  x2: "18",
  y2: "18"
}, null, -1), _t = [
  Ut,
  Vt
];
function jt(r, o) {
  return l(), f("svg", Wt, _t);
}
const Kt = /* @__PURE__ */ G(Rt, [["render", jt]]), Xt = () => {
  const r = p(!1);
  return W(() => {
    const o = () => {
      r.value = document.hidden;
    };
    return document.addEventListener("visibilitychange", o), () => window.removeEventListener("visibilitychange", o);
  }), {
    isDocumentHidden: r
  };
}, Gt = ["aria-live", "data-styled", "data-mounted", "data-promise", "data-removed", "data-visible", "data-y-position", "data-x-position", "data-index", "data-front", "data-swiping", "data-dismissible", "data-type", "data-invert", "data-swipe-out", "data-expanded"], Zt = ["aria-label", "data-disabled"], qt = {
  key: 0,
  "data-icon": ""
}, Jt = { "data-content": "" }, Qt = 4e3, te = 14, ee = 20, ae = 200, oe = /* @__PURE__ */ gt({
  __name: "Toast",
  props: {
    toast: {},
    toasts: {},
    index: {},
    expanded: { type: Boolean },
    invert: { type: Boolean },
    heights: {},
    gap: {},
    position: {},
    visibleToasts: {},
    expandByDefault: { type: Boolean },
    closeButton: { type: Boolean },
    interacting: { type: Boolean },
    duration: {},
    descriptionClass: {},
    style: {},
    cancelButtonStyle: {},
    actionButtonStyle: {},
    unstyled: { type: Boolean },
    loadingIcon: {},
    class: {},
    classes: {},
    icons: {},
    closeButtonAriaLabel: {},
    pauseWhenPageIsHidden: { type: Boolean },
    cn: { type: Function }
  },
  emits: ["update:heights", "removeToast"],
  setup(r, { emit: o }) {
    const e = o, a = r, m = p(!1), u = p(!1), g = p(!1), v = p(!1), d = p(0), H = p(0);
    let D = 0;
    const E = p(null), z = b(() => a.index === 0), A = b(() => a.index + 1 <= a.visibleToasts), T = b(() => a.toast.type), _ = b(() => a.toast.dismissible !== !1), lt = b(() => {
      var t, i, w, S, x, h, M;
      return a.cn(
        (t = a.classes) == null ? void 0 : t.toast,
        (w = (i = a.toast) == null ? void 0 : i.classes) == null ? void 0 : w.toast,
        (S = a.classes) == null ? void 0 : S.default,
        (x = a.classes) == null ? void 0 : x[a.toast.type || "default"],
        (M = (h = a.toast) == null ? void 0 : h.classes) == null ? void 0 : M[a.toast.type || "default"]
      );
    }), dt = a.toast.style || {}, Z = b(
      () => a.heights.findIndex((t) => t.toastId === a.toast.id) || 0
    ), ct = b(() => a.toast.closeButton ?? a.closeButton), s = b(
      () => a.toast.duration || a.duration || Qt
    ), n = p(0), c = p(0), B = p(s.value), $ = p(0), y = p(null), L = b(() => a.position.split("-")), q = b(() => L.value[0]), J = b(() => L.value[1]), Q = b(() => typeof a.toast.title != "string"), tt = b(() => typeof a.toast.description != "string"), et = b(() => a.heights.reduce((t, i, w) => w >= Z.value ? t : t + i.height, 0)), at = Xt(), ot = b(() => a.toast.invert || a.invert), U = b(() => T.value === "loading");
    kt(() => {
      if (!m.value)
        return;
      const t = E.value, i = t == null ? void 0 : t.style.height;
      t.style.height = "auto";
      const w = t.getBoundingClientRect().height;
      t.style.height = i, H.value = w;
      let S;
      a.heights.find(
        (h) => h.toastId === a.toast.id
      ) ? S = a.heights.map(
        (h) => h.toastId === a.toast.id ? { ...h, height: w } : h
      ) : S = [
        {
          toastId: a.toast.id,
          height: w,
          position: a.toast.position
        },
        ...a.heights
      ], e("update:heights", S);
    });
    const I = () => {
      u.value = !0, d.value = c.value, setTimeout(() => {
        e("removeToast", a.toast);
      }, ae);
    }, ut = () => {
      var t, i;
      U.value || !_.value || (I(), (i = (t = a.toast).onDismiss) == null || i.call(t, a.toast));
    }, It = (t) => {
      U.value || !_.value || (D = Date.now(), d.value = c.value, t.target.setPointerCapture(t.pointerId), t.target.tagName !== "BUTTON" && (g.value = !0, y.value = { x: t.clientX, y: t.clientY }));
    }, Pt = (t) => {
      var x, h, M, Y;
      if (v.value)
        return;
      y.value = null;
      const i = Number(
        ((x = E.value) == null ? void 0 : x.style.getPropertyValue("--swipe-amount").replace("px", "")) || 0
      ), w = Date.now() - D || 50, S = Math.abs(i) / w;
      if (Math.abs(i) >= ee || S > 0.11) {
        d.value = c.value, (M = (h = a.toast).onDismiss) == null || M.call(h, a.toast), I(), v.value = !0;
        return;
      }
      (Y = E.value) == null || Y.style.setProperty("--swipe-amount", "0px"), g.value = !1;
    }, zt = (t) => {
      var Y;
      if (!y.value)
        return;
      const i = t.clientY - y.value.y, w = t.clientX - y.value.x, x = (L.value[0] === "top" ? Math.min : Math.max)(0, i), h = t.pointerType === "touch" ? 10 : 2;
      Math.abs(x) > h ? (Y = E.value) == null || Y.style.setProperty("--swipe-amount", `${i}px`) : Math.abs(w) > h && (y.value = null);
    };
    return W(() => {
      c.value = Z.value * te + et.value;
    }), W((t) => {
      if (a.toast.promise && T.value === "loading" || a.toast.duration === 1 / 0 || a.toast.type === "loading")
        return;
      let i;
      const w = () => {
        if ($.value < n.value) {
          const x = Date.now() - n.value;
          B.value = B.value - x;
        }
        $.value = Date.now();
      }, S = () => {
        n.value = Date.now(), i = setTimeout(() => {
          var x, h;
          (h = (x = a.toast).onAutoClose) == null || h.call(x, a.toast), I();
        }, B.value);
      };
      a.expanded || a.interacting || a.pauseWhenPageIsHidden && at ? w() : S(), t(() => {
        clearTimeout(i);
      });
    }), W(() => {
      a.toast.delete && I();
    }), kt(() => {
      if (E.value) {
        const t = E.value.getBoundingClientRect().height;
        H.value = t;
        const i = [
          { toastId: a.toast.id, height: t, position: a.toast.position },
          ...a.heights
        ];
        e("update:heights", i);
      }
      m.value = !0;
    }), Ht(() => {
      if (E.value) {
        const t = a.heights.filter(
          (i) => i.toastId !== a.toast.id
        );
        e("update:heights", t);
      }
    }), (t, i) => {
      var w, S, x, h, M, Y, ht, mt, vt, yt, bt, wt;
      return l(), f("li", {
        "aria-live": t.toast.important ? "assertive" : "polite",
        "aria-atomic": "true",
        role: "status",
        tabindex: "0",
        ref_key: "toastRef",
        ref: E,
        "data-sonner-toast": "",
        class: F(lt.value),
        "data-styled": !(t.toast.component || (w = t.toast) != null && w.unstyled || t.unstyled),
        "data-mounted": m.value,
        "data-promise": !!t.toast.promise,
        "data-removed": u.value,
        "data-visible": A.value,
        "data-y-position": q.value,
        "data-x-position": J.value,
        "data-index": t.index,
        "data-front": z.value,
        "data-swiping": g.value,
        "data-dismissible": _.value,
        "data-type": T.value,
        "data-invert": ot.value,
        "data-swipe-out": v.value,
        "data-expanded": !!(t.expanded || t.expandByDefault && m.value),
        style: Et({
          "--index": t.index,
          "--toasts-before": t.index,
          "--z-index": t.toasts.length - t.index,
          "--offset": `${u.value ? d.value : c.value}px`,
          "--initial-height": t.expandByDefault ? "auto" : `${H.value}px`,
          ...t.style,
          ...it(dt)
        }),
        onPointerdown: It,
        onPointerup: Pt,
        onPointermove: zt
      }, [
        ct.value && !t.toast.component ? (l(), f("button", {
          key: 0,
          "aria-label": t.closeButtonAriaLabel || "Close toast",
          "data-disabled": U.value,
          "data-close-button": "",
          class: F(t.cn((S = t.classes) == null ? void 0 : S.closeButton, (h = (x = t.toast) == null ? void 0 : x.classes) == null ? void 0 : h.closeButton)),
          onClick: ut
        }, [
          V(Kt)
        ], 10, Zt)) : N("", !0),
        t.toast.component ? (l(), X(st(t.toast.component), rt({ key: 1 }, t.toast.componentProps, { onCloseToast: I }), null, 16)) : (l(), f(R, { key: 2 }, [
          T.value !== "default" || t.toast.icon || t.toast.promise ? (l(), f("div", qt, [
            (t.toast.promise || T.value === "loading") && !t.toast.icon ? P(t.$slots, "loading-icon", { key: 0 }) : N("", !0),
            t.toast.icon ? (l(), X(st(t.toast.icon), { key: 1 })) : (l(), f(R, { key: 2 }, [
              T.value === "success" ? P(t.$slots, "success-icon", { key: 0 }) : T.value === "error" ? P(t.$slots, "error-icon", { key: 1 }) : T.value === "warning" ? P(t.$slots, "warning-icon", { key: 2 }) : T.value === "info" ? P(t.$slots, "info-icon", { key: 3 }) : N("", !0)
            ], 64))
          ])) : N("", !0),
          O("div", Jt, [
            O("div", {
              "data-title": "",
              class: F(t.cn((M = t.classes) == null ? void 0 : M.title, (Y = t.toast.classes) == null ? void 0 : Y.title))
            }, [
              Q.value ? (l(), X(st(t.toast.title), Tt(rt({ key: 0 }, t.toast.componentProps)), null, 16)) : (l(), f(R, { key: 1 }, [
                Bt(nt(t.toast.title), 1)
              ], 64))
            ], 2),
            t.toast.description ? (l(), f("div", {
              key: 0,
              "data-description": "",
              class: F(
                t.cn(
                  t.descriptionClass,
                  t.toast.descriptionClass,
                  (ht = t.classes) == null ? void 0 : ht.description,
                  (mt = t.toast.classes) == null ? void 0 : mt.description
                )
              )
            }, [
              tt.value ? (l(), X(st(t.toast.description), Tt(rt({ key: 0 }, t.toast.componentProps)), null, 16)) : (l(), f(R, { key: 1 }, [
                Bt(nt(t.toast.description), 1)
              ], 64))
            ], 2)) : N("", !0)
          ]),
          t.toast.cancel ? (l(), f("button", {
            key: 1,
            class: F(t.cn((vt = t.classes) == null ? void 0 : vt.cancelButton, (yt = t.toast.classes) == null ? void 0 : yt.cancelButton)),
            "data-button": "",
            "data-cancel": "",
            onClick: i[0] || (i[0] = () => {
              var j;
              I(), (j = t.toast.cancel) != null && j.onClick && t.toast.cancel.onClick();
            })
          }, nt(t.toast.cancel.label), 3)) : N("", !0),
          t.toast.action ? (l(), f("button", {
            key: 2,
            class: F(t.cn((bt = t.classes) == null ? void 0 : bt.actionButton, (wt = t.toast.classes) == null ? void 0 : wt.actionButton)),
            "data-button": "",
            onClick: i[1] || (i[1] = (j) => {
              var xt;
              (xt = t.toast.action) == null || xt.onClick(j), !j.defaultPrevented && I();
            })
          }, nt(t.toast.action.label), 3)) : N("", !0)
        ], 64))
      ], 46, Gt);
    };
  }
}), se = ["data-visible"], ne = { class: "sonner-spinner" }, re = /* @__PURE__ */ gt({
  __name: "Loader",
  props: {
    visible: { type: Boolean }
  },
  setup(r) {
    const o = Array(12).fill(0);
    return (e, a) => (l(), f("div", {
      class: "sonner-loading-wrapper",
      "data-visible": e.visible
    }, [
      O("div", ne, [
        (l(!0), f(R, null, ft(it(o), (m) => (l(), f("div", {
          key: `spinner-bar-${m}`,
          class: "sonner-loading-bar"
        }))), 128))
      ])
    ], 8, se));
  }
}), ie = {}, le = {
  xmlns: "http://www.w3.org/2000/svg",
  viewBox: "0 0 20 20",
  fill: "currentColor",
  height: "20",
  width: "20"
}, de = /* @__PURE__ */ O("path", {
  "fill-rule": "evenodd",
  d: "M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z",
  "clip-rule": "evenodd"
}, null, -1), ce = [
  de
];
function ue(r, o) {
  return l(), f("svg", le, ce);
}
const fe = /* @__PURE__ */ G(ie, [["render", ue]]), pe = {}, ge = {
  xmlns: "http://www.w3.org/2000/svg",
  viewBox: "0 0 20 20",
  fill: "currentColor",
  height: "20",
  width: "20"
}, he = /* @__PURE__ */ O("path", {
  "fill-rule": "evenodd",
  d: "M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z",
  "clip-rule": "evenodd"
}, null, -1), me = [
  he
];
function ve(r, o) {
  return l(), f("svg", ge, me);
}
const ye = /* @__PURE__ */ G(pe, [["render", ve]]), be = {}, we = {
  xmlns: "http://www.w3.org/2000/svg",
  viewBox: "0 0 24 24",
  fill: "currentColor",
  height: "20",
  width: "20"
}, xe = /* @__PURE__ */ O("path", {
  "fill-rule": "evenodd",
  d: "M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z",
  "clip-rule": "evenodd"
}, null, -1), ke = [
  xe
];
function Te(r, o) {
  return l(), f("svg", we, ke);
}
const Be = /* @__PURE__ */ G(be, [["render", Te]]), $e = {}, Se = {
  xmlns: "http://www.w3.org/2000/svg",
  viewBox: "0 0 20 20",
  fill: "currentColor",
  height: "20",
  width: "20"
}, Ce = /* @__PURE__ */ O("path", {
  "fill-rule": "evenodd",
  d: "M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-5a.75.75 0 01.75.75v4.5a.75.75 0 01-1.5 0v-4.5A.75.75 0 0110 5zm0 10a1 1 0 100-2 1 1 0 000 2z",
  "clip-rule": "evenodd"
}, null, -1), Ee = [
  Ce
];
function Ie(r, o) {
  return l(), f("svg", Se, Ee);
}
const Pe = /* @__PURE__ */ G($e, [["render", Ie]]), ze = ["aria-label"], Ae = ["dir", "data-theme", "data-rich-colors", "data-y-position", "data-x-position"], Me = 3, St = "32px", Oe = 4e3, He = 356, Ct = 14, De = typeof window < "u" && typeof document < "u", Le = /* @__PURE__ */ gt({
  name: "Toaster",
  inheritAttrs: !1,
  __name: "Toaster",
  props: {
    invert: { type: Boolean, default: !1 },
    theme: { default: "light" },
    position: { default: "bottom-right" },
    hotkey: { default: () => ["altKey", "KeyT"] },
    richColors: { type: Boolean, default: !1 },
    expand: { type: Boolean, default: !1 },
    duration: { default: Oe },
    gap: { default: Ct },
    visibleToasts: { default: Me },
    closeButton: { type: Boolean, default: !1 },
    toastOptions: { default: () => ({}) },
    class: { default: "" },
    style: { default: () => ({}) },
    offset: { default: St },
    dir: { default: "auto" },
    icons: {},
    containerAriaLabel: { default: "Notifications" },
    pauseWhenPageIsHidden: { type: Boolean, default: !1 },
    cn: {}
  },
  setup(r) {
    function o(...s) {
      return s.filter(Boolean).join(" ");
    }
    function e() {
      if (typeof window > "u" || typeof document > "u")
        return "ltr";
      const s = document.documentElement.getAttribute("dir");
      return s === "auto" || !s ? window.getComputedStyle(document.documentElement).direction : s;
    }
    const a = r, m = Dt(), u = p([]), g = b(() => {
      const s = u.value.filter((n) => n.position).map((n) => n.position);
      return s.length > 0 ? Array.from(new Set([a.position].concat(s))) : [a.position];
    }), v = p([]), d = p(!1), H = p(!1), D = p(
      a.theme !== "system" ? a.theme : typeof window < "u" && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"
    ), E = b(() => a.cn || o), z = p(null), A = p(null), T = p(!1), _ = a.hotkey.join("+").replace(/Key/g, "").replace(/Digit/g, "");
    function lt(s) {
      v.value = v.value.filter(({ toastId: n }) => n !== s.id), u.value = u.value.filter(({ id: n }) => n !== s.id);
    }
    const dt = (s) => {
      var n, c;
      T.value && !((c = (n = s.currentTarget) == null ? void 0 : n.contains) != null && c.call(n, s.relatedTarget)) && (T.value = !1, A.value && (A.value.focus({ preventScroll: !0 }), A.value = null));
    }, Z = (s) => {
      s.target instanceof HTMLElement && s.target.dataset.dismissible === "false" || T.value || (T.value = !0, A.value = s.relatedTarget);
    }, ct = (s) => {
      s.target && s.target instanceof HTMLElement && s.target.dataset.dismissible === "false" || (H.value = !1);
    };
    return W((s) => {
      const n = C.subscribe((c) => {
        if (c.dismiss) {
          u.value = u.value.map(
            (B) => B.id === c.id ? { ...B, delete: !0 } : B
          );
          return;
        }
        Lt(() => {
          const B = u.value.findIndex(
            ($) => $.id === c.id
          );
          B !== -1 ? u.value.splice(B, 1, c) : u.value = [c, ...u.value];
        });
      });
      s(() => {
        n();
      });
    }), $t(
      () => a.theme,
      (s) => {
        if (s !== "system") {
          D.value = s;
          return;
        }
        s === "system" && (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? D.value = "dark" : D.value = "light"), !(typeof window > "u") && window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", ({ matches: n }) => {
          n ? D.value = "dark" : D.value = "light";
        });
      }
    ), $t(
      () => z.value,
      () => {
        if (z.value)
          return () => {
            A.value && (A.value.focus({ preventScroll: !0 }), A.value = null, T.value = !1);
          };
      }
    ), W(() => {
      u.value.length <= 1 && (d.value = !1);
    }), W((s) => {
      function n(c) {
        const B = a.hotkey.every(
          (L) => c[L] || c.code === L
        ), $ = Array.isArray(z.value) ? z.value[0] : z.value;
        B && (d.value = !0, $ == null || $.focus());
        const y = document.activeElement === z.value || ($ == null ? void 0 : $.contains(document.activeElement));
        c.code === "Escape" && y && (d.value = !1);
      }
      De && (document.addEventListener("keydown", n), s(() => {
        document.removeEventListener("keydown", n);
      }));
    }), (s, n) => (l(), f("section", {
      "aria-label": `${s.containerAriaLabel} ${it(_)}`,
      tabIndex: -1
    }, [
      (l(!0), f(R, null, ft(g.value, (c, B) => {
        var $;
        return l(), f("ol", rt({
          key: c,
          ref_for: !0,
          ref_key: "listRef",
          ref: z,
          "data-sonner-toaster": "",
          class: s.class,
          dir: s.dir === "auto" ? e() : s.dir,
          tabIndex: -1,
          "data-theme": s.theme,
          "data-rich-colors": s.richColors,
          "data-y-position": c.split("-")[0],
          "data-x-position": c.split("-")[1],
          style: {
            "--front-toast-height": `${($ = v.value[0]) == null ? void 0 : $.height}px`,
            "--offset": typeof s.offset == "number" ? `${s.offset}px` : s.offset || St,
            "--width": `${He}px`,
            "--gap": `${Ct}px`,
            ...s.style,
            ...it(m).style
          },
          onBlur: dt,
          onFocus: Z,
          onMouseenter: n[1] || (n[1] = (y) => d.value = !0),
          onMousemove: n[2] || (n[2] = (y) => d.value = !0),
          onMouseleave: n[3] || (n[3] = () => {
            H.value || (d.value = !1);
          }),
          onPointerdown: ct,
          onPointerup: n[4] || (n[4] = (y) => H.value = !1)
        }, s.$attrs), [
          (l(!0), f(R, null, ft(u.value.filter(
            (y) => !y.position && B === 0 || y.position === c
          ), (y, L) => {
            var q, J, Q, tt, et, at, ot, U, I;
            return l(), X(oe, {
              key: y.id,
              index: L,
              toast: y,
              duration: ((q = s.toastOptions) == null ? void 0 : q.duration) ?? s.duration,
              class: F(((J = s.toastOptions) == null ? void 0 : J.class) ?? ""),
              descriptionClass: (Q = s.toastOptions) == null ? void 0 : Q.descriptionClass,
              invert: s.invert,
              visibleToasts: s.visibleToasts,
              closeButton: ((tt = s.toastOptions) == null ? void 0 : tt.closeButton) ?? s.closeButton,
              interacting: H.value,
              position: c,
              style: Et((et = s.toastOptions) == null ? void 0 : et.style),
              unstyled: (at = s.toastOptions) == null ? void 0 : at.unstyled,
              classes: (ot = s.toastOptions) == null ? void 0 : ot.classes,
              cancelButtonStyle: (U = s.toastOptions) == null ? void 0 : U.cancelButtonStyle,
              actionButtonStyle: (I = s.toastOptions) == null ? void 0 : I.actionButtonStyle,
              toasts: u.value,
              expandByDefault: s.expand,
              gap: s.gap,
              expanded: d.value,
              pauseWhenPageIsHidden: s.pauseWhenPageIsHidden,
              cn: E.value,
              heights: v.value,
              "onUpdate:heights": n[0] || (n[0] = (ut) => v.value = ut),
              onRemoveToast: lt
            }, {
              "loading-icon": K(() => [
                P(s.$slots, "loading-icon", {}, () => [
                  V(re, {
                    visible: y.type === "loading"
                  }, null, 8, ["visible"])
                ])
              ]),
              "success-icon": K(() => [
                P(s.$slots, "success-icon", {}, () => [
                  V(fe)
                ])
              ]),
              "error-icon": K(() => [
                P(s.$slots, "error-icon", {}, () => [
                  V(Pe)
                ])
              ]),
              "warning-icon": K(() => [
                P(s.$slots, "warning-icon", {}, () => [
                  V(Be)
                ])
              ]),
              "info-icon": K(() => [
                P(s.$slots, "info-icon", {}, () => [
                  V(ye)
                ])
              ]),
              _: 2
            }, 1032, ["index", "toast", "duration", "class", "descriptionClass", "invert", "visibleToasts", "closeButton", "interacting", "position", "style", "unstyled", "classes", "cancelButtonStyle", "actionButtonStyle", "toasts", "expandByDefault", "gap", "expanded", "pauseWhenPageIsHidden", "cn", "heights"]);
          }), 128))
        ], 16, Ae);
      }), 128))
    ], 8, ze));
  }
}), Re = {
  install(r) {
    r.component("Toaster", Le);
  }
};
export {
  Le as Toaster,
  Re as default,
  Fe as toast
};
//# sourceMappingURL=vue-sonner.js.map
