/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-22617dd6.js');
const theme = require('./theme-d1c573d2.js');
const ionicGlobal = require('./ionic-global-c5503e93.js');

const textCss = ":host(.ion-color){color:var(--ion-color-base)}";
const IonTextStyle0 = textCss;

const Text = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
        this.color = undefined;
    }
    render() {
        const mode = ionicGlobal.getIonMode(this);
        return (index.h(index.Host, { key: '4330b56cbc4e15953d9b3162fb40af728a8195dd', class: theme.createColorClasses(this.color, {
                [mode]: true,
            }) }, index.h("slot", { key: 'ec674a71d8fbb04d537fd79d617d9db4a607c340' })));
    }
};
Text.style = IonTextStyle0;

exports.ion_text = Text;
