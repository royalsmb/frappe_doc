/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { reorderThreeOutline, reorderTwoSharp } from "ionicons/icons";
import { getIonMode } from "../../global/ionic-global";
/**
 * @part icon - The icon of the reorder handle (uses ion-icon).
 */
export class Reorder {
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
    static get is() { return "ion-reorder"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "ios": ["reorder.ios.scss"],
            "md": ["reorder.md.scss"]
        };
    }
    static get styleUrls() {
        return {
            "ios": ["reorder.ios.css"],
            "md": ["reorder.md.css"]
        };
    }
    static get elementRef() { return "el"; }
    static get listeners() {
        return [{
                "name": "click",
                "method": "onClick",
                "target": undefined,
                "capture": true,
                "passive": false
            }];
    }
}
