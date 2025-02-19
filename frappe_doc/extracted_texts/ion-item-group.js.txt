/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { proxyCustomElement, HTMLElement, h, Host } from '@stencil/core/internal/client';
import { b as getIonMode } from './ionic-global.js';

const itemGroupIosCss = "ion-item-group{display:block}";
const IonItemGroupIosStyle0 = itemGroupIosCss;

const itemGroupMdCss = "ion-item-group{display:block}";
const IonItemGroupMdStyle0 = itemGroupMdCss;

const ItemGroup = /*@__PURE__*/ proxyCustomElement(class ItemGroup extends HTMLElement {
    constructor() {
        super();
        this.__registerHost();
    }
    render() {
        const mode = getIonMode(this);
        return (h(Host, { key: '5778fb7e9c6791874b4ff14f0babdae715e322e7', role: "group", class: {
                [mode]: true,
                // Used internally for styling
                [`item-group-${mode}`]: true,
                item: true,
            } }));
    }
    static get style() { return {
        ios: IonItemGroupIosStyle0,
        md: IonItemGroupMdStyle0
    }; }
}, [32, "ion-item-group"]);
function defineCustomElement$1() {
    if (typeof customElements === "undefined") {
        return;
    }
    const components = ["ion-item-group"];
    components.forEach(tagName => { switch (tagName) {
        case "ion-item-group":
            if (!customElements.get(tagName)) {
                customElements.define(tagName, ItemGroup);
            }
            break;
    } });
}

const IonItemGroup = ItemGroup;
const defineCustomElement = defineCustomElement$1;

export { IonItemGroup, defineCustomElement };
