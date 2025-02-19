/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { createColorClasses } from "../../utils/theme";
import { getIonMode } from "../../global/ionic-global";
/**
 * @virtualProp {"ios" | "md"} mode - The mode determines which platform styles to use.
 *
 * @slot - Content is placed between the named slots if provided without a slot.
 * @slot start - Content is placed to the left of the divider text in LTR, and to the right in RTL.
 * @slot end - Content is placed to the right of the divider text in LTR, and to the left in RTL.
 */
export class ItemDivider {
    constructor() {
        this.color = undefined;
        this.sticky = false;
    }
    render() {
        const mode = getIonMode(this);
        return (h(Host, { key: '5727179159ef2a8879f55435265003e0ec72df3f', class: createColorClasses(this.color, {
                [mode]: true,
                'item-divider-sticky': this.sticky,
                item: true,
            }) }, h("slot", { key: 'bb7df137e60ca3fa9a50c612e30fbb3ee4c818ad', name: "start" }), h("div", { key: '6a25a01271957cfdd8e8dfb6ef76e1eb710380f2', class: "item-divider-inner" }, h("div", { key: '554ba681b0f346ed0af03232f8b2e6ca399877d9', class: "item-divider-wrapper" }, h("slot", { key: 'f98e20a01f09d0a2e19b7351eb1b4028881a07ab' })), h("slot", { key: '755643b5b8d3463af41b3d0805871073a34386a3', name: "end" }))));
    }
    static get is() { return "ion-item-divider"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "ios": ["item-divider.ios.scss"],
            "md": ["item-divider.md.scss"]
        };
    }
    static get styleUrls() {
        return {
            "ios": ["item-divider.ios.css"],
            "md": ["item-divider.md.css"]
        };
    }
    static get properties() {
        return {
            "color": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "Color",
                    "resolved": "\"danger\" | \"dark\" | \"light\" | \"medium\" | \"primary\" | \"secondary\" | \"success\" | \"tertiary\" | \"warning\" | string & Record<never, never> | undefined",
                    "references": {
                        "Color": {
                            "location": "import",
                            "path": "../../interface",
                            "id": "src/interface.d.ts::Color"
                        }
                    }
                },
                "required": false,
                "optional": true,
                "docs": {
                    "tags": [],
                    "text": "The color to use from your application's color palette.\nDefault options are: `\"primary\"`, `\"secondary\"`, `\"tertiary\"`, `\"success\"`, `\"warning\"`, `\"danger\"`, `\"light\"`, `\"medium\"`, and `\"dark\"`.\nFor more information on colors, see [theming](/docs/theming/basics)."
                },
                "attribute": "color",
                "reflect": true
            },
            "sticky": {
                "type": "boolean",
                "mutable": false,
                "complexType": {
                    "original": "boolean",
                    "resolved": "boolean",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": "When it's set to `true`, the item-divider will stay visible when it reaches the top\nof the viewport until the next `ion-item-divider` replaces it.\n\nThis feature relies in `position:sticky`:\nhttps://caniuse.com/#feat=css-sticky"
                },
                "attribute": "sticky",
                "reflect": false,
                "defaultValue": "false"
            }
        };
    }
    static get elementRef() { return "el"; }
}
