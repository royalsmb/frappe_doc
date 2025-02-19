/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { getIonMode } from "../../global/ionic-global";
export class Avatar {
    render() {
        return (h(Host, { key: 'f6014b524497bb18ae919ba6f6928407310d6870', class: getIonMode(this) }, h("slot", { key: '192ff4a8e10c0b0a4a2ed795ff2675afa8b23449' })));
    }
    static get is() { return "ion-avatar"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "ios": ["avatar.ios.scss"],
            "md": ["avatar.md.scss"]
        };
    }
    static get styleUrls() {
        return {
            "ios": ["avatar.ios.css"],
            "md": ["avatar.md.css"]
        };
    }
}
