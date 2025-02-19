/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import { Host, h } from "@stencil/core";
import { ENABLE_HTML_CONTENT_DEFAULT } from "../../utils/config";
import { sanitizeDOMString } from "../../utils/sanitization/index";
import { arrowDown, caretBackSharp } from "ionicons/icons";
import { config } from "../../global/config";
import { getIonMode } from "../../global/ionic-global";
import { supportsRubberBandScrolling } from "../refresher/refresher.utils";
import { SPINNERS } from "../spinner/spinner-configs";
export class RefresherContent {
    constructor() {
        this.customHTMLEnabled = config.get('innerHTMLTemplatesEnabled', ENABLE_HTML_CONTENT_DEFAULT);
        this.pullingIcon = undefined;
        this.pullingText = undefined;
        this.refreshingSpinner = undefined;
        this.refreshingText = undefined;
    }
    componentWillLoad() {
        if (this.pullingIcon === undefined) {
            /**
             * The native iOS refresher uses a spinner instead of
             * an icon, so we need to see if this device supports
             * the native iOS refresher.
             */
            const hasRubberBandScrolling = supportsRubberBandScrolling();
            const mode = getIonMode(this);
            const overflowRefresher = hasRubberBandScrolling ? 'lines' : arrowDown;
            this.pullingIcon = config.get('refreshingIcon', mode === 'ios' && hasRubberBandScrolling ? config.get('spinner', overflowRefresher) : 'circular');
        }
        if (this.refreshingSpinner === undefined) {
            const mode = getIonMode(this);
            this.refreshingSpinner = config.get('refreshingSpinner', config.get('spinner', mode === 'ios' ? 'lines' : 'circular'));
        }
    }
    renderPullingText() {
        const { customHTMLEnabled, pullingText } = this;
        if (customHTMLEnabled) {
            return h("div", { class: "refresher-pulling-text", innerHTML: sanitizeDOMString(pullingText) });
        }
        return h("div", { class: "refresher-pulling-text" }, pullingText);
    }
    renderRefreshingText() {
        const { customHTMLEnabled, refreshingText } = this;
        if (customHTMLEnabled) {
            return h("div", { class: "refresher-refreshing-text", innerHTML: sanitizeDOMString(refreshingText) });
        }
        return h("div", { class: "refresher-refreshing-text" }, refreshingText);
    }
    render() {
        const pullingIcon = this.pullingIcon;
        const hasSpinner = pullingIcon != null && SPINNERS[pullingIcon] !== undefined;
        const mode = getIonMode(this);
        return (h(Host, { key: 'cf3caa51c4aba8a95622f6d32cafa90b683b9d6e', class: mode }, h("div", { key: '5ad70801104bbea873d3525206660c52e4447903', class: "refresher-pulling" }, this.pullingIcon && hasSpinner && (h("div", { key: '0f95df169fd367528bfaa5d9ccf6690a613609c4', class: "refresher-pulling-icon" }, h("div", { key: '4b8f0465a19f017751b207807c32e1fe00fda433', class: "spinner-arrow-container" }, h("ion-spinner", { key: '77e60179d76f0d17f8f2dc3518f97a2a924418e6', name: this.pullingIcon, paused: true }), mode === 'md' && this.pullingIcon === 'circular' && (h("div", { key: 'f78f63f08f071bead1bfe655bae6394f8a219d91', class: "arrow-container" }, h("ion-icon", { key: '4d833d134d2b221cae2dfb0611d4029f2d664db5', icon: caretBackSharp, "aria-hidden": "true" })))))), this.pullingIcon && !hasSpinner && (h("div", { key: 'e6db19d7fa324363d2a7c3c046510f4c8461f7e6', class: "refresher-pulling-icon" }, h("ion-icon", { key: '66c2ef1a53c5809f49891de515da5f55d9bf8dcc', icon: this.pullingIcon, lazy: false, "aria-hidden": "true" }))), this.pullingText !== undefined && this.renderPullingText()), h("div", { key: '80c413e21d362a5bb0419fcd13092453b3445cee', class: "refresher-refreshing" }, this.refreshingSpinner && (h("div", { key: '0d5511f9644de26332a1a9ed39b160691fab74d9', class: "refresher-refreshing-icon" }, h("ion-spinner", { key: '54e4a96b081c7b453a98e00cceea7c086268a450', name: this.refreshingSpinner }))), this.refreshingText !== undefined && this.renderRefreshingText())));
    }
    static get is() { return "ion-refresher-content"; }
    static get properties() {
        return {
            "pullingIcon": {
                "type": "string",
                "mutable": true,
                "complexType": {
                    "original": "SpinnerTypes | string | null",
                    "resolved": "null | string | undefined",
                    "references": {
                        "SpinnerTypes": {
                            "location": "import",
                            "path": "../spinner/spinner-configs",
                            "id": "src/components/spinner/spinner-configs.ts::SpinnerTypes"
                        }
                    }
                },
                "required": false,
                "optional": true,
                "docs": {
                    "tags": [],
                    "text": "A static icon or a spinner to display when you begin to pull down.\nA spinner name can be provided to gradually show tick marks\nwhen pulling down on iOS devices."
                },
                "attribute": "pulling-icon",
                "reflect": false
            },
            "pullingText": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string | IonicSafeString",
                    "resolved": "IonicSafeString | string | undefined",
                    "references": {
                        "IonicSafeString": {
                            "location": "import",
                            "path": "../../utils/sanitization",
                            "id": "src/utils/sanitization/index.ts::IonicSafeString"
                        }
                    }
                },
                "required": false,
                "optional": true,
                "docs": {
                    "tags": [],
                    "text": "The text you want to display when you begin to pull down.\n`pullingText` can accept either plaintext or HTML as a string.\nTo display characters normally reserved for HTML, they\nmust be escaped. For example `<Ionic>` would become\n`&lt;Ionic&gt;`\n\nFor more information: [Security Documentation](https://ionicframework.com/docs/faq/security)\n\nContent is parsed as plaintext by default.\n`innerHTMLTemplatesEnabled` must be set to `true` in the Ionic config\nbefore custom HTML can be used."
                },
                "attribute": "pulling-text",
                "reflect": false
            },
            "refreshingSpinner": {
                "type": "string",
                "mutable": true,
                "complexType": {
                    "original": "SpinnerTypes | null",
                    "resolved": "\"bubbles\" | \"circles\" | \"circular\" | \"crescent\" | \"dots\" | \"lines\" | \"lines-sharp\" | \"lines-sharp-small\" | \"lines-small\" | null | undefined",
                    "references": {
                        "SpinnerTypes": {
                            "location": "import",
                            "path": "../spinner/spinner-configs",
                            "id": "src/components/spinner/spinner-configs.ts::SpinnerTypes"
                        }
                    }
                },
                "required": false,
                "optional": true,
                "docs": {
                    "tags": [],
                    "text": "An animated SVG spinner that shows when refreshing begins"
                },
                "attribute": "refreshing-spinner",
                "reflect": false
            },
            "refreshingText": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string | IonicSafeString",
                    "resolved": "IonicSafeString | string | undefined",
                    "references": {
                        "IonicSafeString": {
                            "location": "import",
                            "path": "../../utils/sanitization",
                            "id": "src/utils/sanitization/index.ts::IonicSafeString"
                        }
                    }
                },
                "required": false,
                "optional": true,
                "docs": {
                    "tags": [],
                    "text": "The text you want to display when performing a refresh.\n`refreshingText` can accept either plaintext or HTML as a string.\nTo display characters normally reserved for HTML, they\nmust be escaped. For example `<Ionic>` would become\n`&lt;Ionic&gt;`\n\nFor more information: [Security Documentation](https://ionicframework.com/docs/faq/security)\n\nContent is parsed as plaintext by default.\n`innerHTMLTemplatesEnabled` must be set to `true` in the Ionic config\nbefore custom HTML can be used."
                },
                "attribute": "refreshing-text",
                "reflect": false
            }
        };
    }
    static get elementRef() { return "el"; }
}
