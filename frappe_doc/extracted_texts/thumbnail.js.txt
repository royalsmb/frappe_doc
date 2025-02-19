/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { getIonMode } from "../../global/ionic-global";
export class Thumbnail {
    render() {
        return (h(Host, { key: 'd2667635930e4c0896805f452357e7dc9086bc72', class: getIonMode(this) }, h("slot", { key: '66eb1487f3da4da2ef71b812a8d0f0fe884c7d81' })));
    }
    static get is() { return "ion-thumbnail"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "$": ["thumbnail.scss"]
        };
    }
    static get styleUrls() {
        return {
            "$": ["thumbnail.css"]
        };
    }
}
