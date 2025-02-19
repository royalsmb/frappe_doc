/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-22617dd6.js');
const gestureController = require('./gesture-controller-c40c045a.js');
const ionicGlobal = require('./ionic-global-c5503e93.js');

const backdropIosCss = ":host{left:0;right:0;top:0;bottom:0;display:block;position:absolute;-webkit-transform:translateZ(0);transform:translateZ(0);contain:strict;cursor:pointer;opacity:0.01;-ms-touch-action:none;touch-action:none;z-index:2}:host(.backdrop-hide){background:transparent}:host(.backdrop-no-tappable){cursor:auto}:host{background-color:var(--ion-backdrop-color, #000)}";
const IonBackdropIosStyle0 = backdropIosCss;

const backdropMdCss = ":host{left:0;right:0;top:0;bottom:0;display:block;position:absolute;-webkit-transform:translateZ(0);transform:translateZ(0);contain:strict;cursor:pointer;opacity:0.01;-ms-touch-action:none;touch-action:none;z-index:2}:host(.backdrop-hide){background:transparent}:host(.backdrop-no-tappable){cursor:auto}:host{background-color:var(--ion-backdrop-color, #000)}";
const IonBackdropMdStyle0 = backdropMdCss;

const Backdrop = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
        this.ionBackdropTap = index.createEvent(this, "ionBackdropTap", 7);
        this.blocker = gestureController.GESTURE_CONTROLLER.createBlocker({
            disableScroll: true,
        });
        this.visible = true;
        this.tappable = true;
        this.stopPropagation = true;
    }
    connectedCallback() {
        if (this.stopPropagation) {
            this.blocker.block();
        }
    }
    disconnectedCallback() {
        this.blocker.unblock();
    }
    onMouseDown(ev) {
        this.emitTap(ev);
    }
    emitTap(ev) {
        if (this.stopPropagation) {
            ev.preventDefault();
            ev.stopPropagation();
        }
        if (this.tappable) {
            this.ionBackdropTap.emit();
        }
    }
    render() {
        const mode = ionicGlobal.getIonMode(this);
        return (index.h(index.Host, { key: '16b1328f4a058b8d3752e58dc56c44bed556c425', tabindex: "-1", "aria-hidden": "true", class: {
                [mode]: true,
                'backdrop-hide': !this.visible,
                'backdrop-no-tappable': !this.tappable,
            } }));
    }
};
Backdrop.style = {
    ios: IonBackdropIosStyle0,
    md: IonBackdropMdStyle0
};

exports.ion_backdrop = Backdrop;
