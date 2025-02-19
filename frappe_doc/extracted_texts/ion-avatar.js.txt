/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { proxyCustomElement, HTMLElement, h, Host } from '@stencil/core/internal/client';
import { b as getIonMode } from './ionic-global.js';

const avatarIosCss = ":host{border-radius:var(--border-radius);display:block}::slotted(ion-img),::slotted(img){border-radius:var(--border-radius);width:100%;height:100%;-o-object-fit:cover;object-fit:cover;overflow:hidden}:host{--border-radius:50%;width:48px;height:48px}";
const IonAvatarIosStyle0 = avatarIosCss;

const avatarMdCss = ":host{border-radius:var(--border-radius);display:block}::slotted(ion-img),::slotted(img){border-radius:var(--border-radius);width:100%;height:100%;-o-object-fit:cover;object-fit:cover;overflow:hidden}:host{--border-radius:50%;width:64px;height:64px}";
const IonAvatarMdStyle0 = avatarMdCss;

const Avatar = /*@__PURE__*/ proxyCustomElement(class Avatar extends HTMLElement {
    constructor() {
        super();
        this.__registerHost();
        this.__attachShadow();
    }
    render() {
        return (h(Host, { key: 'f6014b524497bb18ae919ba6f6928407310d6870', class: getIonMode(this) }, h("slot", { key: '192ff4a8e10c0b0a4a2ed795ff2675afa8b23449' })));
    }
    static get style() { return {
        ios: IonAvatarIosStyle0,
        md: IonAvatarMdStyle0
    }; }
}, [33, "ion-avatar"]);
function defineCustomElement$1() {
    if (typeof customElements === "undefined") {
        return;
    }
    const components = ["ion-avatar"];
    components.forEach(tagName => { switch (tagName) {
        case "ion-avatar":
            if (!customElements.get(tagName)) {
                customElements.define(tagName, Avatar);
            }
            break;
    } });
}

const IonAvatar = Avatar;
const defineCustomElement = defineCustomElement$1;

export { IonAvatar, defineCustomElement };
