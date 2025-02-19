/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-22617dd6.js');
const ionicGlobal = require('./ionic-global-c5503e93.js');
const theme = require('./theme-d1c573d2.js');

const avatarIosCss = ":host{border-radius:var(--border-radius);display:block}::slotted(ion-img),::slotted(img){border-radius:var(--border-radius);width:100%;height:100%;-o-object-fit:cover;object-fit:cover;overflow:hidden}:host{--border-radius:50%;width:48px;height:48px}";
const IonAvatarIosStyle0 = avatarIosCss;

const avatarMdCss = ":host{border-radius:var(--border-radius);display:block}::slotted(ion-img),::slotted(img){border-radius:var(--border-radius);width:100%;height:100%;-o-object-fit:cover;object-fit:cover;overflow:hidden}:host{--border-radius:50%;width:64px;height:64px}";
const IonAvatarMdStyle0 = avatarMdCss;

const Avatar = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
    }
    render() {
        return (index.h(index.Host, { key: 'f6014b524497bb18ae919ba6f6928407310d6870', class: ionicGlobal.getIonMode(this) }, index.h("slot", { key: '192ff4a8e10c0b0a4a2ed795ff2675afa8b23449' })));
    }
};
Avatar.style = {
    ios: IonAvatarIosStyle0,
    md: IonAvatarMdStyle0
};

const badgeIosCss = ":host{--background:var(--ion-color-primary, #3880ff);--color:var(--ion-color-primary-contrast, #fff);--padding-top:3px;--padding-end:8px;--padding-bottom:3px;--padding-start:8px;-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;-webkit-padding-start:var(--padding-start);padding-inline-start:var(--padding-start);-webkit-padding-end:var(--padding-end);padding-inline-end:var(--padding-end);padding-top:var(--padding-top);padding-bottom:var(--padding-bottom);display:inline-block;min-width:10px;background:var(--background);color:var(--color);font-family:var(--ion-font-family, inherit);font-size:0.8125rem;font-weight:bold;line-height:1;text-align:center;white-space:nowrap;contain:content;vertical-align:baseline}:host(.ion-color){background:var(--ion-color-base);color:var(--ion-color-contrast)}:host(:empty){display:none}:host{border-radius:10px;font-size:max(13px, 0.8125rem)}";
const IonBadgeIosStyle0 = badgeIosCss;

const badgeMdCss = ":host{--background:var(--ion-color-primary, #3880ff);--color:var(--ion-color-primary-contrast, #fff);--padding-top:3px;--padding-end:8px;--padding-bottom:3px;--padding-start:8px;-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;-webkit-padding-start:var(--padding-start);padding-inline-start:var(--padding-start);-webkit-padding-end:var(--padding-end);padding-inline-end:var(--padding-end);padding-top:var(--padding-top);padding-bottom:var(--padding-bottom);display:inline-block;min-width:10px;background:var(--background);color:var(--color);font-family:var(--ion-font-family, inherit);font-size:0.8125rem;font-weight:bold;line-height:1;text-align:center;white-space:nowrap;contain:content;vertical-align:baseline}:host(.ion-color){background:var(--ion-color-base);color:var(--ion-color-contrast)}:host(:empty){display:none}:host{--padding-top:3px;--padding-end:4px;--padding-bottom:4px;--padding-start:4px;border-radius:4px}";
const IonBadgeMdStyle0 = badgeMdCss;

const Badge = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
        this.color = undefined;
    }
    render() {
        const mode = ionicGlobal.getIonMode(this);
        return (index.h(index.Host, { key: '22d41ceefb76f40dfbf739fd71483f1272a45858', class: theme.createColorClasses(this.color, {
                [mode]: true,
            }) }, index.h("slot", { key: 'e7e65463bac5903971a8f9f6be55515f42b81a83' })));
    }
};
Badge.style = {
    ios: IonBadgeIosStyle0,
    md: IonBadgeMdStyle0
};

const thumbnailCss = ":host{--size:48px;--border-radius:0;border-radius:var(--border-radius);display:block;width:var(--size);height:var(--size)}::slotted(ion-img),::slotted(img){border-radius:var(--border-radius);width:100%;height:100%;-o-object-fit:cover;object-fit:cover;overflow:hidden}";
const IonThumbnailStyle0 = thumbnailCss;

const Thumbnail = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
    }
    render() {
        return (index.h(index.Host, { key: 'd2667635930e4c0896805f452357e7dc9086bc72', class: ionicGlobal.getIonMode(this) }, index.h("slot", { key: '66eb1487f3da4da2ef71b812a8d0f0fe884c7d81' })));
    }
};
Thumbnail.style = IonThumbnailStyle0;

exports.ion_avatar = Avatar;
exports.ion_badge = Badge;
exports.ion_thumbnail = Thumbnail;
