/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { getIonMode } from "../../global/ionic-global";
export class Row {
    render() {
        return (h(Host, { key: '242c9a45b0bb39af2aebf412fdfa9a176babc834', class: getIonMode(this) }, h("slot", { key: 'd9015d663d631bbf20bd3e0821fed874cd6c5156' })));
    }
    static get is() { return "ion-row"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "$": ["row.scss"]
        };
    }
    static get styleUrls() {
        return {
            "$": ["row.css"]
        };
    }
}
