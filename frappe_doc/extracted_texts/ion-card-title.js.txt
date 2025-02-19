/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { proxyCustomElement, HTMLElement, h, Host } from '@stencil/core/internal/client';
import { c as createColorClasses } from './theme.js';
import { b as getIonMode } from './ionic-global.js';

const cardTitleIosCss = ":host{display:block;position:relative;color:var(--color)}:host(.ion-color){color:var(--ion-color-base)}:host{--color:var(--ion-text-color, #000);margin-left:0;margin-right:0;margin-top:0;margin-bottom:0;padding-left:0;padding-right:0;padding-top:0;padding-bottom:0;font-size:1.75rem;font-weight:700;line-height:1.2}";
const IonCardTitleIosStyle0 = cardTitleIosCss;

const cardTitleMdCss = ":host{display:block;position:relative;color:var(--color)}:host(.ion-color){color:var(--ion-color-base)}:host{--color:var(--ion-color-step-850, #262626);margin-left:0;margin-right:0;margin-top:0;margin-bottom:0;padding-left:0;padding-right:0;padding-top:0;padding-bottom:0;font-size:1.25rem;font-weight:500;line-height:1.2}";
const IonCardTitleMdStyle0 = cardTitleMdCss;

const CardTitle = /*@__PURE__*/ proxyCustomElement(class CardTitle extends HTMLElement {
    constructor() {
        super();
        this.__registerHost();
        this.__attachShadow();
        this.color = undefined;
    }
    render() {
        const mode = getIonMode(this);
        return (h(Host, { key: 'a9e4190346e7d0a8e6089ec1fe01bca0f5f7200d', role: "heading", "aria-level": "2", class: createColorClasses(this.color, {
                'ion-inherit-color': true,
                [mode]: true,
            }) }, h("slot", { key: '8d87636ad703545b6d2297629205a5a8616eb94e' })));
    }
    static get style() { return {
        ios: IonCardTitleIosStyle0,
        md: IonCardTitleMdStyle0
    }; }
}, [33, "ion-card-title", {
        "color": [513]
    }]);
function defineCustomElement$1() {
    if (typeof customElements === "undefined") {
        return;
    }
    const components = ["ion-card-title"];
    components.forEach(tagName => { switch (tagName) {
        case "ion-card-title":
            if (!customElements.get(tagName)) {
                customElements.define(tagName, CardTitle);
            }
            break;
    } });
}

const IonCardTitle = CardTitle;
const defineCustomElement = defineCustomElement$1;

export { IonCardTitle, defineCustomElement };
