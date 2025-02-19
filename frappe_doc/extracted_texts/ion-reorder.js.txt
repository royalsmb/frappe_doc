/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { proxyCustomElement, HTMLElement, h, Host } from '@stencil/core/internal/client';
import { r as reorderThreeOutline, p as reorderTwoSharp } from './index7.js';
import { b as getIonMode } from './ionic-global.js';
import { d as defineCustomElement$2 } from './icon.js';

const reorderIosCss = ":host([slot]){display:none;line-height:0;z-index:100}.reorder-icon{display:block}::slotted(ion-icon){font-size:dynamic-font(16px)}.reorder-icon{font-size:2.125rem;opacity:0.4}";
const IonReorderIosStyle0 = reorderIosCss;

const reorderMdCss = ":host([slot]){display:none;line-height:0;z-index:100}.reorder-icon{display:block}::slotted(ion-icon){font-size:dynamic-font(16px)}.reorder-icon{font-size:1.9375rem;opacity:0.3}";
const IonReorderMdStyle0 = reorderMdCss;

const Reorder = /*@__PURE__*/ proxyCustomElement(class Reorder extends HTMLElement {
    constructor() {
        super();
        this.__registerHost();
        this.__attachShadow();
    }
    onClick(ev) {
        const reorderGroup = this.el.closest('ion-reorder-group');
        ev.preventDefault();
        // Only stop event propagation if the reorder is inside of an enabled
        // reorder group. This allows interaction with clickable children components.
        if (!reorderGroup || !reorderGroup.disabled) {
            ev.stopImmediatePropagation();
        }
    }
    render() {
        const mode = getIonMode(this);
        const reorderIcon = mode === 'ios' ? reorderThreeOutline : reorderTwoSharp;
        return (h(Host, { key: '5747b63aa64b05bfed96bbce8087186c7e14c6d5', class: mode }, h("slot", { key: 'a745f29a23c905cd0bff572acb755b597a3fb3c3' }, h("ion-icon", { key: '48f433e85a3a68c16bc426623b2b74957b4b2eb7', icon: reorderIcon, lazy: false, class: "reorder-icon", part: "icon", "aria-hidden": "true" }))));
    }
    get el() { return this; }
    static get style() { return {
        ios: IonReorderIosStyle0,
        md: IonReorderMdStyle0
    }; }
}, [33, "ion-reorder", undefined, [[2, "click", "onClick"]]]);
function defineCustomElement$1() {
    if (typeof customElements === "undefined") {
        return;
    }
    const components = ["ion-reorder", "ion-icon"];
    components.forEach(tagName => { switch (tagName) {
        case "ion-reorder":
            if (!customElements.get(tagName)) {
                customElements.define(tagName, Reorder);
            }
            break;
        case "ion-icon":
            if (!customElements.get(tagName)) {
                defineCustomElement$2();
            }
            break;
    } });
}

const IonReorder = Reorder;
const defineCustomElement = defineCustomElement$1;

export { IonReorder, defineCustomElement };
