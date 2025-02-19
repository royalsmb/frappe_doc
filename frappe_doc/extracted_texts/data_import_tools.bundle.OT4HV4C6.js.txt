(() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __commonJS = (cb, mod) => function __require() {
    return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));

  // node_modules/sortablejs/Sortable.min.js
  var require_Sortable_min = __commonJS({
    "node_modules/sortablejs/Sortable.min.js"(exports, module) {
      !function(t, e) {
        "object" == typeof exports && "undefined" != typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define(e) : (t = t || self).Sortable = e();
      }(exports, function() {
        "use strict";
        function e(e2, t2) {
          var n2, o2 = Object.keys(e2);
          return Object.getOwnPropertySymbols && (n2 = Object.getOwnPropertySymbols(e2), t2 && (n2 = n2.filter(function(t3) {
            return Object.getOwnPropertyDescriptor(e2, t3).enumerable;
          })), o2.push.apply(o2, n2)), o2;
        }
        function M(o2) {
          for (var t2 = 1; t2 < arguments.length; t2++) {
            var i2 = null != arguments[t2] ? arguments[t2] : {};
            t2 % 2 ? e(Object(i2), true).forEach(function(t3) {
              var e2, n2;
              e2 = o2, t3 = i2[n2 = t3], n2 in e2 ? Object.defineProperty(e2, n2, { value: t3, enumerable: true, configurable: true, writable: true }) : e2[n2] = t3;
            }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(o2, Object.getOwnPropertyDescriptors(i2)) : e(Object(i2)).forEach(function(t3) {
              Object.defineProperty(o2, t3, Object.getOwnPropertyDescriptor(i2, t3));
            });
          }
          return o2;
        }
        function o(t2) {
          return (o = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(t3) {
            return typeof t3;
          } : function(t3) {
            return t3 && "function" == typeof Symbol && t3.constructor === Symbol && t3 !== Symbol.prototype ? "symbol" : typeof t3;
          })(t2);
        }
        function a() {
          return (a = Object.assign || function(t2) {
            for (var e2 = 1; e2 < arguments.length; e2++) {
              var n2, o2 = arguments[e2];
              for (n2 in o2)
                Object.prototype.hasOwnProperty.call(o2, n2) && (t2[n2] = o2[n2]);
            }
            return t2;
          }).apply(this, arguments);
        }
        function i(t2, e2) {
          if (null == t2)
            return {};
          var n2, o2 = function(t3, e3) {
            if (null == t3)
              return {};
            for (var n3, o3 = {}, i3 = Object.keys(t3), r3 = 0; r3 < i3.length; r3++)
              n3 = i3[r3], 0 <= e3.indexOf(n3) || (o3[n3] = t3[n3]);
            return o3;
          }(t2, e2);
          if (Object.getOwnPropertySymbols)
            for (var i2 = Object.getOwnPropertySymbols(t2), r2 = 0; r2 < i2.length; r2++)
              n2 = i2[r2], 0 <= e2.indexOf(n2) || Object.prototype.propertyIsEnumerable.call(t2, n2) && (o2[n2] = t2[n2]);
          return o2;
        }
        function r(t2) {
          return function(t3) {
            if (Array.isArray(t3))
              return l(t3);
          }(t2) || function(t3) {
            if ("undefined" != typeof Symbol && null != t3[Symbol.iterator] || null != t3["@@iterator"])
              return Array.from(t3);
          }(t2) || function(t3, e2) {
            if (t3) {
              if ("string" == typeof t3)
                return l(t3, e2);
              var n2 = Object.prototype.toString.call(t3).slice(8, -1);
              return "Map" === (n2 = "Object" === n2 && t3.constructor ? t3.constructor.name : n2) || "Set" === n2 ? Array.from(t3) : "Arguments" === n2 || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n2) ? l(t3, e2) : void 0;
            }
          }(t2) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
          }();
        }
        function l(t2, e2) {
          (null == e2 || e2 > t2.length) && (e2 = t2.length);
          for (var n2 = 0, o2 = new Array(e2); n2 < e2; n2++)
            o2[n2] = t2[n2];
          return o2;
        }
        function t(t2) {
          if ("undefined" != typeof window && window.navigator)
            return !!navigator.userAgent.match(t2);
        }
        var y = t(/(?:Trident.*rv[ :]?11\.|msie|iemobile|Windows Phone)/i), w = t(/Edge/i), s = t(/firefox/i), u = t(/safari/i) && !t(/chrome/i) && !t(/android/i), n = t(/iP(ad|od|hone)/i), c = t(/chrome/i) && t(/android/i), d = { capture: false, passive: false };
        function h(t2, e2, n2) {
          t2.addEventListener(e2, n2, !y && d);
        }
        function f(t2, e2, n2) {
          t2.removeEventListener(e2, n2, !y && d);
        }
        function p(t2, e2) {
          if (e2 && (">" === e2[0] && (e2 = e2.substring(1)), t2))
            try {
              if (t2.matches)
                return t2.matches(e2);
              if (t2.msMatchesSelector)
                return t2.msMatchesSelector(e2);
              if (t2.webkitMatchesSelector)
                return t2.webkitMatchesSelector(e2);
            } catch (t3) {
              return;
            }
        }
        function N(t2, e2, n2, o2) {
          if (t2) {
            n2 = n2 || document;
            do {
              if (null != e2 && (">" !== e2[0] || t2.parentNode === n2) && p(t2, e2) || o2 && t2 === n2)
                return t2;
            } while (t2 !== n2 && (t2 = (i2 = t2).host && i2 !== document && i2.host.nodeType ? i2.host : i2.parentNode));
          }
          var i2;
          return null;
        }
        var g, m = /\s+/g;
        function I(t2, e2, n2) {
          var o2;
          t2 && e2 && (t2.classList ? t2.classList[n2 ? "add" : "remove"](e2) : (o2 = (" " + t2.className + " ").replace(m, " ").replace(" " + e2 + " ", " "), t2.className = (o2 + (n2 ? " " + e2 : "")).replace(m, " ")));
        }
        function P(t2, e2, n2) {
          var o2 = t2 && t2.style;
          if (o2) {
            if (void 0 === n2)
              return document.defaultView && document.defaultView.getComputedStyle ? n2 = document.defaultView.getComputedStyle(t2, "") : t2.currentStyle && (n2 = t2.currentStyle), void 0 === e2 ? n2 : n2[e2];
            o2[e2 = !(e2 in o2 || -1 !== e2.indexOf("webkit")) ? "-webkit-" + e2 : e2] = n2 + ("string" == typeof n2 ? "" : "px");
          }
        }
        function v(t2, e2) {
          var n2 = "";
          if ("string" == typeof t2)
            n2 = t2;
          else
            do {
              var o2 = P(t2, "transform");
            } while (o2 && "none" !== o2 && (n2 = o2 + " " + n2), !e2 && (t2 = t2.parentNode));
          var i2 = window.DOMMatrix || window.WebKitCSSMatrix || window.CSSMatrix || window.MSCSSMatrix;
          return i2 && new i2(n2);
        }
        function b(t2, e2, n2) {
          if (t2) {
            var o2 = t2.getElementsByTagName(e2), i2 = 0, r2 = o2.length;
            if (n2)
              for (; i2 < r2; i2++)
                n2(o2[i2], i2);
            return o2;
          }
          return [];
        }
        function O() {
          var t2 = document.scrollingElement;
          return t2 || document.documentElement;
        }
        function k(t2, e2, n2, o2, i2) {
          if (t2.getBoundingClientRect || t2 === window) {
            var r2, a2, l2, s2, c2, u2, d2 = t2 !== window && t2.parentNode && t2 !== O() ? (a2 = (r2 = t2.getBoundingClientRect()).top, l2 = r2.left, s2 = r2.bottom, c2 = r2.right, u2 = r2.height, r2.width) : (l2 = a2 = 0, s2 = window.innerHeight, c2 = window.innerWidth, u2 = window.innerHeight, window.innerWidth);
            if ((e2 || n2) && t2 !== window && (i2 = i2 || t2.parentNode, !y))
              do {
                if (i2 && i2.getBoundingClientRect && ("none" !== P(i2, "transform") || n2 && "static" !== P(i2, "position"))) {
                  var h2 = i2.getBoundingClientRect();
                  a2 -= h2.top + parseInt(P(i2, "border-top-width")), l2 -= h2.left + parseInt(P(i2, "border-left-width")), s2 = a2 + r2.height, c2 = l2 + r2.width;
                  break;
                }
              } while (i2 = i2.parentNode);
            return o2 && t2 !== window && (o2 = (e2 = v(i2 || t2)) && e2.a, t2 = e2 && e2.d, e2 && (s2 = (a2 /= t2) + (u2 /= t2), c2 = (l2 /= o2) + (d2 /= o2))), { top: a2, left: l2, bottom: s2, right: c2, width: d2, height: u2 };
          }
        }
        function R(t2, e2, n2) {
          for (var o2 = A(t2, true), i2 = k(t2)[e2]; o2; ) {
            var r2 = k(o2)[n2];
            if (!("top" === n2 || "left" === n2 ? r2 <= i2 : i2 <= r2))
              return o2;
            if (o2 === O())
              break;
            o2 = A(o2, false);
          }
          return false;
        }
        function X(t2, e2, n2, o2) {
          for (var i2 = 0, r2 = 0, a2 = t2.children; r2 < a2.length; ) {
            if ("none" !== a2[r2].style.display && a2[r2] !== Bt.ghost && (o2 || a2[r2] !== Bt.dragged) && N(a2[r2], n2.draggable, t2, false)) {
              if (i2 === e2)
                return a2[r2];
              i2++;
            }
            r2++;
          }
          return null;
        }
        function Y(t2, e2) {
          for (var n2 = t2.lastElementChild; n2 && (n2 === Bt.ghost || "none" === P(n2, "display") || e2 && !p(n2, e2)); )
            n2 = n2.previousElementSibling;
          return n2 || null;
        }
        function B(t2, e2) {
          var n2 = 0;
          if (!t2 || !t2.parentNode)
            return -1;
          for (; t2 = t2.previousElementSibling; )
            "TEMPLATE" === t2.nodeName.toUpperCase() || t2 === Bt.clone || e2 && !p(t2, e2) || n2++;
          return n2;
        }
        function E(t2) {
          var e2 = 0, n2 = 0, o2 = O();
          if (t2)
            do {
              var i2 = v(t2), r2 = i2.a, i2 = i2.d;
            } while (e2 += t2.scrollLeft * r2, n2 += t2.scrollTop * i2, t2 !== o2 && (t2 = t2.parentNode));
          return [e2, n2];
        }
        function A(t2, e2) {
          if (!t2 || !t2.getBoundingClientRect)
            return O();
          var n2 = t2, o2 = false;
          do {
            if (n2.clientWidth < n2.scrollWidth || n2.clientHeight < n2.scrollHeight) {
              var i2 = P(n2);
              if (n2.clientWidth < n2.scrollWidth && ("auto" == i2.overflowX || "scroll" == i2.overflowX) || n2.clientHeight < n2.scrollHeight && ("auto" == i2.overflowY || "scroll" == i2.overflowY)) {
                if (!n2.getBoundingClientRect || n2 === document.body)
                  return O();
                if (o2 || e2)
                  return n2;
                o2 = true;
              }
            }
          } while (n2 = n2.parentNode);
          return O();
        }
        function D(t2, e2) {
          return Math.round(t2.top) === Math.round(e2.top) && Math.round(t2.left) === Math.round(e2.left) && Math.round(t2.height) === Math.round(e2.height) && Math.round(t2.width) === Math.round(e2.width);
        }
        function S(e2, n2) {
          return function() {
            var t2;
            g || (1 === (t2 = arguments).length ? e2.call(this, t2[0]) : e2.apply(this, t2), g = setTimeout(function() {
              g = void 0;
            }, n2));
          };
        }
        function F(t2, e2, n2) {
          t2.scrollLeft += e2, t2.scrollTop += n2;
        }
        function _(t2) {
          var e2 = window.Polymer, n2 = window.jQuery || window.Zepto;
          return e2 && e2.dom ? e2.dom(t2).cloneNode(true) : n2 ? n2(t2).clone(true)[0] : t2.cloneNode(true);
        }
        function C(t2, e2) {
          P(t2, "position", "absolute"), P(t2, "top", e2.top), P(t2, "left", e2.left), P(t2, "width", e2.width), P(t2, "height", e2.height);
        }
        function T(t2) {
          P(t2, "position", ""), P(t2, "top", ""), P(t2, "left", ""), P(t2, "width", ""), P(t2, "height", "");
        }
        var j = "Sortable" + new Date().getTime();
        function x() {
          var e2, o2 = [];
          return { captureAnimationState: function() {
            o2 = [], this.options.animation && [].slice.call(this.el.children).forEach(function(t2) {
              var e3, n2;
              "none" !== P(t2, "display") && t2 !== Bt.ghost && (o2.push({ target: t2, rect: k(t2) }), e3 = M({}, o2[o2.length - 1].rect), !t2.thisAnimationDuration || (n2 = v(t2, true)) && (e3.top -= n2.f, e3.left -= n2.e), t2.fromRect = e3);
            });
          }, addAnimationState: function(t2) {
            o2.push(t2);
          }, removeAnimationState: function(t2) {
            o2.splice(function(t3, e3) {
              for (var n2 in t3)
                if (t3.hasOwnProperty(n2)) {
                  for (var o3 in e3)
                    if (e3.hasOwnProperty(o3) && e3[o3] === t3[n2][o3])
                      return Number(n2);
                }
              return -1;
            }(o2, { target: t2 }), 1);
          }, animateAll: function(t2) {
            var c2 = this;
            if (!this.options.animation)
              return clearTimeout(e2), void ("function" == typeof t2 && t2());
            var u2 = false, d2 = 0;
            o2.forEach(function(t3) {
              var e3 = 0, n2 = t3.target, o3 = n2.fromRect, i2 = k(n2), r2 = n2.prevFromRect, a2 = n2.prevToRect, l2 = t3.rect, s2 = v(n2, true);
              s2 && (i2.top -= s2.f, i2.left -= s2.e), n2.toRect = i2, n2.thisAnimationDuration && D(r2, i2) && !D(o3, i2) && (l2.top - i2.top) / (l2.left - i2.left) == (o3.top - i2.top) / (o3.left - i2.left) && (t3 = l2, s2 = r2, r2 = a2, a2 = c2.options, e3 = Math.sqrt(Math.pow(s2.top - t3.top, 2) + Math.pow(s2.left - t3.left, 2)) / Math.sqrt(Math.pow(s2.top - r2.top, 2) + Math.pow(s2.left - r2.left, 2)) * a2.animation), D(i2, o3) || (n2.prevFromRect = o3, n2.prevToRect = i2, e3 = e3 || c2.options.animation, c2.animate(n2, l2, i2, e3)), e3 && (u2 = true, d2 = Math.max(d2, e3), clearTimeout(n2.animationResetTimer), n2.animationResetTimer = setTimeout(function() {
                n2.animationTime = 0, n2.prevFromRect = null, n2.fromRect = null, n2.prevToRect = null, n2.thisAnimationDuration = null;
              }, e3), n2.thisAnimationDuration = e3);
            }), clearTimeout(e2), u2 ? e2 = setTimeout(function() {
              "function" == typeof t2 && t2();
            }, d2) : "function" == typeof t2 && t2(), o2 = [];
          }, animate: function(t2, e3, n2, o3) {
            var i2, r2;
            o3 && (P(t2, "transition", ""), P(t2, "transform", ""), i2 = (r2 = v(this.el)) && r2.a, r2 = r2 && r2.d, i2 = (e3.left - n2.left) / (i2 || 1), r2 = (e3.top - n2.top) / (r2 || 1), t2.animatingX = !!i2, t2.animatingY = !!r2, P(t2, "transform", "translate3d(" + i2 + "px," + r2 + "px,0)"), this.forRepaintDummy = t2.offsetWidth, P(t2, "transition", "transform " + o3 + "ms" + (this.options.easing ? " " + this.options.easing : "")), P(t2, "transform", "translate3d(0,0,0)"), "number" == typeof t2.animated && clearTimeout(t2.animated), t2.animated = setTimeout(function() {
              P(t2, "transition", ""), P(t2, "transform", ""), t2.animated = false, t2.animatingX = false, t2.animatingY = false;
            }, o3));
          } };
        }
        var H = [], L = { initializeByDefault: true }, K = { mount: function(e2) {
          for (var t2 in L)
            !L.hasOwnProperty(t2) || t2 in e2 || (e2[t2] = L[t2]);
          H.forEach(function(t3) {
            if (t3.pluginName === e2.pluginName)
              throw "Sortable: Cannot mount plugin ".concat(e2.pluginName, " more than once");
          }), H.push(e2);
        }, pluginEvent: function(e2, n2, o2) {
          var t2 = this;
          this.eventCanceled = false, o2.cancel = function() {
            t2.eventCanceled = true;
          };
          var i2 = e2 + "Global";
          H.forEach(function(t3) {
            n2[t3.pluginName] && (n2[t3.pluginName][i2] && n2[t3.pluginName][i2](M({ sortable: n2 }, o2)), n2.options[t3.pluginName] && n2[t3.pluginName][e2] && n2[t3.pluginName][e2](M({ sortable: n2 }, o2)));
          });
        }, initializePlugins: function(n2, o2, i2, t2) {
          for (var e2 in H.forEach(function(t3) {
            var e3 = t3.pluginName;
            (n2.options[e3] || t3.initializeByDefault) && ((t3 = new t3(n2, o2, n2.options)).sortable = n2, t3.options = n2.options, n2[e3] = t3, a(i2, t3.defaults));
          }), n2.options) {
            var r2;
            n2.options.hasOwnProperty(e2) && (void 0 !== (r2 = this.modifyOption(n2, e2, n2.options[e2])) && (n2.options[e2] = r2));
          }
        }, getEventProperties: function(e2, n2) {
          var o2 = {};
          return H.forEach(function(t2) {
            "function" == typeof t2.eventProperties && a(o2, t2.eventProperties.call(n2[t2.pluginName], e2));
          }), o2;
        }, modifyOption: function(e2, n2, o2) {
          var i2;
          return H.forEach(function(t2) {
            e2[t2.pluginName] && t2.optionListeners && "function" == typeof t2.optionListeners[n2] && (i2 = t2.optionListeners[n2].call(e2[t2.pluginName], o2));
          }), i2;
        } };
        function W(t2) {
          var e2 = t2.sortable, n2 = t2.rootEl, o2 = t2.name, i2 = t2.targetEl, r2 = t2.cloneEl, a2 = t2.toEl, l2 = t2.fromEl, s2 = t2.oldIndex, c2 = t2.newIndex, u2 = t2.oldDraggableIndex, d2 = t2.newDraggableIndex, h2 = t2.originalEvent, f2 = t2.putSortable, p2 = t2.extraEventProperties;
          if (e2 = e2 || n2 && n2[j]) {
            var g2, m2 = e2.options, t2 = "on" + o2.charAt(0).toUpperCase() + o2.substr(1);
            !window.CustomEvent || y || w ? (g2 = document.createEvent("Event")).initEvent(o2, true, true) : g2 = new CustomEvent(o2, { bubbles: true, cancelable: true }), g2.to = a2 || n2, g2.from = l2 || n2, g2.item = i2 || n2, g2.clone = r2, g2.oldIndex = s2, g2.newIndex = c2, g2.oldDraggableIndex = u2, g2.newDraggableIndex = d2, g2.originalEvent = h2, g2.pullMode = f2 ? f2.lastPutMode : void 0;
            var v2, b2 = M(M({}, p2), K.getEventProperties(o2, e2));
            for (v2 in b2)
              g2[v2] = b2[v2];
            n2 && n2.dispatchEvent(g2), m2[t2] && m2[t2].call(e2, g2);
          }
        }
        function z(t2, e2) {
          var n2 = (o2 = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).evt, o2 = i(o2, G);
          K.pluginEvent.bind(Bt)(t2, e2, M({ dragEl: q, parentEl: V, ghostEl: Z, rootEl: $2, nextEl: Q, lastDownEl: J, cloneEl: tt, cloneHidden: et, dragStarted: pt, putSortable: lt, activeSortable: Bt.active, originalEvent: n2, oldIndex: nt, oldDraggableIndex: it, newIndex: ot, newDraggableIndex: rt, hideGhostForTarget: kt, unhideGhostForTarget: Rt, cloneNowHidden: function() {
            et = true;
          }, cloneNowShown: function() {
            et = false;
          }, dispatchSortableEvent: function(t3) {
            U({ sortable: e2, name: t3, originalEvent: n2 });
          } }, o2));
        }
        var G = ["evt"];
        function U(t2) {
          W(M({ putSortable: lt, cloneEl: tt, targetEl: q, rootEl: $2, oldIndex: nt, oldDraggableIndex: it, newIndex: ot, newDraggableIndex: rt }, t2));
        }
        var q, V, Z, $2, Q, J, tt, et, nt, ot, it, rt, at, lt, st, ct, ut, dt, ht, ft, pt, gt, mt, vt, bt, yt = false, wt = false, Et = [], Dt = false, St = false, _t = [], Ct = false, Tt = [], xt = "undefined" != typeof document, Ot = n, At = w || y ? "cssFloat" : "float", Mt = xt && !c && !n && "draggable" in document.createElement("div"), Nt = function() {
          if (xt) {
            if (y)
              return false;
            var t2 = document.createElement("x");
            return t2.style.cssText = "pointer-events:auto", "auto" === t2.style.pointerEvents;
          }
        }(), It = function(t2, e2) {
          var n2 = P(t2), o2 = parseInt(n2.width) - parseInt(n2.paddingLeft) - parseInt(n2.paddingRight) - parseInt(n2.borderLeftWidth) - parseInt(n2.borderRightWidth), i2 = X(t2, 0, e2), r2 = X(t2, 1, e2), a2 = i2 && P(i2), l2 = r2 && P(r2), s2 = a2 && parseInt(a2.marginLeft) + parseInt(a2.marginRight) + k(i2).width, t2 = l2 && parseInt(l2.marginLeft) + parseInt(l2.marginRight) + k(r2).width;
          if ("flex" === n2.display)
            return "column" === n2.flexDirection || "column-reverse" === n2.flexDirection ? "vertical" : "horizontal";
          if ("grid" === n2.display)
            return n2.gridTemplateColumns.split(" ").length <= 1 ? "vertical" : "horizontal";
          if (i2 && a2.float && "none" !== a2.float) {
            e2 = "left" === a2.float ? "left" : "right";
            return !r2 || "both" !== l2.clear && l2.clear !== e2 ? "horizontal" : "vertical";
          }
          return i2 && ("block" === a2.display || "flex" === a2.display || "table" === a2.display || "grid" === a2.display || o2 <= s2 && "none" === n2[At] || r2 && "none" === n2[At] && o2 < s2 + t2) ? "vertical" : "horizontal";
        }, Pt = function(t2) {
          function l2(r2, a2) {
            return function(t3, e3, n3, o2) {
              var i2 = t3.options.group.name && e3.options.group.name && t3.options.group.name === e3.options.group.name;
              if (null == r2 && (a2 || i2))
                return true;
              if (null == r2 || false === r2)
                return false;
              if (a2 && "clone" === r2)
                return r2;
              if ("function" == typeof r2)
                return l2(r2(t3, e3, n3, o2), a2)(t3, e3, n3, o2);
              e3 = (a2 ? t3 : e3).options.group.name;
              return true === r2 || "string" == typeof r2 && r2 === e3 || r2.join && -1 < r2.indexOf(e3);
            };
          }
          var e2 = {}, n2 = t2.group;
          n2 && "object" == o(n2) || (n2 = { name: n2 }), e2.name = n2.name, e2.checkPull = l2(n2.pull, true), e2.checkPut = l2(n2.put), e2.revertClone = n2.revertClone, t2.group = e2;
        }, kt = function() {
          !Nt && Z && P(Z, "display", "none");
        }, Rt = function() {
          !Nt && Z && P(Z, "display", "");
        };
        xt && !c && document.addEventListener("click", function(t2) {
          if (wt)
            return t2.preventDefault(), t2.stopPropagation && t2.stopPropagation(), t2.stopImmediatePropagation && t2.stopImmediatePropagation(), wt = false;
        }, true);
        function Xt(t2) {
          if (q) {
            t2 = t2.touches ? t2.touches[0] : t2;
            var e2 = (i2 = t2.clientX, r2 = t2.clientY, Et.some(function(t3) {
              var e3 = t3[j].options.emptyInsertThreshold;
              if (e3 && !Y(t3)) {
                var n3 = k(t3), o3 = i2 >= n3.left - e3 && i2 <= n3.right + e3, e3 = r2 >= n3.top - e3 && r2 <= n3.bottom + e3;
                return o3 && e3 ? a2 = t3 : void 0;
              }
            }), a2);
            if (e2) {
              var n2, o2 = {};
              for (n2 in t2)
                t2.hasOwnProperty(n2) && (o2[n2] = t2[n2]);
              o2.target = o2.rootEl = e2, o2.preventDefault = void 0, o2.stopPropagation = void 0, e2[j]._onDragOver(o2);
            }
          }
          var i2, r2, a2;
        }
        function Yt(t2) {
          q && q.parentNode[j]._isOutsideThisEl(t2.target);
        }
        function Bt(t2, e2) {
          if (!t2 || !t2.nodeType || 1 !== t2.nodeType)
            throw "Sortable: `el` must be an HTMLElement, not ".concat({}.toString.call(t2));
          this.el = t2, this.options = e2 = a({}, e2), t2[j] = this;
          var n2, o2, i2 = { group: null, sort: true, disabled: false, store: null, handle: null, draggable: /^[uo]l$/i.test(t2.nodeName) ? ">li" : ">*", swapThreshold: 1, invertSwap: false, invertedSwapThreshold: null, removeCloneOnHide: true, direction: function() {
            return It(t2, this.options);
          }, ghostClass: "sortable-ghost", chosenClass: "sortable-chosen", dragClass: "sortable-drag", ignore: "a, img", filter: null, preventOnFilter: true, animation: 0, easing: null, setData: function(t3, e3) {
            t3.setData("Text", e3.textContent);
          }, dropBubble: false, dragoverBubble: false, dataIdAttr: "data-id", delay: 0, delayOnTouchOnly: false, touchStartThreshold: (Number.parseInt ? Number : window).parseInt(window.devicePixelRatio, 10) || 1, forceFallback: false, fallbackClass: "sortable-fallback", fallbackOnBody: false, fallbackTolerance: 0, fallbackOffset: { x: 0, y: 0 }, supportPointer: false !== Bt.supportPointer && "PointerEvent" in window && !u, emptyInsertThreshold: 5 };
          for (n2 in K.initializePlugins(this, t2, i2), i2)
            n2 in e2 || (e2[n2] = i2[n2]);
          for (o2 in Pt(e2), this)
            "_" === o2.charAt(0) && "function" == typeof this[o2] && (this[o2] = this[o2].bind(this));
          this.nativeDraggable = !e2.forceFallback && Mt, this.nativeDraggable && (this.options.touchStartThreshold = 1), e2.supportPointer ? h(t2, "pointerdown", this._onTapStart) : (h(t2, "mousedown", this._onTapStart), h(t2, "touchstart", this._onTapStart)), this.nativeDraggable && (h(t2, "dragover", this), h(t2, "dragenter", this)), Et.push(this.el), e2.store && e2.store.get && this.sort(e2.store.get(this) || []), a(this, x());
        }
        function Ft(t2, e2, n2, o2, i2, r2, a2, l2) {
          var s2, c2, u2 = t2[j], d2 = u2.options.onMove;
          return !window.CustomEvent || y || w ? (s2 = document.createEvent("Event")).initEvent("move", true, true) : s2 = new CustomEvent("move", { bubbles: true, cancelable: true }), s2.to = e2, s2.from = t2, s2.dragged = n2, s2.draggedRect = o2, s2.related = i2 || e2, s2.relatedRect = r2 || k(e2), s2.willInsertAfter = l2, s2.originalEvent = a2, t2.dispatchEvent(s2), c2 = d2 ? d2.call(u2, s2, a2) : c2;
        }
        function jt(t2) {
          t2.draggable = false;
        }
        function Ht() {
          Ct = false;
        }
        function Lt(t2) {
          return setTimeout(t2, 0);
        }
        function Kt(t2) {
          return clearTimeout(t2);
        }
        Bt.prototype = { constructor: Bt, _isOutsideThisEl: function(t2) {
          this.el.contains(t2) || t2 === this.el || (gt = null);
        }, _getDirection: function(t2, e2) {
          return "function" == typeof this.options.direction ? this.options.direction.call(this, t2, e2, q) : this.options.direction;
        }, _onTapStart: function(e2) {
          if (e2.cancelable) {
            var n2 = this, o2 = this.el, t2 = this.options, i2 = t2.preventOnFilter, r2 = e2.type, a2 = e2.touches && e2.touches[0] || e2.pointerType && "touch" === e2.pointerType && e2, l2 = (a2 || e2).target, s2 = e2.target.shadowRoot && (e2.path && e2.path[0] || e2.composedPath && e2.composedPath()[0]) || l2, c2 = t2.filter;
            if (!function(t3) {
              Tt.length = 0;
              var e3 = t3.getElementsByTagName("input"), n3 = e3.length;
              for (; n3--; ) {
                var o3 = e3[n3];
                o3.checked && Tt.push(o3);
              }
            }(o2), !q && !(/mousedown|pointerdown/.test(r2) && 0 !== e2.button || t2.disabled) && !s2.isContentEditable && (this.nativeDraggable || !u || !l2 || "SELECT" !== l2.tagName.toUpperCase()) && !((l2 = N(l2, t2.draggable, o2, false)) && l2.animated || J === l2)) {
              if (nt = B(l2), it = B(l2, t2.draggable), "function" == typeof c2) {
                if (c2.call(this, e2, l2, this))
                  return U({ sortable: n2, rootEl: s2, name: "filter", targetEl: l2, toEl: o2, fromEl: o2 }), z("filter", n2, { evt: e2 }), void (i2 && e2.cancelable && e2.preventDefault());
              } else if (c2 = c2 && c2.split(",").some(function(t3) {
                if (t3 = N(s2, t3.trim(), o2, false))
                  return U({ sortable: n2, rootEl: t3, name: "filter", targetEl: l2, fromEl: o2, toEl: o2 }), z("filter", n2, { evt: e2 }), true;
              }))
                return void (i2 && e2.cancelable && e2.preventDefault());
              t2.handle && !N(s2, t2.handle, o2, false) || this._prepareDragStart(e2, a2, l2);
            }
          }
        }, _prepareDragStart: function(t2, e2, n2) {
          var o2, i2 = this, r2 = i2.el, a2 = i2.options, l2 = r2.ownerDocument;
          n2 && !q && n2.parentNode === r2 && (o2 = k(n2), $2 = r2, V = (q = n2).parentNode, Q = q.nextSibling, J = n2, at = a2.group, st = { target: Bt.dragged = q, clientX: (e2 || t2).clientX, clientY: (e2 || t2).clientY }, ht = st.clientX - o2.left, ft = st.clientY - o2.top, this._lastX = (e2 || t2).clientX, this._lastY = (e2 || t2).clientY, q.style["will-change"] = "all", o2 = function() {
            z("delayEnded", i2, { evt: t2 }), Bt.eventCanceled ? i2._onDrop() : (i2._disableDelayedDragEvents(), !s && i2.nativeDraggable && (q.draggable = true), i2._triggerDragStart(t2, e2), U({ sortable: i2, name: "choose", originalEvent: t2 }), I(q, a2.chosenClass, true));
          }, a2.ignore.split(",").forEach(function(t3) {
            b(q, t3.trim(), jt);
          }), h(l2, "dragover", Xt), h(l2, "mousemove", Xt), h(l2, "touchmove", Xt), h(l2, "mouseup", i2._onDrop), h(l2, "touchend", i2._onDrop), h(l2, "touchcancel", i2._onDrop), s && this.nativeDraggable && (this.options.touchStartThreshold = 4, q.draggable = true), z("delayStart", this, { evt: t2 }), !a2.delay || a2.delayOnTouchOnly && !e2 || this.nativeDraggable && (w || y) ? o2() : Bt.eventCanceled ? this._onDrop() : (h(l2, "mouseup", i2._disableDelayedDrag), h(l2, "touchend", i2._disableDelayedDrag), h(l2, "touchcancel", i2._disableDelayedDrag), h(l2, "mousemove", i2._delayedDragTouchMoveHandler), h(l2, "touchmove", i2._delayedDragTouchMoveHandler), a2.supportPointer && h(l2, "pointermove", i2._delayedDragTouchMoveHandler), i2._dragStartTimer = setTimeout(o2, a2.delay)));
        }, _delayedDragTouchMoveHandler: function(t2) {
          t2 = t2.touches ? t2.touches[0] : t2;
          Math.max(Math.abs(t2.clientX - this._lastX), Math.abs(t2.clientY - this._lastY)) >= Math.floor(this.options.touchStartThreshold / (this.nativeDraggable && window.devicePixelRatio || 1)) && this._disableDelayedDrag();
        }, _disableDelayedDrag: function() {
          q && jt(q), clearTimeout(this._dragStartTimer), this._disableDelayedDragEvents();
        }, _disableDelayedDragEvents: function() {
          var t2 = this.el.ownerDocument;
          f(t2, "mouseup", this._disableDelayedDrag), f(t2, "touchend", this._disableDelayedDrag), f(t2, "touchcancel", this._disableDelayedDrag), f(t2, "mousemove", this._delayedDragTouchMoveHandler), f(t2, "touchmove", this._delayedDragTouchMoveHandler), f(t2, "pointermove", this._delayedDragTouchMoveHandler);
        }, _triggerDragStart: function(t2, e2) {
          e2 = e2 || "touch" == t2.pointerType && t2, !this.nativeDraggable || e2 ? this.options.supportPointer ? h(document, "pointermove", this._onTouchMove) : h(document, e2 ? "touchmove" : "mousemove", this._onTouchMove) : (h(q, "dragend", this), h($2, "dragstart", this._onDragStart));
          try {
            document.selection ? Lt(function() {
              document.selection.empty();
            }) : window.getSelection().removeAllRanges();
          } catch (t3) {
          }
        }, _dragStarted: function(t2, e2) {
          var n2;
          yt = false, $2 && q ? (z("dragStarted", this, { evt: e2 }), this.nativeDraggable && h(document, "dragover", Yt), n2 = this.options, t2 || I(q, n2.dragClass, false), I(q, n2.ghostClass, true), Bt.active = this, t2 && this._appendGhost(), U({ sortable: this, name: "start", originalEvent: e2 })) : this._nulling();
        }, _emulateDragOver: function() {
          if (ct) {
            this._lastX = ct.clientX, this._lastY = ct.clientY, kt();
            for (var t2 = document.elementFromPoint(ct.clientX, ct.clientY), e2 = t2; t2 && t2.shadowRoot && (t2 = t2.shadowRoot.elementFromPoint(ct.clientX, ct.clientY)) !== e2; )
              e2 = t2;
            if (q.parentNode[j]._isOutsideThisEl(t2), e2)
              do {
                if (e2[j]) {
                  if (e2[j]._onDragOver({ clientX: ct.clientX, clientY: ct.clientY, target: t2, rootEl: e2 }) && !this.options.dragoverBubble)
                    break;
                }
              } while (e2 = (t2 = e2).parentNode);
            Rt();
          }
        }, _onTouchMove: function(t2) {
          if (st) {
            var e2 = this.options, n2 = e2.fallbackTolerance, o2 = e2.fallbackOffset, i2 = t2.touches ? t2.touches[0] : t2, r2 = Z && v(Z, true), a2 = Z && r2 && r2.a, l2 = Z && r2 && r2.d, e2 = Ot && bt && E(bt), a2 = (i2.clientX - st.clientX + o2.x) / (a2 || 1) + (e2 ? e2[0] - _t[0] : 0) / (a2 || 1), l2 = (i2.clientY - st.clientY + o2.y) / (l2 || 1) + (e2 ? e2[1] - _t[1] : 0) / (l2 || 1);
            if (!Bt.active && !yt) {
              if (n2 && Math.max(Math.abs(i2.clientX - this._lastX), Math.abs(i2.clientY - this._lastY)) < n2)
                return;
              this._onDragStart(t2, true);
            }
            Z && (r2 ? (r2.e += a2 - (ut || 0), r2.f += l2 - (dt || 0)) : r2 = { a: 1, b: 0, c: 0, d: 1, e: a2, f: l2 }, r2 = "matrix(".concat(r2.a, ",").concat(r2.b, ",").concat(r2.c, ",").concat(r2.d, ",").concat(r2.e, ",").concat(r2.f, ")"), P(Z, "webkitTransform", r2), P(Z, "mozTransform", r2), P(Z, "msTransform", r2), P(Z, "transform", r2), ut = a2, dt = l2, ct = i2), t2.cancelable && t2.preventDefault();
          }
        }, _appendGhost: function() {
          if (!Z) {
            var t2 = this.options.fallbackOnBody ? document.body : $2, e2 = k(q, true, Ot, true, t2), n2 = this.options;
            if (Ot) {
              for (bt = t2; "static" === P(bt, "position") && "none" === P(bt, "transform") && bt !== document; )
                bt = bt.parentNode;
              bt !== document.body && bt !== document.documentElement ? (bt === document && (bt = O()), e2.top += bt.scrollTop, e2.left += bt.scrollLeft) : bt = O(), _t = E(bt);
            }
            I(Z = q.cloneNode(true), n2.ghostClass, false), I(Z, n2.fallbackClass, true), I(Z, n2.dragClass, true), P(Z, "transition", ""), P(Z, "transform", ""), P(Z, "box-sizing", "border-box"), P(Z, "margin", 0), P(Z, "top", e2.top), P(Z, "left", e2.left), P(Z, "width", e2.width), P(Z, "height", e2.height), P(Z, "opacity", "0.8"), P(Z, "position", Ot ? "absolute" : "fixed"), P(Z, "zIndex", "100000"), P(Z, "pointerEvents", "none"), Bt.ghost = Z, t2.appendChild(Z), P(Z, "transform-origin", ht / parseInt(Z.style.width) * 100 + "% " + ft / parseInt(Z.style.height) * 100 + "%");
          }
        }, _onDragStart: function(t2, e2) {
          var n2 = this, o2 = t2.dataTransfer, i2 = n2.options;
          z("dragStart", this, { evt: t2 }), Bt.eventCanceled ? this._onDrop() : (z("setupClone", this), Bt.eventCanceled || ((tt = _(q)).removeAttribute("id"), tt.draggable = false, tt.style["will-change"] = "", this._hideClone(), I(tt, this.options.chosenClass, false), Bt.clone = tt), n2.cloneId = Lt(function() {
            z("clone", n2), Bt.eventCanceled || (n2.options.removeCloneOnHide || $2.insertBefore(tt, q), n2._hideClone(), U({ sortable: n2, name: "clone" }));
          }), e2 || I(q, i2.dragClass, true), e2 ? (wt = true, n2._loopId = setInterval(n2._emulateDragOver, 50)) : (f(document, "mouseup", n2._onDrop), f(document, "touchend", n2._onDrop), f(document, "touchcancel", n2._onDrop), o2 && (o2.effectAllowed = "move", i2.setData && i2.setData.call(n2, o2, q)), h(document, "drop", n2), P(q, "transform", "translateZ(0)")), yt = true, n2._dragStartId = Lt(n2._dragStarted.bind(n2, e2, t2)), h(document, "selectstart", n2), pt = true, u && P(document.body, "user-select", "none"));
        }, _onDragOver: function(n2) {
          var o2, i2, r2, t2, a2 = this.el, l2 = n2.target, e2 = this.options, s2 = e2.group, c2 = Bt.active, u2 = at === s2, d2 = e2.sort, h2 = lt || c2, f2 = this, p2 = false;
          if (!Ct) {
            if (void 0 !== n2.preventDefault && n2.cancelable && n2.preventDefault(), l2 = N(l2, e2.draggable, a2, true), T2("dragOver"), Bt.eventCanceled)
              return p2;
            if (q.contains(n2.target) || l2.animated && l2.animatingX && l2.animatingY || f2._ignoreWhileAnimating === l2)
              return O2(false);
            if (wt = false, c2 && !e2.disabled && (u2 ? d2 || (i2 = V !== $2) : lt === this || (this.lastPutMode = at.checkPull(this, c2, q, n2)) && s2.checkPut(this, c2, q, n2))) {
              if (r2 = "vertical" === this._getDirection(n2, l2), o2 = k(q), T2("dragOverValid"), Bt.eventCanceled)
                return p2;
              if (i2)
                return V = $2, x2(), this._hideClone(), T2("revert"), Bt.eventCanceled || (Q ? $2.insertBefore(q, Q) : $2.appendChild(q)), O2(true);
              var g2 = Y(a2, e2.draggable);
              if (!g2 || function(t3, e3, n3) {
                n3 = k(Y(n3.el, n3.options.draggable));
                return e3 ? t3.clientX > n3.right + 10 || t3.clientX <= n3.right && t3.clientY > n3.bottom && t3.clientX >= n3.left : t3.clientX > n3.right && t3.clientY > n3.top || t3.clientX <= n3.right && t3.clientY > n3.bottom + 10;
              }(n2, r2, this) && !g2.animated) {
                if (g2 === q)
                  return O2(false);
                if ((l2 = g2 && a2 === n2.target ? g2 : l2) && (w2 = k(l2)), false !== Ft($2, a2, q, o2, l2, w2, n2, !!l2))
                  return x2(), g2 && g2.nextSibling ? a2.insertBefore(q, g2.nextSibling) : a2.appendChild(q), V = a2, A2(), O2(true);
              } else if (g2 && function(t3, e3, n3) {
                n3 = k(X(n3.el, 0, n3.options, true));
                return e3 ? t3.clientX < n3.left - 10 || t3.clientY < n3.top && t3.clientX < n3.right : t3.clientY < n3.top - 10 || t3.clientY < n3.bottom && t3.clientX < n3.left;
              }(n2, r2, this)) {
                var m2 = X(a2, 0, e2, true);
                if (m2 === q)
                  return O2(false);
                if (w2 = k(l2 = m2), false !== Ft($2, a2, q, o2, l2, w2, n2, false))
                  return x2(), a2.insertBefore(q, m2), V = a2, A2(), O2(true);
              } else if (l2.parentNode === a2) {
                var v2, b2, y2, w2 = k(l2), E2 = q.parentNode !== a2, D2 = (D2 = q.animated && q.toRect || o2, C2 = l2.animated && l2.toRect || w2, S2 = (t2 = r2) ? D2.left : D2.top, s2 = t2 ? D2.right : D2.bottom, g2 = t2 ? D2.width : D2.height, m2 = t2 ? C2.left : C2.top, D2 = t2 ? C2.right : C2.bottom, C2 = t2 ? C2.width : C2.height, !(S2 === m2 || s2 === D2 || S2 + g2 / 2 === m2 + C2 / 2)), S2 = r2 ? "top" : "left", g2 = R(l2, "top", "top") || R(q, "top", "top"), m2 = g2 ? g2.scrollTop : void 0;
                if (gt !== l2 && (b2 = w2[S2], Dt = false, St = !D2 && e2.invertSwap || E2), 0 !== (v2 = function(t3, e3, n3, o3, i3, r3, a3, l3) {
                  var s3 = o3 ? t3.clientY : t3.clientX, c3 = o3 ? n3.height : n3.width, t3 = o3 ? n3.top : n3.left, o3 = o3 ? n3.bottom : n3.right, n3 = false;
                  if (!a3) {
                    if (l3 && vt < c3 * i3) {
                      if (Dt = !Dt && (1 === mt ? t3 + c3 * r3 / 2 < s3 : s3 < o3 - c3 * r3 / 2) ? true : Dt)
                        n3 = true;
                      else if (1 === mt ? s3 < t3 + vt : o3 - vt < s3)
                        return -mt;
                    } else if (t3 + c3 * (1 - i3) / 2 < s3 && s3 < o3 - c3 * (1 - i3) / 2)
                      return function(t4) {
                        return B(q) < B(t4) ? 1 : -1;
                      }(e3);
                  }
                  if ((n3 = n3 || a3) && (s3 < t3 + c3 * r3 / 2 || o3 - c3 * r3 / 2 < s3))
                    return t3 + c3 / 2 < s3 ? 1 : -1;
                  return 0;
                }(n2, l2, w2, r2, D2 ? 1 : e2.swapThreshold, null == e2.invertedSwapThreshold ? e2.swapThreshold : e2.invertedSwapThreshold, St, gt === l2)))
                  for (var _2 = B(q); (y2 = V.children[_2 -= v2]) && ("none" === P(y2, "display") || y2 === Z); )
                    ;
                if (0 === v2 || y2 === l2)
                  return O2(false);
                mt = v2;
                var C2 = (gt = l2).nextElementSibling, E2 = false, D2 = Ft($2, a2, q, o2, l2, w2, n2, E2 = 1 === v2);
                if (false !== D2)
                  return 1 !== D2 && -1 !== D2 || (E2 = 1 === D2), Ct = true, setTimeout(Ht, 30), x2(), E2 && !C2 ? a2.appendChild(q) : l2.parentNode.insertBefore(q, E2 ? C2 : l2), g2 && F(g2, 0, m2 - g2.scrollTop), V = q.parentNode, void 0 === b2 || St || (vt = Math.abs(b2 - k(l2)[S2])), A2(), O2(true);
              }
              if (a2.contains(q))
                return O2(false);
            }
            return false;
          }
          function T2(t3, e3) {
            z(t3, f2, M({ evt: n2, isOwner: u2, axis: r2 ? "vertical" : "horizontal", revert: i2, dragRect: o2, targetRect: w2, canSort: d2, fromSortable: h2, target: l2, completed: O2, onMove: function(t4, e4) {
              return Ft($2, a2, q, o2, t4, k(t4), n2, e4);
            }, changed: A2 }, e3));
          }
          function x2() {
            T2("dragOverAnimationCapture"), f2.captureAnimationState(), f2 !== h2 && h2.captureAnimationState();
          }
          function O2(t3) {
            return T2("dragOverCompleted", { insertion: t3 }), t3 && (u2 ? c2._hideClone() : c2._showClone(f2), f2 !== h2 && (I(q, (lt || c2).options.ghostClass, false), I(q, e2.ghostClass, true)), lt !== f2 && f2 !== Bt.active ? lt = f2 : f2 === Bt.active && lt && (lt = null), h2 === f2 && (f2._ignoreWhileAnimating = l2), f2.animateAll(function() {
              T2("dragOverAnimationComplete"), f2._ignoreWhileAnimating = null;
            }), f2 !== h2 && (h2.animateAll(), h2._ignoreWhileAnimating = null)), (l2 === q && !q.animated || l2 === a2 && !l2.animated) && (gt = null), e2.dragoverBubble || n2.rootEl || l2 === document || (q.parentNode[j]._isOutsideThisEl(n2.target), t3 || Xt(n2)), !e2.dragoverBubble && n2.stopPropagation && n2.stopPropagation(), p2 = true;
          }
          function A2() {
            ot = B(q), rt = B(q, e2.draggable), U({ sortable: f2, name: "change", toEl: a2, newIndex: ot, newDraggableIndex: rt, originalEvent: n2 });
          }
        }, _ignoreWhileAnimating: null, _offMoveEvents: function() {
          f(document, "mousemove", this._onTouchMove), f(document, "touchmove", this._onTouchMove), f(document, "pointermove", this._onTouchMove), f(document, "dragover", Xt), f(document, "mousemove", Xt), f(document, "touchmove", Xt);
        }, _offUpEvents: function() {
          var t2 = this.el.ownerDocument;
          f(t2, "mouseup", this._onDrop), f(t2, "touchend", this._onDrop), f(t2, "pointerup", this._onDrop), f(t2, "touchcancel", this._onDrop), f(document, "selectstart", this);
        }, _onDrop: function(t2) {
          var e2 = this.el, n2 = this.options;
          ot = B(q), rt = B(q, n2.draggable), z("drop", this, { evt: t2 }), V = q && q.parentNode, ot = B(q), rt = B(q, n2.draggable), Bt.eventCanceled || (Dt = St = yt = false, clearInterval(this._loopId), clearTimeout(this._dragStartTimer), Kt(this.cloneId), Kt(this._dragStartId), this.nativeDraggable && (f(document, "drop", this), f(e2, "dragstart", this._onDragStart)), this._offMoveEvents(), this._offUpEvents(), u && P(document.body, "user-select", ""), P(q, "transform", ""), t2 && (pt && (t2.cancelable && t2.preventDefault(), n2.dropBubble || t2.stopPropagation()), Z && Z.parentNode && Z.parentNode.removeChild(Z), ($2 === V || lt && "clone" !== lt.lastPutMode) && tt && tt.parentNode && tt.parentNode.removeChild(tt), q && (this.nativeDraggable && f(q, "dragend", this), jt(q), q.style["will-change"] = "", pt && !yt && I(q, (lt || this).options.ghostClass, false), I(q, this.options.chosenClass, false), U({ sortable: this, name: "unchoose", toEl: V, newIndex: null, newDraggableIndex: null, originalEvent: t2 }), $2 !== V ? (0 <= ot && (U({ rootEl: V, name: "add", toEl: V, fromEl: $2, originalEvent: t2 }), U({ sortable: this, name: "remove", toEl: V, originalEvent: t2 }), U({ rootEl: V, name: "sort", toEl: V, fromEl: $2, originalEvent: t2 }), U({ sortable: this, name: "sort", toEl: V, originalEvent: t2 })), lt && lt.save()) : ot !== nt && 0 <= ot && (U({ sortable: this, name: "update", toEl: V, originalEvent: t2 }), U({ sortable: this, name: "sort", toEl: V, originalEvent: t2 })), Bt.active && (null != ot && -1 !== ot || (ot = nt, rt = it), U({ sortable: this, name: "end", toEl: V, originalEvent: t2 }), this.save())))), this._nulling();
        }, _nulling: function() {
          z("nulling", this), $2 = q = V = Z = Q = tt = J = et = st = ct = pt = ot = rt = nt = it = gt = mt = lt = at = Bt.dragged = Bt.ghost = Bt.clone = Bt.active = null, Tt.forEach(function(t2) {
            t2.checked = true;
          }), Tt.length = ut = dt = 0;
        }, handleEvent: function(t2) {
          switch (t2.type) {
            case "drop":
            case "dragend":
              this._onDrop(t2);
              break;
            case "dragenter":
            case "dragover":
              q && (this._onDragOver(t2), function(t3) {
                t3.dataTransfer && (t3.dataTransfer.dropEffect = "move");
                t3.cancelable && t3.preventDefault();
              }(t2));
              break;
            case "selectstart":
              t2.preventDefault();
          }
        }, toArray: function() {
          for (var t2, e2 = [], n2 = this.el.children, o2 = 0, i2 = n2.length, r2 = this.options; o2 < i2; o2++)
            N(t2 = n2[o2], r2.draggable, this.el, false) && e2.push(t2.getAttribute(r2.dataIdAttr) || function(t3) {
              var e3 = t3.tagName + t3.className + t3.src + t3.href + t3.textContent, n3 = e3.length, o3 = 0;
              for (; n3--; )
                o3 += e3.charCodeAt(n3);
              return o3.toString(36);
            }(t2));
          return e2;
        }, sort: function(t2, e2) {
          var n2 = {}, o2 = this.el;
          this.toArray().forEach(function(t3, e3) {
            e3 = o2.children[e3];
            N(e3, this.options.draggable, o2, false) && (n2[t3] = e3);
          }, this), e2 && this.captureAnimationState(), t2.forEach(function(t3) {
            n2[t3] && (o2.removeChild(n2[t3]), o2.appendChild(n2[t3]));
          }), e2 && this.animateAll();
        }, save: function() {
          var t2 = this.options.store;
          t2 && t2.set && t2.set(this);
        }, closest: function(t2, e2) {
          return N(t2, e2 || this.options.draggable, this.el, false);
        }, option: function(t2, e2) {
          var n2 = this.options;
          if (void 0 === e2)
            return n2[t2];
          var o2 = K.modifyOption(this, t2, e2);
          n2[t2] = void 0 !== o2 ? o2 : e2, "group" === t2 && Pt(n2);
        }, destroy: function() {
          z("destroy", this);
          var t2 = this.el;
          t2[j] = null, f(t2, "mousedown", this._onTapStart), f(t2, "touchstart", this._onTapStart), f(t2, "pointerdown", this._onTapStart), this.nativeDraggable && (f(t2, "dragover", this), f(t2, "dragenter", this)), Array.prototype.forEach.call(t2.querySelectorAll("[draggable]"), function(t3) {
            t3.removeAttribute("draggable");
          }), this._onDrop(), this._disableDelayedDragEvents(), Et.splice(Et.indexOf(this.el), 1), this.el = t2 = null;
        }, _hideClone: function() {
          et || (z("hideClone", this), Bt.eventCanceled || (P(tt, "display", "none"), this.options.removeCloneOnHide && tt.parentNode && tt.parentNode.removeChild(tt), et = true));
        }, _showClone: function(t2) {
          "clone" === t2.lastPutMode ? et && (z("showClone", this), Bt.eventCanceled || (q.parentNode != $2 || this.options.group.revertClone ? Q ? $2.insertBefore(tt, Q) : $2.appendChild(tt) : $2.insertBefore(tt, q), this.options.group.revertClone && this.animate(q, tt), P(tt, "display", ""), et = false)) : this._hideClone();
        } }, xt && h(document, "touchmove", function(t2) {
          (Bt.active || yt) && t2.cancelable && t2.preventDefault();
        }), Bt.utils = { on: h, off: f, css: P, find: b, is: function(t2, e2) {
          return !!N(t2, e2, t2, false);
        }, extend: function(t2, e2) {
          if (t2 && e2)
            for (var n2 in e2)
              e2.hasOwnProperty(n2) && (t2[n2] = e2[n2]);
          return t2;
        }, throttle: S, closest: N, toggleClass: I, clone: _, index: B, nextTick: Lt, cancelNextTick: Kt, detectDirection: It, getChild: X }, Bt.get = function(t2) {
          return t2[j];
        }, Bt.mount = function() {
          for (var t2 = arguments.length, e2 = new Array(t2), n2 = 0; n2 < t2; n2++)
            e2[n2] = arguments[n2];
          (e2 = e2[0].constructor === Array ? e2[0] : e2).forEach(function(t3) {
            if (!t3.prototype || !t3.prototype.constructor)
              throw "Sortable: Mounted plugin must be a constructor function, not ".concat({}.toString.call(t3));
            t3.utils && (Bt.utils = M(M({}, Bt.utils), t3.utils)), K.mount(t3);
          });
        }, Bt.create = function(t2, e2) {
          return new Bt(t2, e2);
        };
        var Wt, zt, Gt, Ut, qt, Vt, Zt = [], $t = !(Bt.version = "1.15.0");
        function Qt() {
          Zt.forEach(function(t2) {
            clearInterval(t2.pid);
          }), Zt = [];
        }
        function Jt() {
          clearInterval(Vt);
        }
        var te, ee = S(function(n2, t2, e2, o2) {
          if (t2.scroll) {
            var i2, r2 = (n2.touches ? n2.touches[0] : n2).clientX, a2 = (n2.touches ? n2.touches[0] : n2).clientY, l2 = t2.scrollSensitivity, s2 = t2.scrollSpeed, c2 = O(), u2 = false;
            zt !== e2 && (zt = e2, Qt(), Wt = t2.scroll, i2 = t2.scrollFn, true === Wt && (Wt = A(e2, true)));
            var d2 = 0, h2 = Wt;
            do {
              var f2 = h2, p2 = k(f2), g2 = p2.top, m2 = p2.bottom, v2 = p2.left, b2 = p2.right, y2 = p2.width, w2 = p2.height, E2 = void 0, D2 = void 0, S2 = f2.scrollWidth, _2 = f2.scrollHeight, C2 = P(f2), T2 = f2.scrollLeft, p2 = f2.scrollTop, D2 = f2 === c2 ? (E2 = y2 < S2 && ("auto" === C2.overflowX || "scroll" === C2.overflowX || "visible" === C2.overflowX), w2 < _2 && ("auto" === C2.overflowY || "scroll" === C2.overflowY || "visible" === C2.overflowY)) : (E2 = y2 < S2 && ("auto" === C2.overflowX || "scroll" === C2.overflowX), w2 < _2 && ("auto" === C2.overflowY || "scroll" === C2.overflowY)), T2 = E2 && (Math.abs(b2 - r2) <= l2 && T2 + y2 < S2) - (Math.abs(v2 - r2) <= l2 && !!T2), p2 = D2 && (Math.abs(m2 - a2) <= l2 && p2 + w2 < _2) - (Math.abs(g2 - a2) <= l2 && !!p2);
              if (!Zt[d2])
                for (var x2 = 0; x2 <= d2; x2++)
                  Zt[x2] || (Zt[x2] = {});
              Zt[d2].vx == T2 && Zt[d2].vy == p2 && Zt[d2].el === f2 || (Zt[d2].el = f2, Zt[d2].vx = T2, Zt[d2].vy = p2, clearInterval(Zt[d2].pid), 0 == T2 && 0 == p2 || (u2 = true, Zt[d2].pid = setInterval(function() {
                o2 && 0 === this.layer && Bt.active._onTouchMove(qt);
                var t3 = Zt[this.layer].vy ? Zt[this.layer].vy * s2 : 0, e3 = Zt[this.layer].vx ? Zt[this.layer].vx * s2 : 0;
                "function" == typeof i2 && "continue" !== i2.call(Bt.dragged.parentNode[j], e3, t3, n2, qt, Zt[this.layer].el) || F(Zt[this.layer].el, e3, t3);
              }.bind({ layer: d2 }), 24))), d2++;
            } while (t2.bubbleScroll && h2 !== c2 && (h2 = A(h2, false)));
            $t = u2;
          }
        }, 30), c = function(t2) {
          var e2 = t2.originalEvent, n2 = t2.putSortable, o2 = t2.dragEl, i2 = t2.activeSortable, r2 = t2.dispatchSortableEvent, a2 = t2.hideGhostForTarget, t2 = t2.unhideGhostForTarget;
          e2 && (i2 = n2 || i2, a2(), e2 = e2.changedTouches && e2.changedTouches.length ? e2.changedTouches[0] : e2, e2 = document.elementFromPoint(e2.clientX, e2.clientY), t2(), i2 && !i2.el.contains(e2) && (r2("spill"), this.onSpill({ dragEl: o2, putSortable: n2 })));
        };
        function ne() {
        }
        function oe() {
        }
        ne.prototype = { startIndex: null, dragStart: function(t2) {
          t2 = t2.oldDraggableIndex;
          this.startIndex = t2;
        }, onSpill: function(t2) {
          var e2 = t2.dragEl, n2 = t2.putSortable;
          this.sortable.captureAnimationState(), n2 && n2.captureAnimationState();
          t2 = X(this.sortable.el, this.startIndex, this.options);
          t2 ? this.sortable.el.insertBefore(e2, t2) : this.sortable.el.appendChild(e2), this.sortable.animateAll(), n2 && n2.animateAll();
        }, drop: c }, a(ne, { pluginName: "revertOnSpill" }), oe.prototype = { onSpill: function(t2) {
          var e2 = t2.dragEl, t2 = t2.putSortable || this.sortable;
          t2.captureAnimationState(), e2.parentNode && e2.parentNode.removeChild(e2), t2.animateAll();
        }, drop: c }, a(oe, { pluginName: "removeOnSpill" });
        var ie, re, ae, le, se, ce = [], ue = [], de = false, he = false, fe = false;
        function pe(n2, o2) {
          ue.forEach(function(t2, e2) {
            e2 = o2.children[t2.sortableIndex + (n2 ? Number(e2) : 0)];
            e2 ? o2.insertBefore(t2, e2) : o2.appendChild(t2);
          });
        }
        function ge() {
          ce.forEach(function(t2) {
            t2 !== ae && t2.parentNode && t2.parentNode.removeChild(t2);
          });
        }
        return Bt.mount(new function() {
          function t2() {
            for (var t3 in this.defaults = { scroll: true, forceAutoScrollFallback: false, scrollSensitivity: 30, scrollSpeed: 10, bubbleScroll: true }, this)
              "_" === t3.charAt(0) && "function" == typeof this[t3] && (this[t3] = this[t3].bind(this));
          }
          return t2.prototype = { dragStarted: function(t3) {
            t3 = t3.originalEvent;
            this.sortable.nativeDraggable ? h(document, "dragover", this._handleAutoScroll) : this.options.supportPointer ? h(document, "pointermove", this._handleFallbackAutoScroll) : t3.touches ? h(document, "touchmove", this._handleFallbackAutoScroll) : h(document, "mousemove", this._handleFallbackAutoScroll);
          }, dragOverCompleted: function(t3) {
            t3 = t3.originalEvent;
            this.options.dragOverBubble || t3.rootEl || this._handleAutoScroll(t3);
          }, drop: function() {
            this.sortable.nativeDraggable ? f(document, "dragover", this._handleAutoScroll) : (f(document, "pointermove", this._handleFallbackAutoScroll), f(document, "touchmove", this._handleFallbackAutoScroll), f(document, "mousemove", this._handleFallbackAutoScroll)), Jt(), Qt(), clearTimeout(g), g = void 0;
          }, nulling: function() {
            qt = zt = Wt = $t = Vt = Gt = Ut = null, Zt.length = 0;
          }, _handleFallbackAutoScroll: function(t3) {
            this._handleAutoScroll(t3, true);
          }, _handleAutoScroll: function(e2, n2) {
            var o2, i2 = this, r2 = (e2.touches ? e2.touches[0] : e2).clientX, a2 = (e2.touches ? e2.touches[0] : e2).clientY, t3 = document.elementFromPoint(r2, a2);
            qt = e2, n2 || this.options.forceAutoScrollFallback || w || y || u ? (ee(e2, this.options, t3, n2), o2 = A(t3, true), !$t || Vt && r2 === Gt && a2 === Ut || (Vt && Jt(), Vt = setInterval(function() {
              var t4 = A(document.elementFromPoint(r2, a2), true);
              t4 !== o2 && (o2 = t4, Qt()), ee(e2, i2.options, t4, n2);
            }, 10), Gt = r2, Ut = a2)) : this.options.bubbleScroll && A(t3, true) !== O() ? ee(e2, this.options, A(t3, false), false) : Qt();
          } }, a(t2, { pluginName: "scroll", initializeByDefault: true });
        }()), Bt.mount(oe, ne), Bt.mount(new function() {
          function t2() {
            this.defaults = { swapClass: "sortable-swap-highlight" };
          }
          return t2.prototype = { dragStart: function(t3) {
            t3 = t3.dragEl;
            te = t3;
          }, dragOverValid: function(t3) {
            var e2 = t3.completed, n2 = t3.target, o2 = t3.onMove, i2 = t3.activeSortable, r2 = t3.changed, a2 = t3.cancel;
            i2.options.swap && (t3 = this.sortable.el, i2 = this.options, n2 && n2 !== t3 && (t3 = te, te = false !== o2(n2) ? (I(n2, i2.swapClass, true), n2) : null, t3 && t3 !== te && I(t3, i2.swapClass, false)), r2(), e2(true), a2());
          }, drop: function(t3) {
            var e2, n2, o2 = t3.activeSortable, i2 = t3.putSortable, r2 = t3.dragEl, a2 = i2 || this.sortable, l2 = this.options;
            te && I(te, l2.swapClass, false), te && (l2.swap || i2 && i2.options.swap) && r2 !== te && (a2.captureAnimationState(), a2 !== o2 && o2.captureAnimationState(), n2 = te, t3 = (e2 = r2).parentNode, l2 = n2.parentNode, t3 && l2 && !t3.isEqualNode(n2) && !l2.isEqualNode(e2) && (i2 = B(e2), r2 = B(n2), t3.isEqualNode(l2) && i2 < r2 && r2++, t3.insertBefore(n2, t3.children[i2]), l2.insertBefore(e2, l2.children[r2])), a2.animateAll(), a2 !== o2 && o2.animateAll());
          }, nulling: function() {
            te = null;
          } }, a(t2, { pluginName: "swap", eventProperties: function() {
            return { swapItem: te };
          } });
        }()), Bt.mount(new function() {
          function t2(o2) {
            for (var t3 in this)
              "_" === t3.charAt(0) && "function" == typeof this[t3] && (this[t3] = this[t3].bind(this));
            o2.options.avoidImplicitDeselect || (o2.options.supportPointer ? h(document, "pointerup", this._deselectMultiDrag) : (h(document, "mouseup", this._deselectMultiDrag), h(document, "touchend", this._deselectMultiDrag))), h(document, "keydown", this._checkKeyDown), h(document, "keyup", this._checkKeyUp), this.defaults = { selectedClass: "sortable-selected", multiDragKey: null, avoidImplicitDeselect: false, setData: function(t4, e2) {
              var n2 = "";
              ce.length && re === o2 ? ce.forEach(function(t5, e3) {
                n2 += (e3 ? ", " : "") + t5.textContent;
              }) : n2 = e2.textContent, t4.setData("Text", n2);
            } };
          }
          return t2.prototype = { multiDragKeyDown: false, isMultiDrag: false, delayStartGlobal: function(t3) {
            t3 = t3.dragEl;
            ae = t3;
          }, delayEnded: function() {
            this.isMultiDrag = ~ce.indexOf(ae);
          }, setupClone: function(t3) {
            var e2 = t3.sortable, t3 = t3.cancel;
            if (this.isMultiDrag) {
              for (var n2 = 0; n2 < ce.length; n2++)
                ue.push(_(ce[n2])), ue[n2].sortableIndex = ce[n2].sortableIndex, ue[n2].draggable = false, ue[n2].style["will-change"] = "", I(ue[n2], this.options.selectedClass, false), ce[n2] === ae && I(ue[n2], this.options.chosenClass, false);
              e2._hideClone(), t3();
            }
          }, clone: function(t3) {
            var e2 = t3.sortable, n2 = t3.rootEl, o2 = t3.dispatchSortableEvent, t3 = t3.cancel;
            this.isMultiDrag && (this.options.removeCloneOnHide || ce.length && re === e2 && (pe(true, n2), o2("clone"), t3()));
          }, showClone: function(t3) {
            var e2 = t3.cloneNowShown, n2 = t3.rootEl, t3 = t3.cancel;
            this.isMultiDrag && (pe(false, n2), ue.forEach(function(t4) {
              P(t4, "display", "");
            }), e2(), se = false, t3());
          }, hideClone: function(t3) {
            var e2 = this, n2 = (t3.sortable, t3.cloneNowHidden), t3 = t3.cancel;
            this.isMultiDrag && (ue.forEach(function(t4) {
              P(t4, "display", "none"), e2.options.removeCloneOnHide && t4.parentNode && t4.parentNode.removeChild(t4);
            }), n2(), se = true, t3());
          }, dragStartGlobal: function(t3) {
            t3.sortable;
            !this.isMultiDrag && re && re.multiDrag._deselectMultiDrag(), ce.forEach(function(t4) {
              t4.sortableIndex = B(t4);
            }), ce = ce.sort(function(t4, e2) {
              return t4.sortableIndex - e2.sortableIndex;
            }), fe = true;
          }, dragStarted: function(t3) {
            var e2, n2 = this, t3 = t3.sortable;
            this.isMultiDrag && (this.options.sort && (t3.captureAnimationState(), this.options.animation && (ce.forEach(function(t4) {
              t4 !== ae && P(t4, "position", "absolute");
            }), e2 = k(ae, false, true, true), ce.forEach(function(t4) {
              t4 !== ae && C(t4, e2);
            }), de = he = true)), t3.animateAll(function() {
              de = he = false, n2.options.animation && ce.forEach(function(t4) {
                T(t4);
              }), n2.options.sort && ge();
            }));
          }, dragOver: function(t3) {
            var e2 = t3.target, n2 = t3.completed, t3 = t3.cancel;
            he && ~ce.indexOf(e2) && (n2(false), t3());
          }, revert: function(t3) {
            var n2, o2, e2 = t3.fromSortable, i2 = t3.rootEl, r2 = t3.sortable, a2 = t3.dragRect;
            1 < ce.length && (ce.forEach(function(t4) {
              r2.addAnimationState({ target: t4, rect: he ? k(t4) : a2 }), T(t4), t4.fromRect = a2, e2.removeAnimationState(t4);
            }), he = false, n2 = !this.options.removeCloneOnHide, o2 = i2, ce.forEach(function(t4, e3) {
              e3 = o2.children[t4.sortableIndex + (n2 ? Number(e3) : 0)];
              e3 ? o2.insertBefore(t4, e3) : o2.appendChild(t4);
            }));
          }, dragOverCompleted: function(t3) {
            var e2, n2 = t3.sortable, o2 = t3.isOwner, i2 = t3.insertion, r2 = t3.activeSortable, a2 = t3.parentEl, l2 = t3.putSortable, t3 = this.options;
            i2 && (o2 && r2._hideClone(), de = false, t3.animation && 1 < ce.length && (he || !o2 && !r2.options.sort && !l2) && (e2 = k(ae, false, true, true), ce.forEach(function(t4) {
              t4 !== ae && (C(t4, e2), a2.appendChild(t4));
            }), he = true), o2 || (he || ge(), 1 < ce.length ? (o2 = se, r2._showClone(n2), r2.options.animation && !se && o2 && ue.forEach(function(t4) {
              r2.addAnimationState({ target: t4, rect: le }), t4.fromRect = le, t4.thisAnimationDuration = null;
            })) : r2._showClone(n2)));
          }, dragOverAnimationCapture: function(t3) {
            var e2 = t3.dragRect, n2 = t3.isOwner, t3 = t3.activeSortable;
            ce.forEach(function(t4) {
              t4.thisAnimationDuration = null;
            }), t3.options.animation && !n2 && t3.multiDrag.isMultiDrag && (le = a({}, e2), e2 = v(ae, true), le.top -= e2.f, le.left -= e2.e);
          }, dragOverAnimationComplete: function() {
            he && (he = false, ge());
          }, drop: function(t3) {
            var e2 = t3.originalEvent, n2 = t3.rootEl, o2 = t3.parentEl, i2 = t3.sortable, r2 = t3.dispatchSortableEvent, a2 = t3.oldIndex, l2 = t3.putSortable, s2 = l2 || this.sortable;
            if (e2) {
              var c2, u2, d2, h2 = this.options, f2 = o2.children;
              if (!fe)
                if (h2.multiDragKey && !this.multiDragKeyDown && this._deselectMultiDrag(), I(ae, h2.selectedClass, !~ce.indexOf(ae)), ~ce.indexOf(ae))
                  ce.splice(ce.indexOf(ae), 1), ie = null, W({ sortable: i2, rootEl: n2, name: "deselect", targetEl: ae, originalEvent: e2 });
                else {
                  if (ce.push(ae), W({ sortable: i2, rootEl: n2, name: "select", targetEl: ae, originalEvent: e2 }), e2.shiftKey && ie && i2.el.contains(ie)) {
                    var p2 = B(ie), t3 = B(ae);
                    if (~p2 && ~t3 && p2 !== t3)
                      for (var g2, m2 = p2 < t3 ? (g2 = p2, t3) : (g2 = t3, p2 + 1); g2 < m2; g2++)
                        ~ce.indexOf(f2[g2]) || (I(f2[g2], h2.selectedClass, true), ce.push(f2[g2]), W({ sortable: i2, rootEl: n2, name: "select", targetEl: f2[g2], originalEvent: e2 }));
                  } else
                    ie = ae;
                  re = s2;
                }
              fe && this.isMultiDrag && (he = false, (o2[j].options.sort || o2 !== n2) && 1 < ce.length && (c2 = k(ae), u2 = B(ae, ":not(." + this.options.selectedClass + ")"), !de && h2.animation && (ae.thisAnimationDuration = null), s2.captureAnimationState(), de || (h2.animation && (ae.fromRect = c2, ce.forEach(function(t4) {
                var e3;
                t4.thisAnimationDuration = null, t4 !== ae && (e3 = he ? k(t4) : c2, t4.fromRect = e3, s2.addAnimationState({ target: t4, rect: e3 }));
              })), ge(), ce.forEach(function(t4) {
                f2[u2] ? o2.insertBefore(t4, f2[u2]) : o2.appendChild(t4), u2++;
              }), a2 === B(ae) && (d2 = false, ce.forEach(function(t4) {
                t4.sortableIndex !== B(t4) && (d2 = true);
              }), d2 && r2("update"))), ce.forEach(function(t4) {
                T(t4);
              }), s2.animateAll()), re = s2), (n2 === o2 || l2 && "clone" !== l2.lastPutMode) && ue.forEach(function(t4) {
                t4.parentNode && t4.parentNode.removeChild(t4);
              });
            }
          }, nullingGlobal: function() {
            this.isMultiDrag = fe = false, ue.length = 0;
          }, destroyGlobal: function() {
            this._deselectMultiDrag(), f(document, "pointerup", this._deselectMultiDrag), f(document, "mouseup", this._deselectMultiDrag), f(document, "touchend", this._deselectMultiDrag), f(document, "keydown", this._checkKeyDown), f(document, "keyup", this._checkKeyUp);
          }, _deselectMultiDrag: function(t3) {
            if (!(void 0 !== fe && fe || re !== this.sortable || t3 && N(t3.target, this.options.draggable, this.sortable.el, false) || t3 && 0 !== t3.button))
              for (; ce.length; ) {
                var e2 = ce[0];
                I(e2, this.options.selectedClass, false), ce.shift(), W({ sortable: this.sortable, rootEl: this.sortable.el, name: "deselect", targetEl: e2, originalEvent: t3 });
              }
          }, _checkKeyDown: function(t3) {
            t3.key === this.options.multiDragKey && (this.multiDragKeyDown = true);
          }, _checkKeyUp: function(t3) {
            t3.key === this.options.multiDragKey && (this.multiDragKeyDown = false);
          } }, a(t2, { pluginName: "multiDrag", utils: { select: function(t3) {
            var e2 = t3.parentNode[j];
            e2 && e2.options.multiDrag && !~ce.indexOf(t3) && (re && re !== e2 && (re.multiDrag._deselectMultiDrag(), re = e2), I(t3, e2.options.selectedClass, true), ce.push(t3));
          }, deselect: function(t3) {
            var e2 = t3.parentNode[j], n2 = ce.indexOf(t3);
            e2 && e2.options.multiDrag && ~n2 && (I(t3, e2.options.selectedClass, false), ce.splice(n2, 1));
          } }, eventProperties: function() {
            var n2 = this, o2 = [], i2 = [];
            return ce.forEach(function(t3) {
              var e2;
              o2.push({ multiDragElement: t3, index: t3.sortableIndex }), e2 = he && t3 !== ae ? -1 : he ? B(t3, ":not(." + n2.options.selectedClass + ")") : B(t3), i2.push({ multiDragElement: t3, index: e2 });
            }), { items: r(ce), clones: [].concat(ue), oldIndicies: o2, newIndicies: i2 };
          }, optionListeners: { multiDragKey: function(t3) {
            return "ctrl" === (t3 = t3.toLowerCase()) ? t3 = "Control" : 1 < t3.length && (t3 = t3.charAt(0).toUpperCase() + t3.substr(1)), t3;
          } } });
        }()), Bt;
      });
    }
  });

  // node_modules/frappe-datatable/dist/frappe-datatable.cjs.js
  var require_frappe_datatable_cjs = __commonJS({
    "node_modules/frappe-datatable/dist/frappe-datatable.cjs.js"(exports, module) {
      "use strict";
      function _interopDefault(ex) {
        return ex && typeof ex === "object" && "default" in ex ? ex["default"] : ex;
      }
      var Sortable = _interopDefault(require_Sortable_min());
      function $2(expr, con) {
        return typeof expr === "string" ? (con || document).querySelector(expr) : expr || null;
      }
      $2.each = (expr, con) => {
        return typeof expr === "string" ? Array.from((con || document).querySelectorAll(expr)) : expr || null;
      };
      $2.create = (tag, o) => {
        let element = document.createElement(tag);
        for (let i in o) {
          let val = o[i];
          if (i === "inside") {
            $2(val).appendChild(element);
          } else if (i === "around") {
            let ref = $2(val);
            ref.parentNode.insertBefore(element, ref);
            element.appendChild(ref);
          } else if (i === "styles") {
            if (typeof val === "object") {
              Object.keys(val).map((prop) => {
                element.style[prop] = val[prop];
              });
            }
          } else if (i in element) {
            element[i] = val;
          } else {
            element.setAttribute(i, val);
          }
        }
        return element;
      };
      $2.on = (element, event, selector, callback) => {
        if (!callback) {
          callback = selector;
          $2.bind(element, event, callback);
        } else {
          $2.delegate(element, event, selector, callback);
        }
      };
      $2.off = (element, event, handler) => {
        element.removeEventListener(event, handler);
      };
      $2.bind = (element, event, callback) => {
        event.split(/\s+/).forEach(function(event2) {
          element.addEventListener(event2, callback);
        });
      };
      $2.delegate = (element, event, selector, callback) => {
        element.addEventListener(event, function(e) {
          const delegatedTarget = e.target.closest(selector);
          if (delegatedTarget) {
            e.delegatedTarget = delegatedTarget;
            callback.call(this, e, delegatedTarget);
          }
        });
      };
      $2.unbind = (element, o) => {
        if (element) {
          for (let event in o) {
            let callback = o[event];
            event.split(/\s+/).forEach(function(event2) {
              element.removeEventListener(event2, callback);
            });
          }
        }
      };
      $2.fire = (target, type, properties) => {
        let evt = document.createEvent("HTMLEvents");
        evt.initEvent(type, true, true);
        for (let j in properties) {
          evt[j] = properties[j];
        }
        return target.dispatchEvent(evt);
      };
      $2.data = (element, attrs) => {
        if (!attrs) {
          return element.dataset;
        }
        for (const attr in attrs) {
          element.dataset[attr] = attrs[attr];
        }
      };
      $2.style = (elements, styleMap) => {
        if (typeof styleMap === "string") {
          return $2.getStyle(elements, styleMap);
        }
        if (!Array.isArray(elements)) {
          elements = [elements];
        }
        elements.map((element) => {
          for (const prop in styleMap) {
            element.style[prop] = styleMap[prop];
          }
        });
      };
      $2.removeStyle = (elements, styleProps) => {
        if (!Array.isArray(elements)) {
          elements = [elements];
        }
        if (!Array.isArray(styleProps)) {
          styleProps = [styleProps];
        }
        elements.map((element) => {
          for (const prop of styleProps) {
            element.style[prop] = "";
          }
        });
      };
      $2.getStyle = (element, prop) => {
        if (!prop) {
          return getComputedStyle(element);
        }
        let val = getComputedStyle(element)[prop];
        if (["width", "height"].includes(prop)) {
          val = parseFloat(val);
        }
        return val;
      };
      $2.closest = (selector, element) => {
        if (!element)
          return null;
        if (element.matches(selector)) {
          return element;
        }
        return $2.closest(selector, element.parentNode);
      };
      $2.inViewport = (el, parentEl) => {
        const {
          top,
          left,
          bottom,
          right
        } = el.getBoundingClientRect();
        const {
          top: pTop,
          left: pLeft,
          bottom: pBottom,
          right: pRight
        } = parentEl.getBoundingClientRect();
        return top >= pTop && left >= pLeft && bottom <= pBottom && right <= pRight;
      };
      $2.scrollTop = function scrollTop(element, pixels) {
        requestAnimationFrame(() => {
          element.scrollTop = pixels;
        });
      };
      $2.scrollbarSize = function scrollbarSize() {
        if (!$2.scrollBarSizeValue) {
          $2.scrollBarSizeValue = getScrollBarSize();
        }
        return $2.scrollBarSizeValue;
      };
      function getScrollBarSize() {
        const scrollDiv = document.createElement("div");
        $2.style(scrollDiv, {
          width: "100px",
          height: "100px",
          overflow: "scroll",
          position: "absolute",
          top: "-9999px"
        });
        document.body.appendChild(scrollDiv);
        const scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;
        document.body.removeChild(scrollDiv);
        return scrollbarWidth;
      }
      $2.hasVerticalOverflow = function(element) {
        return element.scrollHeight > element.offsetHeight + 10;
      };
      $2.hasHorizontalOverflow = function(element) {
        return element.scrollWidth > element.offsetWidth + 10;
      };
      $2.measureTextWidth = function(text) {
        const div = document.createElement("div");
        div.style.position = "absolute";
        div.style.visibility = "hidden";
        div.style.height = "auto";
        div.style.width = "auto";
        div.style.whiteSpace = "nowrap";
        div.innerText = text;
        document.body.appendChild(div);
        return div.clientWidth + 1;
      };
      function isObject(value) {
        var type = typeof value;
        return value != null && (type == "object" || type == "function");
      }
      var isObject_1 = isObject;
      var commonjsGlobal = typeof window !== "undefined" ? window : typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : {};
      function commonjsRequire() {
        throw new Error("Dynamic requires are not currently supported by rollup-plugin-commonjs");
      }
      function unwrapExports(x) {
        return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
      }
      function createCommonjsModule(fn, module2) {
        return module2 = { exports: {} }, fn(module2, module2.exports), module2.exports;
      }
      var freeGlobal = typeof commonjsGlobal == "object" && commonjsGlobal && commonjsGlobal.Object === Object && commonjsGlobal;
      var _freeGlobal = freeGlobal;
      var freeSelf = typeof self == "object" && self && self.Object === Object && self;
      var root = _freeGlobal || freeSelf || Function("return this")();
      var _root = root;
      var now = function() {
        return _root.Date.now();
      };
      var now_1 = now;
      var Symbol2 = _root.Symbol;
      var _Symbol = Symbol2;
      var objectProto = Object.prototype;
      var hasOwnProperty = objectProto.hasOwnProperty;
      var nativeObjectToString = objectProto.toString;
      var symToStringTag = _Symbol ? _Symbol.toStringTag : void 0;
      function getRawTag(value) {
        var isOwn = hasOwnProperty.call(value, symToStringTag), tag = value[symToStringTag];
        try {
          value[symToStringTag] = void 0;
        } catch (e) {
        }
        var result = nativeObjectToString.call(value);
        {
          if (isOwn) {
            value[symToStringTag] = tag;
          } else {
            delete value[symToStringTag];
          }
        }
        return result;
      }
      var _getRawTag = getRawTag;
      var objectProto$1 = Object.prototype;
      var nativeObjectToString$1 = objectProto$1.toString;
      function objectToString(value) {
        return nativeObjectToString$1.call(value);
      }
      var _objectToString = objectToString;
      var nullTag = "[object Null]";
      var undefinedTag = "[object Undefined]";
      var symToStringTag$1 = _Symbol ? _Symbol.toStringTag : void 0;
      function baseGetTag(value) {
        if (value == null) {
          return value === void 0 ? undefinedTag : nullTag;
        }
        return symToStringTag$1 && symToStringTag$1 in Object(value) ? _getRawTag(value) : _objectToString(value);
      }
      var _baseGetTag = baseGetTag;
      function isObjectLike(value) {
        return value != null && typeof value == "object";
      }
      var isObjectLike_1 = isObjectLike;
      var symbolTag = "[object Symbol]";
      function isSymbol(value) {
        return typeof value == "symbol" || isObjectLike_1(value) && _baseGetTag(value) == symbolTag;
      }
      var isSymbol_1 = isSymbol;
      var NAN = 0 / 0;
      var reTrim = /^\s+|\s+$/g;
      var reIsBadHex = /^[-+]0x[0-9a-f]+$/i;
      var reIsBinary = /^0b[01]+$/i;
      var reIsOctal = /^0o[0-7]+$/i;
      var freeParseInt = parseInt;
      function toNumber(value) {
        if (typeof value == "number") {
          return value;
        }
        if (isSymbol_1(value)) {
          return NAN;
        }
        if (isObject_1(value)) {
          var other = typeof value.valueOf == "function" ? value.valueOf() : value;
          value = isObject_1(other) ? other + "" : other;
        }
        if (typeof value != "string") {
          return value === 0 ? value : +value;
        }
        value = value.replace(reTrim, "");
        var isBinary = reIsBinary.test(value);
        return isBinary || reIsOctal.test(value) ? freeParseInt(value.slice(2), isBinary ? 2 : 8) : reIsBadHex.test(value) ? NAN : +value;
      }
      var toNumber_1 = toNumber;
      var FUNC_ERROR_TEXT = "Expected a function";
      var nativeMax = Math.max;
      var nativeMin = Math.min;
      function debounce(func, wait, options) {
        var lastArgs, lastThis, maxWait, result, timerId, lastCallTime, lastInvokeTime = 0, leading = false, maxing = false, trailing = true;
        if (typeof func != "function") {
          throw new TypeError(FUNC_ERROR_TEXT);
        }
        wait = toNumber_1(wait) || 0;
        if (isObject_1(options)) {
          leading = !!options.leading;
          maxing = "maxWait" in options;
          maxWait = maxing ? nativeMax(toNumber_1(options.maxWait) || 0, wait) : maxWait;
          trailing = "trailing" in options ? !!options.trailing : trailing;
        }
        function invokeFunc(time) {
          var args = lastArgs, thisArg = lastThis;
          lastArgs = lastThis = void 0;
          lastInvokeTime = time;
          result = func.apply(thisArg, args);
          return result;
        }
        function leadingEdge(time) {
          lastInvokeTime = time;
          timerId = setTimeout(timerExpired, wait);
          return leading ? invokeFunc(time) : result;
        }
        function remainingWait(time) {
          var timeSinceLastCall = time - lastCallTime, timeSinceLastInvoke = time - lastInvokeTime, timeWaiting = wait - timeSinceLastCall;
          return maxing ? nativeMin(timeWaiting, maxWait - timeSinceLastInvoke) : timeWaiting;
        }
        function shouldInvoke(time) {
          var timeSinceLastCall = time - lastCallTime, timeSinceLastInvoke = time - lastInvokeTime;
          return lastCallTime === void 0 || timeSinceLastCall >= wait || timeSinceLastCall < 0 || maxing && timeSinceLastInvoke >= maxWait;
        }
        function timerExpired() {
          var time = now_1();
          if (shouldInvoke(time)) {
            return trailingEdge(time);
          }
          timerId = setTimeout(timerExpired, remainingWait(time));
        }
        function trailingEdge(time) {
          timerId = void 0;
          if (trailing && lastArgs) {
            return invokeFunc(time);
          }
          lastArgs = lastThis = void 0;
          return result;
        }
        function cancel() {
          if (timerId !== void 0) {
            clearTimeout(timerId);
          }
          lastInvokeTime = 0;
          lastArgs = lastCallTime = lastThis = timerId = void 0;
        }
        function flush() {
          return timerId === void 0 ? result : trailingEdge(now_1());
        }
        function debounced() {
          var time = now_1(), isInvoking = shouldInvoke(time);
          lastArgs = arguments;
          lastThis = this;
          lastCallTime = time;
          if (isInvoking) {
            if (timerId === void 0) {
              return leadingEdge(lastCallTime);
            }
            if (maxing) {
              timerId = setTimeout(timerExpired, wait);
              return invokeFunc(lastCallTime);
            }
          }
          if (timerId === void 0) {
            timerId = setTimeout(timerExpired, wait);
          }
          return result;
        }
        debounced.cancel = cancel;
        debounced.flush = flush;
        return debounced;
      }
      var debounce_1 = debounce;
      var FUNC_ERROR_TEXT$1 = "Expected a function";
      function throttle(func, wait, options) {
        var leading = true, trailing = true;
        if (typeof func != "function") {
          throw new TypeError(FUNC_ERROR_TEXT$1);
        }
        if (isObject_1(options)) {
          leading = "leading" in options ? !!options.leading : leading;
          trailing = "trailing" in options ? !!options.trailing : trailing;
        }
        return debounce_1(func, wait, {
          "leading": leading,
          "maxWait": wait,
          "trailing": trailing
        });
      }
      var throttle_1 = throttle;
      var asyncTag = "[object AsyncFunction]";
      var funcTag = "[object Function]";
      var genTag = "[object GeneratorFunction]";
      var proxyTag = "[object Proxy]";
      function isFunction(value) {
        if (!isObject_1(value)) {
          return false;
        }
        var tag = _baseGetTag(value);
        return tag == funcTag || tag == genTag || tag == asyncTag || tag == proxyTag;
      }
      var isFunction_1 = isFunction;
      var coreJsData = _root["__core-js_shared__"];
      var _coreJsData = coreJsData;
      var maskSrcKey = function() {
        var uid = /[^.]+$/.exec(_coreJsData && _coreJsData.keys && _coreJsData.keys.IE_PROTO || "");
        return uid ? "Symbol(src)_1." + uid : "";
      }();
      function isMasked(func) {
        return !!maskSrcKey && maskSrcKey in func;
      }
      var _isMasked = isMasked;
      var funcProto = Function.prototype;
      var funcToString = funcProto.toString;
      function toSource(func) {
        if (func != null) {
          try {
            return funcToString.call(func);
          } catch (e) {
          }
          try {
            return func + "";
          } catch (e) {
          }
        }
        return "";
      }
      var _toSource = toSource;
      var reRegExpChar = /[\\^$.*+?()[\]{}|]/g;
      var reIsHostCtor = /^\[object .+?Constructor\]$/;
      var funcProto$1 = Function.prototype;
      var objectProto$2 = Object.prototype;
      var funcToString$1 = funcProto$1.toString;
      var hasOwnProperty$1 = objectProto$2.hasOwnProperty;
      var reIsNative = RegExp(
        "^" + funcToString$1.call(hasOwnProperty$1).replace(reRegExpChar, "\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g, "$1.*?") + "$"
      );
      function baseIsNative(value) {
        if (!isObject_1(value) || _isMasked(value)) {
          return false;
        }
        var pattern = isFunction_1(value) ? reIsNative : reIsHostCtor;
        return pattern.test(_toSource(value));
      }
      var _baseIsNative = baseIsNative;
      function getValue(object, key) {
        return object == null ? void 0 : object[key];
      }
      var _getValue = getValue;
      function getNative(object, key) {
        var value = _getValue(object, key);
        return _baseIsNative(value) ? value : void 0;
      }
      var _getNative = getNative;
      var nativeCreate = _getNative(Object, "create");
      var _nativeCreate = nativeCreate;
      function hashClear() {
        this.__data__ = _nativeCreate ? _nativeCreate(null) : {};
        this.size = 0;
      }
      var _hashClear = hashClear;
      function hashDelete(key) {
        var result = this.has(key) && delete this.__data__[key];
        this.size -= result ? 1 : 0;
        return result;
      }
      var _hashDelete = hashDelete;
      var HASH_UNDEFINED = "__lodash_hash_undefined__";
      var objectProto$3 = Object.prototype;
      var hasOwnProperty$2 = objectProto$3.hasOwnProperty;
      function hashGet(key) {
        var data = this.__data__;
        if (_nativeCreate) {
          var result = data[key];
          return result === HASH_UNDEFINED ? void 0 : result;
        }
        return hasOwnProperty$2.call(data, key) ? data[key] : void 0;
      }
      var _hashGet = hashGet;
      var objectProto$4 = Object.prototype;
      var hasOwnProperty$3 = objectProto$4.hasOwnProperty;
      function hashHas(key) {
        var data = this.__data__;
        return _nativeCreate ? data[key] !== void 0 : hasOwnProperty$3.call(data, key);
      }
      var _hashHas = hashHas;
      var HASH_UNDEFINED$1 = "__lodash_hash_undefined__";
      function hashSet(key, value) {
        var data = this.__data__;
        this.size += this.has(key) ? 0 : 1;
        data[key] = _nativeCreate && value === void 0 ? HASH_UNDEFINED$1 : value;
        return this;
      }
      var _hashSet = hashSet;
      function Hash(entries) {
        var index = -1, length = entries == null ? 0 : entries.length;
        this.clear();
        while (++index < length) {
          var entry = entries[index];
          this.set(entry[0], entry[1]);
        }
      }
      Hash.prototype.clear = _hashClear;
      Hash.prototype["delete"] = _hashDelete;
      Hash.prototype.get = _hashGet;
      Hash.prototype.has = _hashHas;
      Hash.prototype.set = _hashSet;
      var _Hash = Hash;
      function listCacheClear() {
        this.__data__ = [];
        this.size = 0;
      }
      var _listCacheClear = listCacheClear;
      function eq(value, other) {
        return value === other || value !== value && other !== other;
      }
      var eq_1 = eq;
      function assocIndexOf(array, key) {
        var length = array.length;
        while (length--) {
          if (eq_1(array[length][0], key)) {
            return length;
          }
        }
        return -1;
      }
      var _assocIndexOf = assocIndexOf;
      var arrayProto = Array.prototype;
      var splice = arrayProto.splice;
      function listCacheDelete(key) {
        var data = this.__data__, index = _assocIndexOf(data, key);
        if (index < 0) {
          return false;
        }
        var lastIndex = data.length - 1;
        if (index == lastIndex) {
          data.pop();
        } else {
          splice.call(data, index, 1);
        }
        --this.size;
        return true;
      }
      var _listCacheDelete = listCacheDelete;
      function listCacheGet(key) {
        var data = this.__data__, index = _assocIndexOf(data, key);
        return index < 0 ? void 0 : data[index][1];
      }
      var _listCacheGet = listCacheGet;
      function listCacheHas(key) {
        return _assocIndexOf(this.__data__, key) > -1;
      }
      var _listCacheHas = listCacheHas;
      function listCacheSet(key, value) {
        var data = this.__data__, index = _assocIndexOf(data, key);
        if (index < 0) {
          ++this.size;
          data.push([key, value]);
        } else {
          data[index][1] = value;
        }
        return this;
      }
      var _listCacheSet = listCacheSet;
      function ListCache(entries) {
        var index = -1, length = entries == null ? 0 : entries.length;
        this.clear();
        while (++index < length) {
          var entry = entries[index];
          this.set(entry[0], entry[1]);
        }
      }
      ListCache.prototype.clear = _listCacheClear;
      ListCache.prototype["delete"] = _listCacheDelete;
      ListCache.prototype.get = _listCacheGet;
      ListCache.prototype.has = _listCacheHas;
      ListCache.prototype.set = _listCacheSet;
      var _ListCache = ListCache;
      var Map = _getNative(_root, "Map");
      var _Map = Map;
      function mapCacheClear() {
        this.size = 0;
        this.__data__ = {
          "hash": new _Hash(),
          "map": new (_Map || _ListCache)(),
          "string": new _Hash()
        };
      }
      var _mapCacheClear = mapCacheClear;
      function isKeyable(value) {
        var type = typeof value;
        return type == "string" || type == "number" || type == "symbol" || type == "boolean" ? value !== "__proto__" : value === null;
      }
      var _isKeyable = isKeyable;
      function getMapData(map, key) {
        var data = map.__data__;
        return _isKeyable(key) ? data[typeof key == "string" ? "string" : "hash"] : data.map;
      }
      var _getMapData = getMapData;
      function mapCacheDelete(key) {
        var result = _getMapData(this, key)["delete"](key);
        this.size -= result ? 1 : 0;
        return result;
      }
      var _mapCacheDelete = mapCacheDelete;
      function mapCacheGet(key) {
        return _getMapData(this, key).get(key);
      }
      var _mapCacheGet = mapCacheGet;
      function mapCacheHas(key) {
        return _getMapData(this, key).has(key);
      }
      var _mapCacheHas = mapCacheHas;
      function mapCacheSet(key, value) {
        var data = _getMapData(this, key), size = data.size;
        data.set(key, value);
        this.size += data.size == size ? 0 : 1;
        return this;
      }
      var _mapCacheSet = mapCacheSet;
      function MapCache(entries) {
        var index = -1, length = entries == null ? 0 : entries.length;
        this.clear();
        while (++index < length) {
          var entry = entries[index];
          this.set(entry[0], entry[1]);
        }
      }
      MapCache.prototype.clear = _mapCacheClear;
      MapCache.prototype["delete"] = _mapCacheDelete;
      MapCache.prototype.get = _mapCacheGet;
      MapCache.prototype.has = _mapCacheHas;
      MapCache.prototype.set = _mapCacheSet;
      var _MapCache = MapCache;
      var HASH_UNDEFINED$2 = "__lodash_hash_undefined__";
      function setCacheAdd(value) {
        this.__data__.set(value, HASH_UNDEFINED$2);
        return this;
      }
      var _setCacheAdd = setCacheAdd;
      function setCacheHas(value) {
        return this.__data__.has(value);
      }
      var _setCacheHas = setCacheHas;
      function SetCache(values) {
        var index = -1, length = values == null ? 0 : values.length;
        this.__data__ = new _MapCache();
        while (++index < length) {
          this.add(values[index]);
        }
      }
      SetCache.prototype.add = SetCache.prototype.push = _setCacheAdd;
      SetCache.prototype.has = _setCacheHas;
      var _SetCache = SetCache;
      function baseFindIndex(array, predicate, fromIndex, fromRight) {
        var length = array.length, index = fromIndex + (fromRight ? 1 : -1);
        while (fromRight ? index-- : ++index < length) {
          if (predicate(array[index], index, array)) {
            return index;
          }
        }
        return -1;
      }
      var _baseFindIndex = baseFindIndex;
      function baseIsNaN(value) {
        return value !== value;
      }
      var _baseIsNaN = baseIsNaN;
      function strictIndexOf(array, value, fromIndex) {
        var index = fromIndex - 1, length = array.length;
        while (++index < length) {
          if (array[index] === value) {
            return index;
          }
        }
        return -1;
      }
      var _strictIndexOf = strictIndexOf;
      function baseIndexOf(array, value, fromIndex) {
        return value === value ? _strictIndexOf(array, value, fromIndex) : _baseFindIndex(array, _baseIsNaN, fromIndex);
      }
      var _baseIndexOf = baseIndexOf;
      function arrayIncludes(array, value) {
        var length = array == null ? 0 : array.length;
        return !!length && _baseIndexOf(array, value, 0) > -1;
      }
      var _arrayIncludes = arrayIncludes;
      function arrayIncludesWith(array, value, comparator) {
        var index = -1, length = array == null ? 0 : array.length;
        while (++index < length) {
          if (comparator(value, array[index])) {
            return true;
          }
        }
        return false;
      }
      var _arrayIncludesWith = arrayIncludesWith;
      function cacheHas(cache, key) {
        return cache.has(key);
      }
      var _cacheHas = cacheHas;
      var Set$1 = _getNative(_root, "Set");
      var _Set = Set$1;
      function noop() {
      }
      var noop_1 = noop;
      function setToArray(set) {
        var index = -1, result = Array(set.size);
        set.forEach(function(value) {
          result[++index] = value;
        });
        return result;
      }
      var _setToArray = setToArray;
      var INFINITY = 1 / 0;
      var createSet = !(_Set && 1 / _setToArray(new _Set([, -0]))[1] == INFINITY) ? noop_1 : function(values) {
        return new _Set(values);
      };
      var _createSet = createSet;
      var LARGE_ARRAY_SIZE = 200;
      function baseUniq(array, iteratee, comparator) {
        var index = -1, includes = _arrayIncludes, length = array.length, isCommon = true, result = [], seen = result;
        if (comparator) {
          isCommon = false;
          includes = _arrayIncludesWith;
        } else if (length >= LARGE_ARRAY_SIZE) {
          var set = iteratee ? null : _createSet(array);
          if (set) {
            return _setToArray(set);
          }
          isCommon = false;
          includes = _cacheHas;
          seen = new _SetCache();
        } else {
          seen = iteratee ? [] : result;
        }
        outer:
          while (++index < length) {
            var value = array[index], computed = iteratee ? iteratee(value) : value;
            value = comparator || value !== 0 ? value : 0;
            if (isCommon && computed === computed) {
              var seenIndex = seen.length;
              while (seenIndex--) {
                if (seen[seenIndex] === computed) {
                  continue outer;
                }
              }
              if (iteratee) {
                seen.push(computed);
              }
              result.push(value);
            } else if (!includes(seen, computed, comparator)) {
              if (seen !== result) {
                seen.push(computed);
              }
              result.push(value);
            }
          }
        return result;
      }
      var _baseUniq = baseUniq;
      function uniq(array) {
        return array && array.length ? _baseUniq(array) : [];
      }
      var uniq_1 = uniq;
      function camelCaseToDash(str) {
        return str.replace(/([A-Z])/g, (g) => `-${g[0].toLowerCase()}`);
      }
      function makeDataAttributeString(props) {
        const keys = Object.keys(props);
        return keys.map((key) => {
          const _key = camelCaseToDash(key);
          const val = props[key];
          if (val === void 0)
            return "";
          return `data-${_key}="${val}" `;
        }).join("").trim();
      }
      function copyTextToClipboard(text) {
        var textArea = document.createElement("textarea");
        textArea.style.position = "fixed";
        textArea.style.top = 0;
        textArea.style.left = 0;
        textArea.style.width = "2em";
        textArea.style.height = "2em";
        textArea.style.padding = 0;
        textArea.style.border = "none";
        textArea.style.outline = "none";
        textArea.style.boxShadow = "none";
        textArea.style.background = "transparent";
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        try {
          document.execCommand("copy");
        } catch (err) {
          console.log("Oops, unable to copy");
        }
        document.body.removeChild(textArea);
      }
      function isNumeric(val) {
        return !isNaN(val);
      }
      var throttle$1 = throttle_1;
      var debounce$1 = debounce_1;
      function nextTick(fn, context = null) {
        return (...args) => {
          return new Promise((resolve) => {
            const execute = () => {
              const out = fn.apply(context, args);
              resolve(out);
            };
            setTimeout(execute);
          });
        };
      }
      function linkProperties(target, source, properties) {
        const props = properties.reduce((acc, prop) => {
          acc[prop] = {
            get() {
              return source[prop];
            }
          };
          return acc;
        }, {});
        Object.defineProperties(target, props);
      }
      function isSet(val) {
        return val !== void 0 || val !== null;
      }
      function notSet(val) {
        return !isSet(val);
      }
      function isNumber(val) {
        return !isNaN(val);
      }
      function ensureArray(val) {
        if (!Array.isArray(val)) {
          return [val];
        }
        return val;
      }
      function uniq$1(arr) {
        return uniq_1(arr);
      }
      function numberSortAsc(a, b) {
        return a - b;
      }
      function stripHTML(html) {
        return html.replace(/<[^>]*>/g, "");
      }
      function format(str, args) {
        if (!str)
          return str;
        Object.keys(args).forEach((arg) => {
          let regex = new RegExp(`{(${arg})}`, "g");
          str = str.replace(regex, args[arg]);
        });
        return str;
      }
      function escapeHTML(txt) {
        if (!txt)
          return "";
        let escapeHtmlMapping = {
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
          "/": "&#x2F;",
          "`": "&#x60;",
          "=": "&#x3D;"
        };
        return String(txt).replace(/[&<>"'`=/]/g, (char) => escapeHtmlMapping[char] || char);
      }
      var DataManager = class {
        constructor(options) {
          this.options = options;
          this.sortRows = nextTick(this.sortRows, this);
          this.switchColumn = nextTick(this.switchColumn, this);
          this.removeColumn = nextTick(this.removeColumn, this);
          this.options.filterRows = nextTick(this.options.filterRows, this);
        }
        init(data, columns) {
          if (!data) {
            data = this.options.data;
          }
          if (columns) {
            this.options.columns = columns;
          }
          this.data = data;
          this.rowCount = 0;
          this.columns = [];
          this.rows = [];
          this.prepareColumns();
          this.validateData(this.data);
          this.rows = this.prepareRows(this.data);
          this.prepareTreeRows();
          this.prepareRowView();
          this.prepareNumericColumns();
        }
        get currentSort() {
          const col = this.columns.find((col2) => col2.sortOrder !== "none");
          return col || {
            colIndex: -1,
            sortOrder: "none"
          };
        }
        prepareColumns() {
          this.columns = [];
          this.validateColumns();
          this.prepareDefaultColumns();
          this.prepareHeader();
        }
        prepareDefaultColumns() {
          if (this.options.checkboxColumn && !this.hasColumnById("_checkbox")) {
            const cell = {
              id: "_checkbox",
              content: this.getCheckboxHTML(),
              editable: false,
              resizable: false,
              sortable: false,
              focusable: false,
              dropdown: false,
              width: 32
            };
            this.columns.push(cell);
          }
          if (this.options.serialNoColumn && !this.hasColumnById("_rowIndex")) {
            let cell = {
              id: "_rowIndex",
              content: "",
              align: "center",
              editable: false,
              resizable: false,
              focusable: false,
              dropdown: false
            };
            this.columns.push(cell);
          }
        }
        prepareHeader() {
          let columns = this.columns.concat(this.options.columns);
          const baseCell = {
            isHeader: 1,
            editable: true,
            sortable: true,
            resizable: true,
            focusable: true,
            dropdown: true,
            width: null,
            format: (value) => {
              if (value === null || value === void 0) {
                return "";
              }
              return value + "";
            }
          };
          this.columns = columns.map((cell, i) => this.prepareCell(cell, i)).map((col) => Object.assign({}, baseCell, col)).map((col) => {
            col.content = col.content || col.name || "";
            col.id = col.id || col.content;
            return col;
          });
        }
        prepareCell(content, i) {
          const cell = {
            content: "",
            sortOrder: "none",
            colIndex: i,
            column: this.columns[i]
          };
          if (content !== null && typeof content === "object") {
            Object.assign(cell, content);
          } else {
            cell.content = content;
          }
          return cell;
        }
        prepareNumericColumns() {
          const row0 = this.getRow(0);
          if (!row0)
            return;
          this.columns = this.columns.map((column, i) => {
            const cellValue = row0[i].content;
            if (!column.align && isNumeric(cellValue)) {
              column.align = "right";
            }
            return column;
          });
        }
        prepareRows(data) {
          return data.map((d, i) => {
            const index = this._getNextRowCount();
            let row = [];
            let meta = {
              rowIndex: index
            };
            if (Array.isArray(d)) {
              if (this.options.checkboxColumn) {
                row.push(this.getCheckboxHTML());
              }
              if (this.options.serialNoColumn) {
                row.push(index + 1 + "");
              }
              row = row.concat(d);
              while (row.length < this.columns.length) {
                row.push("");
              }
            } else {
              for (let col of this.columns) {
                if (col.id === "_checkbox") {
                  row.push(this.getCheckboxHTML());
                } else if (col.id === "_rowIndex") {
                  row.push(index + 1 + "");
                } else {
                  row.push(d[col.id]);
                }
              }
              meta.indent = d.indent || 0;
            }
            return this.prepareRow(row, meta);
          });
        }
        prepareTreeRows() {
          this.rows.forEach((row, i) => {
            if (isNumber(row.meta.indent)) {
              const nextRow = this.getRow(i + 1);
              row.meta.isLeaf = !nextRow || notSet(nextRow.meta.indent) || nextRow.meta.indent <= row.meta.indent;
              row.meta.isTreeNodeClose = false;
            }
          });
        }
        prepareRowView() {
          this.rowViewOrder = this.rows.map((row) => row.meta.rowIndex);
        }
        prepareRow(row, meta) {
          const baseRowCell = {
            rowIndex: meta.rowIndex,
            indent: meta.indent
          };
          row = row.map((cell, i) => this.prepareCell(cell, i)).map((cell) => Object.assign({}, baseRowCell, cell));
          row.meta = meta;
          return row;
        }
        validateColumns() {
          const columns = this.options.columns;
          if (!Array.isArray(columns)) {
            throw new DataError("`columns` must be an array");
          }
          columns.forEach((column, i) => {
            if (typeof column !== "string" && typeof column !== "object") {
              throw new DataError(`column "${i}" must be a string or an object`);
            }
          });
        }
        validateData(data) {
          if (Array.isArray(data) && (data.length === 0 || Array.isArray(data[0]) || typeof data[0] === "object")) {
            return true;
          }
          throw new DataError("`data` must be an array of arrays or objects");
        }
        appendRows(rows) {
          this.validateData(rows);
          this.rows = this.rows.concat(this.prepareRows(rows));
          this.prepareTreeRows();
          this.prepareRowView();
        }
        sortRows(colIndex, sortOrder = "none") {
          colIndex = +colIndex;
          this.getColumns().map((col) => {
            if (col.colIndex === colIndex) {
              col.sortOrder = sortOrder;
            } else {
              col.sortOrder = "none";
            }
          });
          this._sortRows(colIndex, sortOrder);
        }
        _sortRows(colIndex, sortOrder) {
          if (this.currentSort.colIndex === colIndex) {
            if (this.currentSort.sortOrder === "asc" && sortOrder === "desc" || this.currentSort.sortOrder === "desc" && sortOrder === "asc") {
              this.reverseArray(this.rowViewOrder);
              this.currentSort.sortOrder = sortOrder;
              return;
            }
          }
          this.rowViewOrder.sort((a, b) => {
            const aIndex = a;
            const bIndex = b;
            let aContent = this.getCell(colIndex, a).content;
            let bContent = this.getCell(colIndex, b).content;
            aContent = aContent == null ? "" : aContent;
            bContent = bContent == null ? "" : bContent;
            if (sortOrder === "none") {
              return aIndex - bIndex;
            } else if (sortOrder === "asc") {
              if (aContent < bContent)
                return -1;
              if (aContent > bContent)
                return 1;
              if (aContent === bContent)
                return 0;
            } else if (sortOrder === "desc") {
              if (aContent < bContent)
                return 1;
              if (aContent > bContent)
                return -1;
              if (aContent === bContent)
                return 0;
            }
            return 0;
          });
          if (this.hasColumnById("_rowIndex")) {
            const srNoColIndex = this.getColumnIndexById("_rowIndex");
            this.rows.forEach((row, index) => {
              const viewIndex = this.rowViewOrder.indexOf(index);
              const cell = row[srNoColIndex];
              cell.content = viewIndex + 1 + "";
            });
          }
        }
        reverseArray(array) {
          let left = null;
          let right = null;
          let length = array.length;
          for (left = 0, right = length - 1; left < right; left += 1, right -= 1) {
            const temporary = array[left];
            array[left] = array[right];
            array[right] = temporary;
          }
        }
        switchColumn(index1, index2) {
          const temp = this.columns[index1];
          this.columns[index1] = this.columns[index2];
          this.columns[index2] = temp;
          this.columns[index1].colIndex = index1;
          this.columns[index2].colIndex = index2;
          this.rows.forEach((row) => {
            const newCell1 = Object.assign({}, row[index1], {
              colIndex: index2
            });
            const newCell2 = Object.assign({}, row[index2], {
              colIndex: index1
            });
            row[index2] = newCell1;
            row[index1] = newCell2;
          });
        }
        removeColumn(index) {
          index = +index;
          const filter = (cell) => cell.colIndex !== index;
          const map = (cell, i) => Object.assign({}, cell, {
            colIndex: i
          });
          this.columns = this.columns.filter(filter).map(map);
          this.rows.forEach((row) => {
            row.splice(index, 1);
            row.forEach((cell, i) => {
              cell.colIndex = i;
            });
          });
        }
        updateRow(row, rowIndex) {
          if (row.length < this.columns.length) {
            if (this.hasColumnById("_rowIndex")) {
              const val = rowIndex + 1 + "";
              row = [val].concat(row);
            }
            if (this.hasColumnById("_checkbox")) {
              const val = '<input type="checkbox" />';
              row = [val].concat(row);
            }
          }
          const _row = this.prepareRow(row, { rowIndex });
          const index = this.rows.findIndex((row2) => row2[0].rowIndex === rowIndex);
          this.rows[index] = _row;
          return _row;
        }
        updateCell(colIndex, rowIndex, options) {
          let cell;
          if (typeof colIndex === "object") {
            cell = colIndex;
            colIndex = cell.colIndex;
            rowIndex = cell.rowIndex;
            options = cell;
          }
          cell = this.getCell(colIndex, rowIndex);
          for (let key in options) {
            const newVal = options[key];
            if (newVal !== void 0) {
              cell[key] = newVal;
            }
          }
          return cell;
        }
        updateColumn(colIndex, keyValPairs) {
          const column = this.getColumn(colIndex);
          for (let key in keyValPairs) {
            const newVal = keyValPairs[key];
            if (newVal !== void 0) {
              column[key] = newVal;
            }
          }
          return column;
        }
        filterRows(filters) {
          return this.options.filterRows(this.rows, filters, this).then((result) => {
            if (!result) {
              result = this.getAllRowIndices();
            }
            if (!result.then) {
              result = Promise.resolve(result);
            }
            return result.then((rowsToShow) => {
              this._filteredRows = rowsToShow;
              const rowsToHide = this.getAllRowIndices().filter((index) => !rowsToShow.includes(index));
              return {
                rowsToHide,
                rowsToShow
              };
            });
          });
        }
        getFilteredRowIndices() {
          return this._filteredRows || this.getAllRowIndices();
        }
        getAllRowIndices() {
          return this.rows.map((row) => row.meta.rowIndex);
        }
        getRowCount() {
          return this.rowCount;
        }
        _getNextRowCount() {
          const val = this.rowCount;
          this.rowCount++;
          return val;
        }
        getRows(start, end) {
          return this.rows.slice(start, end);
        }
        getRowsForView(start, end) {
          const rows = this.rowViewOrder.map((i) => this.rows[i]);
          return rows.slice(start, end);
        }
        getColumns(skipStandardColumns) {
          let columns = this.columns;
          if (skipStandardColumns) {
            columns = columns.slice(this.getStandardColumnCount());
          }
          return columns;
        }
        getStandardColumnCount() {
          if (this.options.checkboxColumn && this.options.serialNoColumn) {
            return 2;
          }
          if (this.options.checkboxColumn || this.options.serialNoColumn) {
            return 1;
          }
          return 0;
        }
        getColumnCount(skipStandardColumns) {
          let val = this.columns.length;
          if (skipStandardColumns) {
            val = val - this.getStandardColumnCount();
          }
          return val;
        }
        getColumn(colIndex) {
          colIndex = +colIndex;
          if (colIndex < 0) {
            colIndex = this.columns.length + colIndex;
          }
          return this.columns.find((col) => col.colIndex === colIndex);
        }
        getColumnById(id) {
          return this.columns.find((col) => col.id === id);
        }
        getRow(rowIndex) {
          rowIndex = +rowIndex;
          return this.rows[rowIndex];
        }
        getCell(colIndex, rowIndex) {
          rowIndex = +rowIndex;
          colIndex = +colIndex;
          return this.getRow(rowIndex)[colIndex];
        }
        getChildren(parentRowIndex) {
          parentRowIndex = +parentRowIndex;
          const parentIndent = this.getRow(parentRowIndex).meta.indent;
          const out = [];
          for (let i = parentRowIndex + 1; i < this.rowCount; i++) {
            const row = this.getRow(i);
            if (isNaN(row.meta.indent))
              continue;
            if (row.meta.indent > parentIndent) {
              out.push(i);
            }
            if (row.meta.indent === parentIndent) {
              break;
            }
          }
          return out;
        }
        getImmediateChildren(parentRowIndex) {
          parentRowIndex = +parentRowIndex;
          const parentIndent = this.getRow(parentRowIndex).meta.indent;
          const out = [];
          const childIndent = parentIndent + 1;
          for (let i = parentRowIndex + 1; i < this.rowCount; i++) {
            const row = this.getRow(i);
            if (isNaN(row.meta.indent) || row.meta.indent > childIndent)
              continue;
            if (row.meta.indent === childIndent) {
              out.push(i);
            }
            if (row.meta.indent === parentIndent) {
              break;
            }
          }
          return out;
        }
        get() {
          return {
            columns: this.columns,
            rows: this.rows
          };
        }
        getData(rowIndex) {
          return this.data[rowIndex];
        }
        hasColumn(name2) {
          return Boolean(this.columns.find((col) => col.content === name2));
        }
        hasColumnById(id) {
          return Boolean(this.columns.find((col) => col.id === id));
        }
        getColumnIndex(name2) {
          return this.columns.findIndex((col) => col.content === name2);
        }
        getColumnIndexById(id) {
          return this.columns.findIndex((col) => col.id === id);
        }
        getCheckboxHTML() {
          return '<input type="checkbox" />';
        }
      };
      var DataError = class extends TypeError {
      };
      var icons = {
        chevronDown: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-down"><polyline points="6 9 12 15 18 9"></polyline></svg>',
        chevronRight: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-right"><polyline points="9 18 15 12 9 6"></polyline></svg>'
      };
      var CellManager = class {
        constructor(instance) {
          this.instance = instance;
          linkProperties(this, this.instance, [
            "wrapper",
            "options",
            "style",
            "header",
            "bodyScrollable",
            "columnmanager",
            "rowmanager",
            "datamanager",
            "keyboard"
          ]);
          this.bindEvents();
        }
        bindEvents() {
          this.bindFocusCell();
          this.bindEditCell();
          this.bindKeyboardSelection();
          this.bindCopyCellContents();
          this.bindMouseEvents();
          this.bindTreeEvents();
        }
        bindFocusCell() {
          this.bindKeyboardNav();
        }
        bindEditCell() {
          this.$editingCell = null;
          $2.on(this.bodyScrollable, "dblclick", ".dt-cell", (e, cell) => {
            this.activateEditing(cell);
          });
          this.keyboard.on("enter", () => {
            if (this.$focusedCell && !this.$editingCell) {
              this.activateEditing(this.$focusedCell);
            } else if (this.$editingCell) {
              this.deactivateEditing();
            }
          });
        }
        bindKeyboardNav() {
          const focusLastCell = (direction) => {
            if (!this.$focusedCell || this.$editingCell) {
              return false;
            }
            let $cell = this.$focusedCell;
            const {
              rowIndex,
              colIndex
            } = $2.data($cell);
            if (direction === "left") {
              $cell = this.getLeftMostCell$(rowIndex);
            } else if (direction === "right") {
              $cell = this.getRightMostCell$(rowIndex);
            } else if (direction === "up") {
              $cell = this.getTopMostCell$(colIndex);
            } else if (direction === "down") {
              $cell = this.getBottomMostCell$(colIndex);
            }
            this.focusCell($cell);
            return true;
          };
          ["left", "right", "up", "down", "tab", "shift+tab"].map((direction) => this.keyboard.on(direction, () => this.focusCellInDirection(direction)));
          ["left", "right", "up", "down"].map((direction) => this.keyboard.on(`ctrl+${direction}`, () => focusLastCell(direction)));
          this.keyboard.on("esc", () => {
            this.deactivateEditing(false);
            this.columnmanager.toggleFilter(false);
          });
          if (this.options.inlineFilters) {
            this.keyboard.on("ctrl+f", (e) => {
              const $cell = $2.closest(".dt-cell", e.target);
              const { colIndex } = $2.data($cell);
              this.activateFilter(colIndex);
              return true;
            });
            $2.on(this.header, "focusin", ".dt-filter", () => {
              this.unfocusCell(this.$focusedCell);
            });
          }
        }
        bindKeyboardSelection() {
          const getNextSelectionCursor = (direction) => {
            let $selectionCursor = this.getSelectionCursor();
            if (direction === "left") {
              $selectionCursor = this.getLeftCell$($selectionCursor);
            } else if (direction === "right") {
              $selectionCursor = this.getRightCell$($selectionCursor);
            } else if (direction === "up") {
              $selectionCursor = this.getAboveCell$($selectionCursor);
            } else if (direction === "down") {
              $selectionCursor = this.getBelowCell$($selectionCursor);
            }
            return $selectionCursor;
          };
          ["left", "right", "up", "down"].map((direction) => this.keyboard.on(`shift+${direction}`, () => this.selectArea(getNextSelectionCursor(direction))));
        }
        bindCopyCellContents() {
          this.keyboard.on("ctrl+c", () => {
            const noOfCellsCopied = this.copyCellContents(this.$focusedCell, this.$selectionCursor);
            const message = this.instance.translate("{count} cells copied", {
              count: noOfCellsCopied
            });
            if (noOfCellsCopied) {
              this.instance.showToastMessage(message, 2);
            }
          });
          if (this.options.pasteFromClipboard) {
            this.keyboard.on("ctrl+v", (e) => {
              this.instance.pasteTarget.focus();
              setTimeout(() => {
                const data = this.instance.pasteTarget.value;
                this.instance.pasteTarget.value = "";
                this.pasteContentInCell(data);
              }, 10);
              return false;
            });
          }
        }
        bindMouseEvents() {
          let mouseDown = null;
          $2.on(this.bodyScrollable, "mousedown", ".dt-cell", (e) => {
            mouseDown = true;
            this.focusCell($2(e.delegatedTarget));
          });
          $2.on(this.bodyScrollable, "mouseup", () => {
            mouseDown = false;
          });
          const selectArea = (e) => {
            if (!mouseDown)
              return;
            this.selectArea($2(e.delegatedTarget));
          };
          $2.on(this.bodyScrollable, "mousemove", ".dt-cell", throttle$1(selectArea, 50));
        }
        bindTreeEvents() {
          $2.on(this.bodyScrollable, "click", ".dt-tree-node__toggle", (e, $toggle) => {
            const $cell = $2.closest(".dt-cell", $toggle);
            const { rowIndex } = $2.data($cell);
            if ($cell.classList.contains("dt-cell--tree-close")) {
              this.rowmanager.openSingleNode(rowIndex);
            } else {
              this.rowmanager.closeSingleNode(rowIndex);
            }
          });
        }
        focusCell($cell, {
          skipClearSelection = 0,
          skipDOMFocus = 0,
          skipScrollToCell = 0
        } = {}) {
          if (!$cell)
            return;
          if ($cell === this.$editingCell)
            return;
          const {
            colIndex,
            isHeader
          } = $2.data($cell);
          if (isHeader) {
            return;
          }
          const column = this.columnmanager.getColumn(colIndex);
          if (column.focusable === false) {
            return;
          }
          if (!skipScrollToCell) {
            this.scrollToCell($cell);
          }
          this.deactivateEditing();
          if (!skipClearSelection) {
            this.clearSelection();
          }
          if (this.$focusedCell) {
            this.$focusedCell.classList.remove("dt-cell--focus");
          }
          this.$focusedCell = $cell;
          $cell.classList.add("dt-cell--focus");
          if (!skipDOMFocus) {
            $cell.focus();
          }
          this.highlightRowColumnHeader($cell);
        }
        unfocusCell($cell) {
          if (!$cell)
            return;
          $cell.classList.remove("dt-cell--focus");
          this.$focusedCell = null;
          if (this.lastHeaders) {
            this.lastHeaders.forEach((header) => header && header.classList.remove("dt-cell--highlight"));
          }
        }
        highlightRowColumnHeader($cell) {
          const {
            colIndex,
            rowIndex
          } = $2.data($cell);
          const srNoColIndex = this.datamanager.getColumnIndexById("_rowIndex");
          const colHeaderSelector = `.dt-cell--header-${colIndex}`;
          const rowHeaderSelector = `.dt-cell--${srNoColIndex}-${rowIndex}`;
          if (this.lastHeaders) {
            this.lastHeaders.forEach((header) => header && header.classList.remove("dt-cell--highlight"));
          }
          const colHeader = $2(colHeaderSelector, this.wrapper);
          const rowHeader = $2(rowHeaderSelector, this.wrapper);
          this.lastHeaders = [colHeader, rowHeader];
          this.lastHeaders.forEach((header) => header && header.classList.add("dt-cell--highlight"));
        }
        selectAreaOnClusterChanged() {
          if (!(this.$focusedCell && this.$selectionCursor))
            return;
          const {
            colIndex,
            rowIndex
          } = $2.data(this.$selectionCursor);
          const $cell = this.getCell$(colIndex, rowIndex);
          if (!$cell || $cell === this.$selectionCursor)
            return;
          const fCell = $2.data(this.$focusedCell);
          this.$focusedCell = this.getCell$(fCell.colIndex, fCell.rowIndex);
          this.selectArea($cell);
        }
        focusCellOnClusterChanged() {
          if (!this.$focusedCell)
            return;
          const {
            colIndex,
            rowIndex
          } = $2.data(this.$focusedCell);
          const $cell = this.getCell$(colIndex, rowIndex);
          if (!$cell)
            return;
          this.focusCell($cell, {
            skipClearSelection: 1,
            skipDOMFocus: 1,
            skipScrollToCell: 1
          });
        }
        selectArea($selectionCursor) {
          if (!this.$focusedCell)
            return;
          if (this._selectArea(this.$focusedCell, $selectionCursor)) {
            this.$selectionCursor = $selectionCursor;
          }
        }
        _selectArea($cell1, $cell2) {
          if ($cell1 === $cell2)
            return false;
          const cells = this.getCellsInRange($cell1, $cell2);
          if (!cells)
            return false;
          this.clearSelection();
          this._selectedCells = cells.map((index) => this.getCell$(...index));
          requestAnimationFrame(() => {
            this._selectedCells.map(($cell) => $cell.classList.add("dt-cell--highlight"));
          });
          return true;
        }
        getCellsInRange($cell1, $cell2) {
          let colIndex1, rowIndex1, colIndex2, rowIndex2;
          if (typeof $cell1 === "number") {
            [colIndex1, rowIndex1, colIndex2, rowIndex2] = arguments;
          } else if (typeof $cell1 === "object") {
            if (!($cell1 && $cell2)) {
              return false;
            }
            const cell1 = $2.data($cell1);
            const cell2 = $2.data($cell2);
            colIndex1 = +cell1.colIndex;
            rowIndex1 = +cell1.rowIndex;
            colIndex2 = +cell2.colIndex;
            rowIndex2 = +cell2.rowIndex;
          }
          if (rowIndex1 > rowIndex2) {
            [rowIndex1, rowIndex2] = [rowIndex2, rowIndex1];
          }
          if (colIndex1 > colIndex2) {
            [colIndex1, colIndex2] = [colIndex2, colIndex1];
          }
          if (this.isStandardCell(colIndex1) || this.isStandardCell(colIndex2)) {
            return false;
          }
          const cells = [];
          let colIndex = colIndex1;
          let rowIndex = rowIndex1;
          const rowIndices = [];
          while (rowIndex <= rowIndex2) {
            rowIndices.push(rowIndex);
            rowIndex += 1;
          }
          rowIndices.map((rowIndex3) => {
            while (colIndex <= colIndex2) {
              cells.push([colIndex, rowIndex3]);
              colIndex++;
            }
            colIndex = colIndex1;
          });
          return cells;
        }
        clearSelection() {
          (this._selectedCells || []).forEach(($cell) => $cell.classList.remove("dt-cell--highlight"));
          this._selectedCells = [];
          this.$selectionCursor = null;
        }
        getSelectionCursor() {
          return this.$selectionCursor || this.$focusedCell;
        }
        activateEditing($cell) {
          this.focusCell($cell);
          const {
            rowIndex,
            colIndex
          } = $2.data($cell);
          const col = this.columnmanager.getColumn(colIndex);
          if (col && (col.editable === false || col.focusable === false)) {
            return;
          }
          const cell = this.getCell(colIndex, rowIndex);
          if (cell && cell.editable === false) {
            return;
          }
          if (this.$editingCell) {
            const {
              _rowIndex,
              _colIndex
            } = $2.data(this.$editingCell);
            if (rowIndex === _rowIndex && colIndex === _colIndex) {
              return;
            }
          }
          this.$editingCell = $cell;
          $cell.classList.add("dt-cell--editing");
          const $editCell = $2(".dt-cell__edit", $cell);
          $editCell.innerHTML = "";
          const editor = this.getEditor(colIndex, rowIndex, cell.content, $editCell);
          if (editor) {
            this.currentCellEditor = editor;
            editor.initValue(cell.content, rowIndex, col);
          }
        }
        deactivateEditing(submitValue = true) {
          if (submitValue) {
            this.submitEditing();
          }
          if (this.$focusedCell)
            this.$focusedCell.focus();
          if (!this.$editingCell)
            return;
          this.$editingCell.classList.remove("dt-cell--editing");
          this.$editingCell = null;
        }
        getEditor(colIndex, rowIndex, value, parent) {
          const column = this.datamanager.getColumn(colIndex);
          const row = this.datamanager.getRow(rowIndex);
          const data = this.datamanager.getData(rowIndex);
          let editor = this.options.getEditor ? this.options.getEditor(colIndex, rowIndex, value, parent, column, row, data) : this.getDefaultEditor(parent);
          if (editor === false) {
            return false;
          }
          if (editor === void 0) {
            editor = this.getDefaultEditor(parent);
          }
          return editor;
        }
        getDefaultEditor(parent) {
          const $input = $2.create("input", {
            class: "dt-input",
            type: "text",
            inside: parent
          });
          return {
            initValue(value) {
              $input.focus();
              $input.value = value;
            },
            getValue() {
              return $input.value;
            },
            setValue(value) {
              $input.value = value;
            }
          };
        }
        submitEditing() {
          let promise = Promise.resolve();
          if (!this.$editingCell)
            return promise;
          const $cell = this.$editingCell;
          const {
            rowIndex,
            colIndex
          } = $2.data($cell);
          const col = this.datamanager.getColumn(colIndex);
          if ($cell) {
            const editor = this.currentCellEditor;
            if (editor) {
              let valuePromise = editor.getValue();
              if (!valuePromise.then) {
                valuePromise = Promise.resolve(valuePromise);
              }
              promise = valuePromise.then((value) => {
                const oldValue = this.getCell(colIndex, rowIndex).content;
                if (oldValue === value)
                  return false;
                const done = editor.setValue(value, rowIndex, col);
                this.updateCell(colIndex, rowIndex, value, true);
                $cell.focus();
                if (done && done.then) {
                  done.catch((e) => {
                    console.log(e);
                    this.updateCell(colIndex, rowIndex, oldValue);
                  });
                }
                return done;
              });
            }
          }
          this.currentCellEditor = null;
          return promise;
        }
        copyCellContents($cell1, $cell2) {
          if (!$cell2 && $cell1) {
            const {
              colIndex,
              rowIndex
            } = $2.data($cell1);
            const cell = this.getCell(colIndex, rowIndex);
            copyTextToClipboard(cell.content);
            return 1;
          }
          const cells = this.getCellsInRange($cell1, $cell2);
          if (!cells)
            return 0;
          const rows = cells.map((index) => this.getCell(...index)).reduce((acc, curr) => {
            const rowIndex = curr.rowIndex;
            acc[rowIndex] = acc[rowIndex] || [];
            acc[rowIndex].push(curr.content);
            return acc;
          }, []);
          const values = rows.map((row) => row.join("	")).join("\n");
          copyTextToClipboard(values);
          return rows.reduce((total, row) => total + row.length, 0);
        }
        pasteContentInCell(data) {
          if (!this.$focusedCell)
            return;
          const matrix = data.split("\n").map((row) => row.split("	")).filter((row) => row.length && row.every((it2) => it2));
          let { colIndex, rowIndex } = $2.data(this.$focusedCell);
          let focusedCell = {
            colIndex: +colIndex,
            rowIndex: +rowIndex
          };
          matrix.forEach((row, i) => {
            let rowIndex2 = i + focusedCell.rowIndex;
            row.forEach((cell, j) => {
              let colIndex2 = j + focusedCell.colIndex;
              this.updateCell(colIndex2, rowIndex2, cell, true);
            });
          });
        }
        activateFilter(colIndex) {
          this.columnmanager.toggleFilter();
          this.columnmanager.focusFilter(colIndex);
          if (!this.columnmanager.isFilterShown) {
            this.$focusedCell && this.$focusedCell.focus();
          }
        }
        updateCell(colIndex, rowIndex, value, refreshHtml = false) {
          const cell = this.datamanager.updateCell(colIndex, rowIndex, {
            content: value
          });
          this.refreshCell(cell, refreshHtml);
        }
        refreshCell(cell, refreshHtml = false) {
          const $cell = $2(this.selector(cell.colIndex, cell.rowIndex), this.bodyScrollable);
          $cell.innerHTML = this.getCellContent(cell, refreshHtml);
        }
        toggleTreeButton(rowIndex, flag) {
          const colIndex = this.columnmanager.getFirstColumnIndex();
          const $cell = this.getCell$(colIndex, rowIndex);
          if ($cell) {
            $cell.classList[flag ? "remove" : "add"]("dt-cell--tree-close");
          }
        }
        isStandardCell(colIndex) {
          return colIndex < this.columnmanager.getFirstColumnIndex();
        }
        focusCellInDirection(direction) {
          if (!this.$focusedCell || this.$editingCell && ["left", "right", "up", "down"].includes(direction)) {
            return false;
          } else if (this.$editingCell && ["tab", "shift+tab"].includes(direction)) {
            this.deactivateEditing();
          }
          let $cell = this.$focusedCell;
          if (direction === "left" || direction === "shift+tab") {
            $cell = this.getLeftCell$($cell);
          } else if (direction === "right" || direction === "tab") {
            $cell = this.getRightCell$($cell);
          } else if (direction === "up") {
            $cell = this.getAboveCell$($cell);
          } else if (direction === "down") {
            $cell = this.getBelowCell$($cell);
          }
          if (!$cell) {
            return false;
          }
          const {
            colIndex
          } = $2.data($cell);
          const column = this.columnmanager.getColumn(colIndex);
          if (!column.focusable) {
            let $prevFocusedCell = this.$focusedCell;
            this.unfocusCell($prevFocusedCell);
            this.$focusedCell = $cell;
            let ret = this.focusCellInDirection(direction);
            if (!ret) {
              this.focusCell($prevFocusedCell);
            }
            return ret;
          }
          this.focusCell($cell);
          return true;
        }
        getCell$(colIndex, rowIndex) {
          return $2(this.selector(colIndex, rowIndex), this.bodyScrollable);
        }
        getAboveCell$($cell) {
          const {
            colIndex
          } = $2.data($cell);
          let $aboveRow = $cell.parentElement.previousElementSibling;
          while ($aboveRow && $aboveRow.classList.contains("dt-row--hide")) {
            $aboveRow = $aboveRow.previousElementSibling;
          }
          if (!$aboveRow)
            return $cell;
          return $2(`.dt-cell--col-${colIndex}`, $aboveRow);
        }
        getBelowCell$($cell) {
          const {
            colIndex
          } = $2.data($cell);
          let $belowRow = $cell.parentElement.nextElementSibling;
          while ($belowRow && $belowRow.classList.contains("dt-row--hide")) {
            $belowRow = $belowRow.nextElementSibling;
          }
          if (!$belowRow)
            return $cell;
          return $2(`.dt-cell--col-${colIndex}`, $belowRow);
        }
        getLeftCell$($cell) {
          return $cell.previousElementSibling;
        }
        getRightCell$($cell) {
          return $cell.nextElementSibling;
        }
        getLeftMostCell$(rowIndex) {
          return this.getCell$(this.columnmanager.getFirstColumnIndex(), rowIndex);
        }
        getRightMostCell$(rowIndex) {
          return this.getCell$(this.columnmanager.getLastColumnIndex(), rowIndex);
        }
        getTopMostCell$(colIndex) {
          return this.getCell$(colIndex, this.rowmanager.getFirstRowIndex());
        }
        getBottomMostCell$(colIndex) {
          return this.getCell$(colIndex, this.rowmanager.getLastRowIndex());
        }
        getCell(colIndex, rowIndex) {
          return this.instance.datamanager.getCell(colIndex, rowIndex);
        }
        getRowHeight() {
          return $2.style($2(".dt-row", this.bodyScrollable), "height");
        }
        scrollToCell($cell) {
          if ($2.inViewport($cell, this.bodyScrollable))
            return false;
          const {
            rowIndex
          } = $2.data($cell);
          this.rowmanager.scrollToRow(rowIndex);
          return false;
        }
        getRowCountPerPage() {
          return Math.ceil(this.instance.getViewportHeight() / this.getRowHeight());
        }
        getCellHTML(cell) {
          const {
            rowIndex,
            colIndex,
            isHeader,
            isFilter,
            isTotalRow
          } = cell;
          const dataAttr = makeDataAttributeString({
            rowIndex,
            colIndex,
            isHeader,
            isFilter,
            isTotalRow
          });
          const row = this.datamanager.getRow(rowIndex);
          const isBodyCell = !(isHeader || isFilter || isTotalRow);
          const className = [
            "dt-cell",
            "dt-cell--col-" + colIndex,
            isBodyCell ? `dt-cell--${colIndex}-${rowIndex}` : "",
            isBodyCell ? "dt-cell--row-" + rowIndex : "",
            isHeader ? "dt-cell--header" : "",
            isHeader ? `dt-cell--header-${colIndex}` : "",
            isFilter ? "dt-cell--filter" : "",
            isBodyCell && (row && row.meta.isTreeNodeClose) ? "dt-cell--tree-close" : ""
          ].join(" ");
          return `
            <div class="${className}" ${dataAttr} tabindex="0">
                ${this.getCellContent(cell)}
            </div>
        `;
        }
        getCellContent(cell, refreshHtml = false) {
          const {
            isHeader,
            isFilter,
            colIndex
          } = cell;
          const editable = !isHeader && cell.editable !== false;
          const editCellHTML = editable ? this.getEditCellHTML(colIndex) : "";
          const sortable = isHeader && cell.sortable !== false;
          const sortIndicator = sortable ? `<span class="sort-indicator">
                ${this.options.sortIndicator[cell.sortOrder]}
            </span>` : "";
          const resizable = isHeader && cell.resizable !== false;
          const resizeColumn = resizable ? '<span class="dt-cell__resize-handle"></span>' : "";
          const hasDropdown = isHeader && cell.dropdown !== false;
          const dropdown = hasDropdown ? this.columnmanager.getDropdownHTML() : "";
          let customFormatter = CellManager.getCustomCellFormatter(cell);
          let contentHTML;
          if (isHeader || isFilter || !customFormatter) {
            contentHTML = cell.content;
          } else {
            if (!cell.html || refreshHtml) {
              const row = this.datamanager.getRow(cell.rowIndex);
              const data = this.datamanager.getData(cell.rowIndex);
              contentHTML = customFormatter(cell.content, row, cell.column, data);
            } else {
              contentHTML = cell.html;
            }
          }
          cell.html = contentHTML;
          if (this.options.treeView && !(isHeader || isFilter) && cell.indent !== void 0) {
            const nextRow = this.datamanager.getRow(cell.rowIndex + 1);
            const addToggle = nextRow && nextRow.meta.indent > cell.indent;
            const leftPadding = 20;
            const unit = "px";
            const firstColumnIndex = this.datamanager.getColumnIndexById("_rowIndex") + 1;
            if (firstColumnIndex === cell.colIndex) {
              const padding = (cell.indent || 0) * leftPadding;
              const toggleHTML = addToggle ? `<span class="dt-tree-node__toggle" style="left: ${padding - leftPadding}${unit}">
                        <span class="icon-open">${icons.chevronDown}</span>
                        <span class="icon-close">${icons.chevronRight}</span>
                    </span>` : "";
              contentHTML = `<span class="dt-tree-node" style="padding-left: ${padding}${unit}">
                    ${toggleHTML}
                    <span>${contentHTML}</span>
                </span>`;
            }
          }
          const className = [
            "dt-cell__content",
            isHeader ? `dt-cell__content--header-${colIndex}` : `dt-cell__content--col-${colIndex}`
          ].join(" ");
          let cellContentHTML = `
            <div class="${className}">
                ${contentHTML}
                ${sortIndicator}
                ${resizeColumn}
                ${dropdown}
            </div>
            ${editCellHTML}
        `;
          let div = document.createElement("div");
          div.innerHTML = contentHTML;
          let textContent = div.textContent;
          textContent = textContent.replace(/\s+/g, " ").trim();
          cellContentHTML = cellContentHTML.replace(">", ` title="${escapeHTML(textContent)}">`);
          return cellContentHTML;
        }
        getEditCellHTML(colIndex) {
          return `<div class="dt-cell__edit dt-cell__edit--col-${colIndex}"></div>`;
        }
        selector(colIndex, rowIndex) {
          return `.dt-cell--${colIndex}-${rowIndex}`;
        }
        static getCustomCellFormatter(cell) {
          return cell.format || cell.column && cell.column.format || null;
        }
      };
      var ColumnManager = class {
        constructor(instance) {
          this.instance = instance;
          linkProperties(this, this.instance, [
            "options",
            "fireEvent",
            "header",
            "datamanager",
            "cellmanager",
            "style",
            "wrapper",
            "rowmanager",
            "bodyScrollable",
            "bodyRenderer"
          ]);
          this.bindEvents();
        }
        renderHeader() {
          this.header.innerHTML = "<div></div>";
          this.refreshHeader();
        }
        refreshHeader() {
          const columns = this.datamanager.getColumns();
          $2("div", this.header).innerHTML = this.getHeaderHTML(columns);
          this.$filterRow = $2(".dt-row-filter", this.header);
          if (this.$filterRow) {
            $2.style(this.$filterRow, { display: "none" });
          }
          this.$columnMap = [];
          this.bindMoveColumn();
        }
        getHeaderHTML(columns) {
          let html = this.rowmanager.getRowHTML(columns, {
            isHeader: 1
          });
          if (this.options.inlineFilters) {
            html += this.rowmanager.getRowHTML(columns, {
              isFilter: 1
            });
          }
          return html;
        }
        bindEvents() {
          this.bindDropdown();
          this.bindResizeColumn();
          this.bindPerfectColumnWidth();
          this.bindFilter();
        }
        bindDropdown() {
          let toggleClass = ".dt-dropdown__toggle";
          let dropdownClass = ".dt-dropdown__list";
          this.instance.dropdownContainer.innerHTML = this.getDropdownListHTML();
          this.$dropdownList = this.instance.dropdownContainer.firstElementChild;
          $2.on(this.header, "click", toggleClass, (e) => {
            this.openDropdown(e);
          });
          const deactivateDropdownOnBodyClick = (e) => {
            const selector = [
              toggleClass,
              toggleClass + " *",
              dropdownClass,
              dropdownClass + " *"
            ].join(",");
            if (e.target.matches(selector))
              return;
            deactivateDropdown();
          };
          $2.on(document.body, "click", deactivateDropdownOnBodyClick);
          document.addEventListener("scroll", deactivateDropdown, true);
          this.instance.on("onDestroy", () => {
            $2.off(document.body, "click", deactivateDropdownOnBodyClick);
            $2.off(document, "scroll", deactivateDropdown);
          });
          $2.on(this.$dropdownList, "click", ".dt-dropdown__list-item", (e, $item) => {
            if (!this._dropdownActiveColIndex)
              return;
            const dropdownItems = this.options.headerDropdown;
            const { index } = $2.data($item);
            const colIndex = this._dropdownActiveColIndex;
            let callback = dropdownItems[index].action;
            callback && callback.call(this.instance, this.getColumn(colIndex));
            this.hideDropdown();
          });
          const _this = this;
          function deactivateDropdown(e) {
            _this.hideDropdown();
          }
          this.hideDropdown();
        }
        openDropdown(e) {
          if (!this._dropdownWidth) {
            $2.style(this.$dropdownList, { display: "" });
            this._dropdownWidth = $2.style(this.$dropdownList, "width");
          }
          $2.style(this.$dropdownList, {
            display: "",
            left: e.clientX - this._dropdownWidth + 4 + "px",
            top: e.clientY + 4 + "px"
          });
          const $cell = $2.closest(".dt-cell", e.target);
          const { colIndex } = $2.data($cell);
          this._dropdownActiveColIndex = colIndex;
        }
        hideDropdown() {
          $2.style(this.$dropdownList, {
            display: "none"
          });
          this._dropdownActiveColIndex = null;
        }
        bindResizeColumn() {
          let isDragging = false;
          let $resizingCell, startWidth, startX;
          $2.on(this.header, "mousedown", ".dt-cell .dt-cell__resize-handle", (e, $handle) => {
            document.body.classList.add("dt-resize");
            const $cell = $handle.parentNode.parentNode;
            $resizingCell = $cell;
            const {
              colIndex
            } = $2.data($resizingCell);
            const col = this.getColumn(colIndex);
            if (col && col.resizable === false) {
              return;
            }
            isDragging = true;
            startWidth = $2.style($2(".dt-cell__content", $resizingCell), "width");
            startX = e.pageX;
          });
          const onMouseup = (e) => {
            document.body.classList.remove("dt-resize");
            if (!$resizingCell)
              return;
            isDragging = false;
            const {
              colIndex
            } = $2.data($resizingCell);
            this.setColumnWidth(colIndex);
            this.style.setBodyStyle();
            $resizingCell = null;
          };
          $2.on(document.body, "mouseup", onMouseup);
          this.instance.on("onDestroy", () => {
            $2.off(document.body, "mouseup", onMouseup);
          });
          const onMouseMove = (e) => {
            if (!isDragging)
              return;
            let delta = e.pageX - startX;
            if (this.options.direction === "rtl") {
              delta = -1 * delta;
            }
            const finalWidth = startWidth + delta;
            const {
              colIndex
            } = $2.data($resizingCell);
            let columnMinWidth = this.options.minimumColumnWidth;
            if (columnMinWidth > finalWidth) {
              return;
            }
            this.datamanager.updateColumn(colIndex, {
              width: finalWidth
            });
            this.setColumnHeaderWidth(colIndex);
          };
          $2.on(document.body, "mousemove", onMouseMove);
          this.instance.on("onDestroy", () => {
            $2.off(document.body, "mousemove", onMouseMove);
          });
        }
        bindPerfectColumnWidth() {
          $2.on(this.header, "dblclick", ".dt-cell .dt-cell__resize-handle", (e, $handle) => {
            const $cell = $handle.parentNode.parentNode;
            const { colIndex } = $2.data($cell);
            let longestCell = this.bodyRenderer.visibleRows.map((d) => d[colIndex]).reduce((acc, curr) => acc.content.length > curr.content.length ? acc : curr);
            let $longestCellHTML = this.cellmanager.getCellHTML(longestCell);
            let $div = document.createElement("div");
            $div.innerHTML = $longestCellHTML;
            let cellText = $div.querySelector(".dt-cell__content").textContent;
            let {
              borderLeftWidth,
              borderRightWidth,
              paddingLeft,
              paddingRight
            } = $2.getStyle(this.bodyScrollable.querySelector(".dt-cell__content"));
            let padding = [borderLeftWidth, borderRightWidth, paddingLeft, paddingRight].map(parseFloat).reduce((sum, val) => sum + val);
            let width = $2.measureTextWidth(cellText) + padding;
            this.datamanager.updateColumn(colIndex, { width });
            this.setColumnHeaderWidth(colIndex);
            this.setColumnWidth(colIndex);
          });
        }
        bindMoveColumn() {
          if (this.options.disableReorderColumn)
            return;
          const $parent = $2(".dt-row", this.header);
          this.sortable = Sortable.create($parent, {
            onEnd: (e) => {
              const {
                oldIndex,
                newIndex
              } = e;
              const $draggedCell = e.item;
              const {
                colIndex
              } = $2.data($draggedCell);
              if (+colIndex === newIndex)
                return;
              this.switchColumn(oldIndex, newIndex);
            },
            preventOnFilter: false,
            filter: ".dt-cell__resize-handle, .dt-dropdown",
            chosenClass: "dt-cell--dragging",
            animation: 150
          });
        }
        sortColumn(colIndex, nextSortOrder) {
          this.instance.freeze();
          this.sortRows(colIndex, nextSortOrder).then(() => {
            this.refreshHeader();
            return this.rowmanager.refreshRows();
          }).then(() => this.instance.unfreeze()).then(() => {
            this.fireEvent("onSortColumn", this.getColumn(colIndex));
          });
        }
        removeColumn(colIndex) {
          const removedCol = this.getColumn(colIndex);
          this.instance.freeze();
          this.datamanager.removeColumn(colIndex).then(() => {
            this.refreshHeader();
            return this.rowmanager.refreshRows();
          }).then(() => this.instance.unfreeze()).then(() => {
            this.fireEvent("onRemoveColumn", removedCol);
          });
        }
        switchColumn(oldIndex, newIndex) {
          this.instance.freeze();
          this.datamanager.switchColumn(oldIndex, newIndex).then(() => {
            this.refreshHeader();
            return this.rowmanager.refreshRows();
          }).then(() => {
            this.setColumnWidth(oldIndex);
            this.setColumnWidth(newIndex);
            this.instance.unfreeze();
          }).then(() => {
            this.fireEvent(
              "onSwitchColumn",
              this.getColumn(oldIndex),
              this.getColumn(newIndex)
            );
          });
        }
        toggleFilter(flag) {
          if (!this.options.inlineFilters)
            return;
          let showFilter;
          if (flag === void 0) {
            showFilter = !this.isFilterShown;
          } else {
            showFilter = flag;
          }
          if (showFilter) {
            $2.style(this.$filterRow, { display: "" });
          } else {
            $2.style(this.$filterRow, { display: "none" });
          }
          this.isFilterShown = showFilter;
          this.style.setBodyStyle();
        }
        focusFilter(colIndex) {
          if (!this.isFilterShown)
            return;
          const $filterInput = $2(`.dt-cell--col-${colIndex} .dt-filter`, this.$filterRow);
          $filterInput.focus();
        }
        bindFilter() {
          if (!this.options.inlineFilters)
            return;
          const handler = (e) => {
            this.applyFilter(this.getAppliedFilters());
          };
          $2.on(this.header, "keydown", ".dt-filter", debounce$1(handler, 300));
        }
        applyFilter(filters) {
          this.datamanager.filterRows(filters).then(({
            rowsToShow
          }) => {
            this.rowmanager.showRows(rowsToShow);
          });
        }
        getAppliedFilters() {
          const filters = {};
          $2.each(".dt-filter", this.header).map((input) => {
            const value = input.value;
            if (value) {
              filters[input.dataset.colIndex] = value;
            }
          });
          return filters;
        }
        applyDefaultSortOrder() {
          const columnsToSort = this.getColumns().filter((col) => col.sortOrder !== "none");
          if (columnsToSort.length === 1) {
            const column = columnsToSort[0];
            this.sortColumn(column.colIndex, column.sortOrder);
          }
        }
        sortRows(colIndex, sortOrder) {
          return this.datamanager.sortRows(colIndex, sortOrder);
        }
        getColumn(colIndex) {
          return this.datamanager.getColumn(colIndex);
        }
        getColumns() {
          return this.datamanager.getColumns();
        }
        setColumnWidth(colIndex, width) {
          colIndex = +colIndex;
          let columnWidth = width || this.getColumn(colIndex).width;
          const selector = [
            `.dt-cell__content--col-${colIndex}`,
            `.dt-cell__edit--col-${colIndex}`
          ].join(", ");
          const styles = {
            width: columnWidth + "px"
          };
          this.style.setStyle(selector, styles);
        }
        setColumnHeaderWidth(colIndex) {
          colIndex = +colIndex;
          this.$columnMap = this.$columnMap || [];
          const selector = `.dt-cell__content--header-${colIndex}`;
          const {
            width
          } = this.getColumn(colIndex);
          let $column = this.$columnMap[colIndex];
          if (!$column) {
            $column = this.header.querySelector(selector);
            this.$columnMap[colIndex] = $column;
          }
          $column.style.width = width + "px";
        }
        getColumnMinWidth(colIndex) {
          colIndex = +colIndex;
          return this.getColumn(colIndex).minWidth || 24;
        }
        getFirstColumnIndex() {
          return this.datamanager.getColumnIndexById("_rowIndex") + 1;
        }
        getHeaderCell$(colIndex) {
          return $2(`.dt-cell--header-${colIndex}`, this.header);
        }
        getLastColumnIndex() {
          return this.datamanager.getColumnCount() - 1;
        }
        getDropdownHTML() {
          const { dropdownButton } = this.options;
          return `
            <div class="dt-dropdown">
                <div class="dt-dropdown__toggle">${dropdownButton}</div>
            </div>
      `;
        }
        getDropdownListHTML() {
          const { headerDropdown: dropdownItems } = this.options;
          return `
            <div class="dt-dropdown__list">
            ${dropdownItems.map((d, i) => `
                <div class="dt-dropdown__list-item" data-index="${i}">${d.label}</div>
            `).join("")}
            </div>
        `;
        }
      };
      var RowManager = class {
        constructor(instance) {
          this.instance = instance;
          linkProperties(this, this.instance, [
            "options",
            "fireEvent",
            "wrapper",
            "bodyScrollable",
            "bodyRenderer",
            "style"
          ]);
          this.bindEvents();
          this.refreshRows = nextTick(this.refreshRows, this);
        }
        get datamanager() {
          return this.instance.datamanager;
        }
        get cellmanager() {
          return this.instance.cellmanager;
        }
        bindEvents() {
          this.bindCheckbox();
        }
        bindCheckbox() {
          if (!this.options.checkboxColumn)
            return;
          this.checkMap = [];
          $2.on(this.wrapper, "click", '.dt-cell--col-0 [type="checkbox"]', (e, $checkbox) => {
            const $cell = $checkbox.closest(".dt-cell");
            const {
              rowIndex,
              isHeader
            } = $2.data($cell);
            const checked = $checkbox.checked;
            if (isHeader) {
              this.checkAll(checked);
            } else {
              this.checkRow(rowIndex, checked);
            }
          });
        }
        refreshRows() {
          this.instance.renderBody();
          this.instance.setDimensions();
        }
        refreshRow(row, rowIndex) {
          const _row = this.datamanager.updateRow(row, rowIndex);
          _row.forEach((cell) => {
            this.cellmanager.refreshCell(cell, true);
          });
        }
        getCheckedRows() {
          if (!this.checkMap) {
            return [];
          }
          let out = [];
          for (let rowIndex in this.checkMap) {
            const checked = this.checkMap[rowIndex];
            if (checked === 1) {
              out.push(rowIndex);
            }
          }
          return out;
        }
        highlightCheckedRows() {
          this.getCheckedRows().map((rowIndex) => this.checkRow(rowIndex, true));
        }
        checkRow(rowIndex, toggle) {
          const value = toggle ? 1 : 0;
          const selector = (rowIndex2) => `.dt-cell--0-${rowIndex2} [type="checkbox"]`;
          this.checkMap[rowIndex] = value;
          $2.each(selector(rowIndex), this.bodyScrollable).map((input) => {
            input.checked = toggle;
          });
          this.highlightRow(rowIndex, toggle);
          this.showCheckStatus();
          this.fireEvent("onCheckRow", this.datamanager.getRow(rowIndex));
        }
        checkAll(toggle) {
          const value = toggle ? 1 : 0;
          if (toggle) {
            if (this.datamanager._filteredRows) {
              this.datamanager._filteredRows.forEach((f) => {
                this.checkRow(f, toggle);
              });
            } else {
              this.checkMap = Array.from(Array(this.getTotalRows())).map((c) => value);
            }
          } else {
            this.checkMap = [];
          }
          $2.each('.dt-cell--col-0 [type="checkbox"]', this.bodyScrollable).map((input) => {
            input.checked = toggle;
          });
          this.highlightAll(toggle);
          this.showCheckStatus();
          this.fireEvent("onCheckRow");
        }
        showCheckStatus() {
          if (!this.options.checkedRowStatus)
            return;
          const checkedRows = this.getCheckedRows();
          const count = checkedRows.length;
          if (count > 0) {
            let message = this.instance.translate("{count} rows selected", {
              count
            });
            this.bodyRenderer.showToastMessage(message);
          } else {
            this.bodyRenderer.clearToastMessage();
          }
        }
        highlightRow(rowIndex, toggle = true) {
          const $row = this.getRow$(rowIndex);
          if (!$row)
            return;
          if (!toggle && this.bodyScrollable.classList.contains("dt-scrollable--highlight-all")) {
            $row.classList.add("dt-row--unhighlight");
            return;
          }
          if (toggle && $row.classList.contains("dt-row--unhighlight")) {
            $row.classList.remove("dt-row--unhighlight");
          }
          this._highlightedRows = this._highlightedRows || {};
          if (toggle) {
            $row.classList.add("dt-row--highlight");
            this._highlightedRows[rowIndex] = $row;
          } else {
            $row.classList.remove("dt-row--highlight");
            delete this._highlightedRows[rowIndex];
          }
        }
        highlightAll(toggle = true) {
          if (toggle) {
            this.bodyScrollable.classList.add("dt-scrollable--highlight-all");
          } else {
            this.bodyScrollable.classList.remove("dt-scrollable--highlight-all");
            for (const rowIndex in this._highlightedRows) {
              const $row = this._highlightedRows[rowIndex];
              $row.classList.remove("dt-row--highlight");
            }
            this._highlightedRows = {};
          }
        }
        showRows(rowIndices) {
          rowIndices = ensureArray(rowIndices);
          const rows = rowIndices.map((rowIndex) => this.datamanager.getRow(rowIndex));
          this.bodyRenderer.renderRows(rows);
        }
        showAllRows() {
          const rowIndices = this.datamanager.getAllRowIndices();
          this.showRows(rowIndices);
        }
        getChildrenToShowForNode(rowIndex) {
          const row = this.datamanager.getRow(rowIndex);
          row.meta.isTreeNodeClose = false;
          return this.datamanager.getImmediateChildren(rowIndex);
        }
        openSingleNode(rowIndex) {
          const childrenToShow = this.getChildrenToShowForNode(rowIndex);
          const visibleRowIndices = this.bodyRenderer.visibleRowIndices;
          const rowsToShow = uniq$1([...childrenToShow, ...visibleRowIndices]).sort(numberSortAsc);
          this.showRows(rowsToShow);
        }
        getChildrenToHideForNode(rowIndex) {
          const row = this.datamanager.getRow(rowIndex);
          row.meta.isTreeNodeClose = true;
          const rowsToHide = this.datamanager.getChildren(rowIndex);
          rowsToHide.forEach((rowIndex2) => {
            const row2 = this.datamanager.getRow(rowIndex2);
            if (!row2.meta.isLeaf) {
              row2.meta.isTreeNodeClose = true;
            }
          });
          return rowsToHide;
        }
        closeSingleNode(rowIndex) {
          const rowsToHide = this.getChildrenToHideForNode(rowIndex);
          const visibleRows = this.bodyRenderer.visibleRowIndices;
          const rowsToShow = visibleRows.filter((rowIndex2) => !rowsToHide.includes(rowIndex2)).sort(numberSortAsc);
          this.showRows(rowsToShow);
        }
        expandAllNodes() {
          let rows = this.datamanager.getRows();
          let rootNodes = rows.filter((row) => !row.meta.isLeaf);
          const childrenToShow = rootNodes.map((row) => this.getChildrenToShowForNode(row.meta.rowIndex)).flat();
          const visibleRowIndices = this.bodyRenderer.visibleRowIndices;
          const rowsToShow = uniq$1([...childrenToShow, ...visibleRowIndices]).sort(numberSortAsc);
          this.showRows(rowsToShow);
        }
        collapseAllNodes() {
          let rows = this.datamanager.getRows();
          let rootNodes = rows.filter((row) => row.meta.indent === 0);
          const rowsToHide = rootNodes.map((row) => this.getChildrenToHideForNode(row.meta.rowIndex)).flat();
          const visibleRows = this.bodyRenderer.visibleRowIndices;
          const rowsToShow = visibleRows.filter((rowIndex) => !rowsToHide.includes(rowIndex)).sort(numberSortAsc);
          this.showRows(rowsToShow);
        }
        setTreeDepth(depth) {
          let rows = this.datamanager.getRows();
          const rowsToOpen = rows.filter((row) => row.meta.indent < depth);
          const rowsToClose = rows.filter((row) => row.meta.indent >= depth);
          const rowsToHide = rowsToClose.filter((row) => row.meta.indent > depth);
          rowsToClose.forEach((row) => {
            if (!row.meta.isLeaf) {
              row.meta.isTreeNodeClose = true;
            }
          });
          rowsToOpen.forEach((row) => {
            if (!row.meta.isLeaf) {
              row.meta.isTreeNodeClose = false;
            }
          });
          const rowsToShow = rows.filter((row) => !rowsToHide.includes(row)).map((row) => row.meta.rowIndex).sort(numberSortAsc);
          this.showRows(rowsToShow);
        }
        getRow$(rowIndex) {
          return $2(this.selector(rowIndex), this.bodyScrollable);
        }
        getTotalRows() {
          return this.datamanager.getRowCount();
        }
        getFirstRowIndex() {
          return 0;
        }
        getLastRowIndex() {
          return this.datamanager.getRowCount() - 1;
        }
        scrollToRow(rowIndex) {
          rowIndex = +rowIndex;
          this._lastScrollTo = this._lastScrollTo || 0;
          const $row = this.getRow$(rowIndex);
          if ($2.inViewport($row, this.bodyScrollable))
            return;
          const {
            height
          } = $row.getBoundingClientRect();
          const {
            top,
            bottom
          } = this.bodyScrollable.getBoundingClientRect();
          const rowsInView = Math.floor((bottom - top) / height);
          let offset = 0;
          if (rowIndex > this._lastScrollTo) {
            offset = height * (rowIndex + 1 - rowsInView);
          } else {
            offset = height * (rowIndex + 1 - 1);
          }
          this._lastScrollTo = rowIndex;
          $2.scrollTop(this.bodyScrollable, offset);
        }
        getRowHTML(row, props) {
          const dataAttr = makeDataAttributeString(props);
          let rowIdentifier = props.rowIndex;
          if (props.isFilter) {
            row = row.map((cell) => Object.assign({}, cell, {
              content: this.getFilterInput({
                colIndex: cell.colIndex,
                name: cell.name
              }),
              isFilter: 1,
              isHeader: void 0,
              editable: false
            }));
            rowIdentifier = "filter";
          }
          if (props.isHeader) {
            rowIdentifier = "header";
          }
          return `
            <div class="dt-row dt-row-${rowIdentifier}" ${dataAttr}>
                ${row.map((cell) => this.cellmanager.getCellHTML(cell)).join("")}
            </div>
        `;
        }
        getFilterInput(props) {
          let title = `title="Filter based on ${props.name || "Index"}"`;
          const dataAttr = makeDataAttributeString(props);
          return `<input class="dt-filter dt-input" type="text" ${dataAttr} tabindex="1"
            ${props.colIndex === 0 ? "disabled" : title} />`;
        }
        selector(rowIndex) {
          return `.dt-row-${rowIndex}`;
        }
      };
      var hyperlist = createCommonjsModule(function(module2, exports2) {
        (function(f) {
          {
            module2.exports = f();
          }
        })(function() {
          return function e(t, n, r) {
            function s(o2, u) {
              if (!n[o2]) {
                if (!t[o2]) {
                  var a = typeof commonjsRequire == "function" && commonjsRequire;
                  if (!u && a)
                    return a(o2, true);
                  if (i)
                    return i(o2, true);
                  var f = new Error("Cannot find module '" + o2 + "'");
                  throw f.code = "MODULE_NOT_FOUND", f;
                }
                var l = n[o2] = { exports: {} };
                t[o2][0].call(l.exports, function(e2) {
                  var n2 = t[o2][1][e2];
                  return s(n2 ? n2 : e2);
                }, l, l.exports, e, t, n, r);
              }
              return n[o2].exports;
            }
            var i = typeof commonjsRequire == "function" && commonjsRequire;
            for (var o = 0; o < r.length; o++)
              s(r[o]);
            return s;
          }({ 1: [function(_dereq_, module3, exports3) {
            Object.defineProperty(exports3, "__esModule", {
              value: true
            });
            var _createClass = function() {
              function defineProperties(target, props) {
                for (var i = 0; i < props.length; i++) {
                  var descriptor = props[i];
                  descriptor.enumerable = descriptor.enumerable || false;
                  descriptor.configurable = true;
                  if ("value" in descriptor)
                    descriptor.writable = true;
                  Object.defineProperty(target, descriptor.key, descriptor);
                }
              }
              return function(Constructor, protoProps, staticProps) {
                if (protoProps)
                  defineProperties(Constructor.prototype, protoProps);
                if (staticProps)
                  defineProperties(Constructor, staticProps);
                return Constructor;
              };
            }();
            function _classCallCheck(instance, Constructor) {
              if (!(instance instanceof Constructor)) {
                throw new TypeError("Cannot call a class as a function");
              }
            }
            var defaultConfig = {
              width: "100%",
              height: "100%"
            };
            var isNumber2 = function isNumber3(input) {
              return Number(input) === Number(input);
            };
            var HyperList2 = function() {
              _createClass(HyperList3, null, [{
                key: "create",
                value: function create(element, userProvidedConfig) {
                  return new HyperList3(element, userProvidedConfig);
                }
              }, {
                key: "mergeStyle",
                value: function mergeStyle(element, style) {
                  for (var i in style) {
                    if (element.style[i] !== style[i]) {
                      element.style[i] = style[i];
                    }
                  }
                }
              }, {
                key: "getMaxBrowserHeight",
                value: function getMaxBrowserHeight() {
                  var wrapper = document.createElement("div");
                  var fixture = document.createElement("div");
                  HyperList3.mergeStyle(wrapper, { position: "absolute", height: "1px", opacity: 0 });
                  HyperList3.mergeStyle(fixture, { height: "1e7px" });
                  wrapper.appendChild(fixture);
                  document.body.appendChild(wrapper);
                  var maxElementHeight = fixture.offsetHeight;
                  document.body.removeChild(wrapper);
                  return maxElementHeight;
                }
              }]);
              function HyperList3(element, userProvidedConfig) {
                var _this = this;
                _classCallCheck(this, HyperList3);
                this._config = {};
                this._lastRepaint = null;
                this._maxElementHeight = HyperList3.getMaxBrowserHeight();
                this.refresh(element, userProvidedConfig);
                var config2 = this._config;
                var render = function render2() {
                  var scrollTop = _this._getScrollPosition();
                  var lastRepaint = _this._lastRepaint;
                  _this._renderAnimationFrame = window.requestAnimationFrame(render2);
                  if (scrollTop === lastRepaint) {
                    return;
                  }
                  if (!lastRepaint || Math.abs(scrollTop - lastRepaint) > _this._averageHeight) {
                    var rendered = _this._renderChunk();
                    _this._lastRepaint = scrollTop;
                    if (rendered !== false && typeof config2.afterRender === "function") {
                      config2.afterRender();
                    }
                  }
                };
                render();
              }
              _createClass(HyperList3, [{
                key: "destroy",
                value: function destroy() {
                  window.cancelAnimationFrame(this._renderAnimationFrame);
                }
              }, {
                key: "refresh",
                value: function refresh(element, userProvidedConfig) {
                  var _this2 = this;
                  Object.assign(this._config, defaultConfig, userProvidedConfig);
                  if (!element || element.nodeType !== 1) {
                    throw new Error("HyperList requires a valid DOM Node container");
                  }
                  this._element = element;
                  var config2 = this._config;
                  var scroller = this._scroller || config2.scroller || document.createElement(config2.scrollerTagName || "tr");
                  if (typeof config2.useFragment !== "boolean") {
                    this._config.useFragment = true;
                  }
                  if (!config2.generate) {
                    throw new Error("Missing required `generate` function");
                  }
                  if (!isNumber2(config2.total)) {
                    throw new Error("Invalid required `total` value, expected number");
                  }
                  if (!Array.isArray(config2.itemHeight) && !isNumber2(config2.itemHeight)) {
                    throw new Error("\n        Invalid required `itemHeight` value, expected number or array\n      ".trim());
                  } else if (isNumber2(config2.itemHeight)) {
                    this._itemHeights = Array(config2.total).fill(config2.itemHeight);
                  } else {
                    this._itemHeights = config2.itemHeight;
                  }
                  Object.keys(defaultConfig).filter(function(prop) {
                    return prop in config2;
                  }).forEach(function(prop) {
                    var value = config2[prop];
                    var isValueNumber = isNumber2(value);
                    var isValuePercent = isValueNumber ? false : value.slice(-1) === "%";
                    if (value && typeof value !== "string" && typeof value !== "number") {
                      var msg = "Invalid optional `" + prop + "`, expected string or number";
                      throw new Error(msg);
                    } else if (isValueNumber) {
                      config2[prop] = value + "px";
                    }
                    if (prop !== "height") {
                      return;
                    }
                    var numberValue = isValueNumber ? value : parseInt(value.replace(/px|%/, ""), 10);
                    if (isValuePercent) {
                      _this2._containerHeight = window.innerHeight * numberValue / 100;
                    } else {
                      _this2._containerHeight = isNumber2(value) ? value : numberValue;
                    }
                  });
                  var elementStyle = {
                    width: "" + config2.width,
                    height: "" + config2.height,
                    overflow: "auto",
                    position: "relative"
                  };
                  HyperList3.mergeStyle(element, elementStyle);
                  var scrollerHeight = config2.itemHeight * config2.total;
                  var maxElementHeight = this._maxElementHeight;
                  if (scrollerHeight > maxElementHeight) {
                    console.warn(["HyperList: The maximum element height", maxElementHeight + "px has", "been exceeded; please reduce your item height."].join(" "));
                  }
                  var scrollerStyle = {
                    opacity: "0",
                    position: "absolute",
                    width: "1px",
                    height: scrollerHeight + "px"
                  };
                  HyperList3.mergeStyle(scroller, scrollerStyle);
                  if (!this._scroller) {
                    element.appendChild(scroller);
                  }
                  this._scroller = scroller;
                  this._scrollHeight = this._computeScrollHeight();
                  this._itemPositions = this._itemPositions || Array(config2.total).fill(0);
                  this._computePositions(0);
                  this._renderChunk(this._lastRepaint !== null);
                  if (typeof config2.afterRender === "function") {
                    config2.afterRender();
                  }
                }
              }, {
                key: "_getRow",
                value: function _getRow(i) {
                  var config2 = this._config;
                  var item = config2.generate(i);
                  var height = item.height;
                  if (height !== void 0 && isNumber2(height)) {
                    item = item.element;
                    if (height !== this._itemHeights) {
                      this._itemHeights[i] = height;
                      this._computePositions(i);
                      this._scrollHeight = this._computeScrollHeight(i);
                    }
                  } else {
                    height = this._itemHeights[i];
                  }
                  if (!item || item.nodeType !== 1) {
                    throw new Error("Generator did not return a DOM Node for index: " + i);
                  }
                  var oldClass = item.getAttribute("class") || "";
                  item.setAttribute("class", oldClass + " " + (config2.rowClassName || "vrow"));
                  var top = this._itemPositions[i];
                  HyperList3.mergeStyle(item, {
                    position: "absolute",
                    top: top + "px"
                  });
                  return item;
                }
              }, {
                key: "_getScrollPosition",
                value: function _getScrollPosition() {
                  var config2 = this._config;
                  if (typeof config2.overrideScrollPosition === "function") {
                    return config2.overrideScrollPosition();
                  }
                  return this._element.scrollTop;
                }
              }, {
                key: "_renderChunk",
                value: function _renderChunk(force) {
                  var config2 = this._config;
                  var element = this._element;
                  var scrollTop = this._getScrollPosition();
                  var total = config2.total;
                  var from = config2.reverse ? this._getReverseFrom(scrollTop) : this._getFrom(scrollTop) - 1;
                  if (from < 0 || from - this._screenItemsLen < 0) {
                    from = 0;
                  }
                  if (!force && this._lastFrom === from) {
                    return false;
                  }
                  this._lastFrom = from;
                  var to = from + this._cachedItemsLen;
                  if (to > total || to + this._cachedItemsLen > total) {
                    to = total;
                  }
                  var fragment = config2.useFragment ? document.createDocumentFragment() : [];
                  var scroller = this._scroller;
                  fragment[config2.useFragment ? "appendChild" : "push"](scroller);
                  for (var i = from; i < to; i++) {
                    var row = this._getRow(i);
                    fragment[config2.useFragment ? "appendChild" : "push"](row);
                  }
                  if (config2.applyPatch) {
                    return config2.applyPatch(element, fragment);
                  }
                  element.innerHTML = "";
                  element.appendChild(fragment);
                }
              }, {
                key: "_computePositions",
                value: function _computePositions() {
                  var from = arguments.length <= 0 || arguments[0] === void 0 ? 1 : arguments[0];
                  var config2 = this._config;
                  var total = config2.total;
                  var reverse = config2.reverse;
                  if (from < 1 && !reverse) {
                    from = 1;
                  }
                  for (var i = from; i < total; i++) {
                    if (reverse) {
                      if (i === 0) {
                        this._itemPositions[0] = this._scrollHeight - this._itemHeights[0];
                      } else {
                        this._itemPositions[i] = this._itemPositions[i - 1] - this._itemHeights[i];
                      }
                    } else {
                      this._itemPositions[i] = this._itemHeights[i - 1] + this._itemPositions[i - 1];
                    }
                  }
                }
              }, {
                key: "_computeScrollHeight",
                value: function _computeScrollHeight() {
                  var _this3 = this;
                  var config2 = this._config;
                  var total = config2.total;
                  var scrollHeight = this._itemHeights.reduce(function(a, b) {
                    return a + b;
                  }, 0);
                  HyperList3.mergeStyle(this._scroller, {
                    opacity: 0,
                    position: "absolute",
                    width: "1px",
                    height: scrollHeight + "px"
                  });
                  var sortedItemHeights = this._itemHeights.slice(0).sort(function(a, b) {
                    return a - b;
                  });
                  var middle = Math.floor(total / 2);
                  var averageHeight = total % 2 === 0 ? (sortedItemHeights[middle] + sortedItemHeights[middle - 1]) / 2 : sortedItemHeights[middle];
                  var containerHeight = this._element.clientHeight ? this._element.clientHeight : this._containerHeight;
                  this._screenItemsLen = Math.ceil(containerHeight / averageHeight);
                  this._containerHeight = containerHeight;
                  this._cachedItemsLen = Math.max(this._cachedItemsLen || 0, this._screenItemsLen * 3);
                  this._averageHeight = averageHeight;
                  if (config2.reverse) {
                    window.requestAnimationFrame(function() {
                      _this3._element.scrollTop = scrollHeight;
                    });
                  }
                  return scrollHeight;
                }
              }, {
                key: "_getFrom",
                value: function _getFrom(scrollTop) {
                  var i = 0;
                  while (this._itemPositions[i] < scrollTop) {
                    i++;
                  }
                  return i;
                }
              }, {
                key: "_getReverseFrom",
                value: function _getReverseFrom(scrollTop) {
                  var i = this._config.total - 1;
                  while (i > 0 && this._itemPositions[i] < scrollTop + this._containerHeight) {
                    i--;
                  }
                  return i;
                }
              }]);
              return HyperList3;
            }();
            exports3.default = HyperList2;
            module3.exports = exports3["default"];
          }, {}] }, {}, [1])(1);
        });
      });
      var HyperList = unwrapExports(hyperlist);
      var BodyRenderer = class {
        constructor(instance) {
          this.instance = instance;
          this.options = instance.options;
          this.datamanager = instance.datamanager;
          this.rowmanager = instance.rowmanager;
          this.cellmanager = instance.cellmanager;
          this.bodyScrollable = instance.bodyScrollable;
          this.footer = this.instance.footer;
          this.log = instance.log;
        }
        renderRows(rows) {
          this.visibleRows = rows;
          this.visibleRowIndices = rows.map((row) => row.meta.rowIndex);
          if (rows.length === 0) {
            this.bodyScrollable.innerHTML = this.getNoDataHTML();
            return;
          }
          let visibleRowIndicesSet = new Set(this.visibleRowIndices);
          const rowViewOrder = this.datamanager.rowViewOrder.map((index) => {
            if (visibleRowIndicesSet.has(index)) {
              return index;
            }
            return null;
          }).filter((index) => index !== null);
          const computedStyle = getComputedStyle(this.bodyScrollable);
          let config2 = {
            width: computedStyle.width,
            height: computedStyle.height,
            itemHeight: this.options.cellHeight,
            total: rows.length,
            generate: (index) => {
              const el = document.createElement("div");
              const rowIndex = rowViewOrder[index];
              const row = this.datamanager.getRow(rowIndex);
              const rowHTML = this.rowmanager.getRowHTML(row, row.meta);
              el.innerHTML = rowHTML;
              return el.children[0];
            },
            afterRender: () => {
              this.restoreState();
            }
          };
          if (!this.hyperlist) {
            this.hyperlist = new HyperList(this.bodyScrollable, config2);
          } else {
            this.hyperlist.refresh(this.bodyScrollable, config2);
          }
          this.renderFooter();
        }
        render() {
          const rows = this.datamanager.getRowsForView();
          this.renderRows(rows);
          this.instance.setDimensions();
        }
        renderFooter() {
          if (!this.options.showTotalRow)
            return;
          const totalRow = this.getTotalRow();
          let html = this.rowmanager.getRowHTML(totalRow, { isTotalRow: 1, rowIndex: "totalRow" });
          this.footer.innerHTML = html;
        }
        getTotalRow() {
          const columns = this.datamanager.getColumns();
          const totalRowTemplate = columns.map((col) => {
            let content = null;
            if (["_rowIndex", "_checkbox"].includes(col.id)) {
              content = "";
            }
            return {
              content,
              isTotalRow: 1,
              colIndex: col.colIndex,
              column: col
            };
          });
          const totalRow = totalRowTemplate.map((cell, i) => {
            if (cell.content === "")
              return cell;
            if (this.options.hooks.columnTotal) {
              const columnValues = this.visibleRows.map((row) => row[i].content);
              const result = this.options.hooks.columnTotal.call(this.instance, columnValues, cell);
              if (result != null) {
                cell.content = result;
                return cell;
              }
            }
            cell.content = this.visibleRows.reduce((acc, prevRow) => {
              const prevCell = prevRow[i];
              if (typeof prevCell.content === "number") {
                if (acc == null)
                  acc = 0;
                return acc + prevCell.content;
              }
              return acc;
            }, cell.content);
            return cell;
          });
          return totalRow;
        }
        restoreState() {
          this.rowmanager.highlightCheckedRows();
          this.cellmanager.selectAreaOnClusterChanged();
          this.cellmanager.focusCellOnClusterChanged();
        }
        showToastMessage(message, hideAfter) {
          this.instance.toastMessage.innerHTML = this.getToastMessageHTML(message);
          if (hideAfter) {
            setTimeout(() => {
              this.clearToastMessage();
            }, hideAfter * 1e3);
          }
        }
        clearToastMessage() {
          this.instance.toastMessage.innerHTML = "";
        }
        getNoDataHTML() {
          return `<div class="dt-scrollable__no-data">${this.options.noDataMessage}</div>`;
        }
        getToastMessageHTML(message) {
          return `<span class="dt-toast__message">${message}</span>`;
        }
      };
      var Style = class {
        constructor(instance) {
          this.instance = instance;
          linkProperties(this, this.instance, [
            "options",
            "datamanager",
            "columnmanager",
            "header",
            "footer",
            "bodyScrollable",
            "datatableWrapper",
            "getColumn",
            "bodyRenderer"
          ]);
          this.scopeClass = "dt-instance-" + instance.constructor.instances;
          instance.datatableWrapper.classList.add(this.scopeClass);
          const styleEl = document.createElement("style");
          instance.wrapper.insertBefore(styleEl, instance.datatableWrapper);
          this.styleEl = styleEl;
          this.bindResizeWindow();
          this.bindScrollHeader();
        }
        get stylesheet() {
          return this.styleEl.sheet;
        }
        bindResizeWindow() {
          this.onWindowResize = this.onWindowResize.bind(this);
          this.onWindowResize = throttle$1(this.onWindowResize, 300);
          if (this.options.layout === "fluid") {
            $2.on(window, "resize", this.onWindowResize);
          }
        }
        bindScrollHeader() {
          this._settingHeaderPosition = false;
          $2.on(this.bodyScrollable, "scroll", (e) => {
            if (this._settingHeaderPosition)
              return;
            this._settingHeaderPosition = true;
            requestAnimationFrame(() => {
              const left = -e.target.scrollLeft;
              $2.style(this.header, {
                transform: `translateX(${left}px)`
              });
              $2.style(this.footer, {
                transform: `translateX(${left}px)`
              });
              this._settingHeaderPosition = false;
            });
          });
        }
        onWindowResize() {
          this.distributeRemainingWidth();
          this.refreshColumnWidth();
          this.setBodyStyle();
        }
        destroy() {
          this.styleEl.remove();
          $2.off(window, "resize", this.onWindowResize);
        }
        setStyle(selector, styleObject) {
          if (selector.includes(",")) {
            selector.split(",").map((s) => s.trim()).forEach((selector2) => {
              this.setStyle(selector2, styleObject);
            });
            return;
          }
          selector = selector.trim();
          if (!selector)
            return;
          this._styleRulesMap = this._styleRulesMap || {};
          const prefixedSelector = this._getPrefixedSelector(selector);
          if (this._styleRulesMap[prefixedSelector]) {
            this.removeStyle(selector);
            styleObject = Object.assign({}, this._styleRulesMap[prefixedSelector], styleObject);
          }
          const styleString = this._getRuleString(styleObject);
          const ruleString = `${prefixedSelector} { ${styleString} }`;
          this._styleRulesMap[prefixedSelector] = styleObject;
          this.stylesheet.insertRule(ruleString);
        }
        removeStyle(selector) {
          if (selector.includes(",")) {
            selector.split(",").map((s) => s.trim()).forEach((selector2) => {
              this.removeStyle(selector2);
            });
            return;
          }
          selector = selector.trim();
          if (!selector)
            return;
          const prefixedSelector = this._getPrefixedSelector(selector);
          const index = Array.from(this.stylesheet.cssRules).findIndex((rule) => rule.selectorText === prefixedSelector);
          if (index === -1)
            return;
          this.stylesheet.deleteRule(index);
        }
        _getPrefixedSelector(selector) {
          return `.${this.scopeClass} ${selector}`;
        }
        _getRuleString(styleObject) {
          return Object.keys(styleObject).map((prop) => {
            let dashed = prop;
            if (!prop.includes("-")) {
              dashed = camelCaseToDash(prop);
            }
            return `${dashed}:${styleObject[prop]};`;
          }).join("");
        }
        setDimensions() {
          this.setCellHeight();
          this.setupMinWidth();
          this.setupNaturalColumnWidth();
          this.setupColumnWidth();
          this.distributeRemainingWidth();
          this.setColumnStyle();
          this.setBodyStyle();
        }
        setCellHeight() {
          this.setStyle(".dt-cell", {
            height: this.options.cellHeight + "px"
          });
        }
        setupMinWidth() {
          $2.each(".dt-cell--header", this.header).map((col) => {
            const { colIndex } = $2.data(col);
            const column = this.getColumn(colIndex);
            if (!column.minWidth) {
              const width = $2.style($2(".dt-cell__content", col), "width");
              column.minWidth = width;
            }
          });
        }
        setupNaturalColumnWidth() {
          if (!$2(".dt-row"))
            return;
          $2.each(".dt-row-header .dt-cell", this.header).map(($headerCell) => {
            const { colIndex } = $2.data($headerCell);
            const column = this.datamanager.getColumn(colIndex);
            let width = $2.style($2(".dt-cell__content", $headerCell), "width");
            if (typeof width === "number" && width >= this.options.minimumColumnWidth) {
              column.naturalWidth = width;
            } else {
              column.naturalWidth = this.options.minimumColumnWidth;
            }
          });
          $2.each(".dt-row-0 .dt-cell", this.bodyScrollable).map(($cell) => {
            const {
              colIndex
            } = $2.data($cell);
            const column = this.datamanager.getColumn(colIndex);
            let naturalWidth = $2.style($2(".dt-cell__content", $cell), "width");
            if (typeof naturalWidth === "number" && naturalWidth >= column.naturalWidth) {
              column.naturalWidth = naturalWidth;
            } else {
              column.naturalWidth = column.naturalWidth;
            }
          });
        }
        setupColumnWidth() {
          if (this.options.layout === "ratio") {
            let totalWidth = $2.style(this.datatableWrapper, "width");
            if (this.options.serialNoColumn) {
              const rowIndexColumn = this.datamanager.getColumnById("_rowIndex");
              totalWidth = totalWidth - rowIndexColumn.width - 1;
            }
            if (this.options.checkboxColumn) {
              const rowIndexColumn = this.datamanager.getColumnById("_checkbox");
              totalWidth = totalWidth - rowIndexColumn.width - 1;
            }
            const totalParts = this.datamanager.getColumns().map((column) => {
              if (column.id === "_rowIndex" || column.id === "_checkbox") {
                return 0;
              }
              if (!column.width) {
                column.width = 1;
              }
              column.ratioWidth = parseInt(column.width, 10);
              return column.ratioWidth;
            }).reduce((a, c) => a + c);
            const onePart = totalWidth / totalParts;
            this.datamanager.getColumns().map((column) => {
              if (column.id === "_rowIndex" || column.id === "_checkbox")
                return;
              column.width = Math.floor(onePart * column.ratioWidth) - 1;
            });
          } else {
            this.datamanager.getColumns().map((column) => {
              if (!column.width) {
                column.width = column.naturalWidth;
              }
              if (column.id === "_rowIndex") {
                column.width = this.getRowIndexColumnWidth();
              }
              if (column.width < this.options.minimumColumnWidth) {
                column.width = this.options.minimumColumnWidth;
              }
            });
          }
        }
        distributeRemainingWidth() {
          if (this.options.layout !== "fluid")
            return;
          const wrapperWidth = $2.style(this.instance.datatableWrapper, "width");
          let firstRow = $2(".dt-row", this.bodyScrollable);
          let firstRowWidth = wrapperWidth;
          if (!firstRow) {
            let headerRow = $2(".dt-row", this.instance.header);
            let cellWidths = Array.from(headerRow.children).map((cell) => cell.offsetWidth);
            firstRowWidth = cellWidths.reduce((sum, a) => sum + a, 0);
          } else {
            firstRowWidth = $2.style(firstRow, "width");
          }
          const resizableColumns = this.datamanager.getColumns().filter((col) => col.resizable);
          const deltaWidth = (wrapperWidth - firstRowWidth) / resizableColumns.length;
          resizableColumns.map((col) => {
            const width = $2.style(this.getColumnHeaderElement(col.colIndex), "width");
            let finalWidth = Math.floor(width + deltaWidth) - 2;
            this.datamanager.updateColumn(col.colIndex, {
              width: finalWidth
            });
          });
        }
        setColumnStyle() {
          this.datamanager.getColumns().map((column) => {
            if (!column.align) {
              column.align = "left";
            }
            if (!["left", "center", "right"].includes(column.align)) {
              column.align = "left";
            }
            this.setStyle(`.dt-cell--col-${column.colIndex}`, {
              "text-align": column.align
            });
            this.columnmanager.setColumnHeaderWidth(column.colIndex);
            this.columnmanager.setColumnWidth(column.colIndex);
          });
        }
        refreshColumnWidth() {
          this.datamanager.getColumns().map((column) => {
            this.columnmanager.setColumnHeaderWidth(column.colIndex);
            this.columnmanager.setColumnWidth(column.colIndex);
          });
        }
        setBodyStyle() {
          const bodyWidth = $2.style(this.datatableWrapper, "width");
          const firstRow = $2(".dt-row", this.bodyScrollable);
          if (!firstRow)
            return;
          const rowWidth = $2.style(firstRow, "width");
          let width = bodyWidth > rowWidth ? rowWidth + 10 : bodyWidth;
          $2.style(this.bodyScrollable, {
            width: width + "px"
          });
          $2.removeStyle(this.bodyScrollable, "height");
          let bodyHeight = $2.getStyle(this.bodyScrollable, "height");
          const scrollHeight = (this.bodyRenderer.hyperlist || {})._scrollHeight || Infinity;
          const hasHorizontalOverflow = $2.hasHorizontalOverflow(this.bodyScrollable);
          let height;
          if (scrollHeight < bodyHeight) {
            height = scrollHeight;
            if (hasHorizontalOverflow) {
              height += $2.scrollbarSize();
            }
            $2.style(this.bodyScrollable, {
              height: height + "px"
            });
          }
          const verticalOverflow = this.bodyScrollable.scrollHeight - this.bodyScrollable.offsetHeight;
          if (verticalOverflow < $2.scrollbarSize()) {
            $2.style(this.bodyScrollable, {
              overflowY: "hidden"
            });
          }
          if (this.options.layout === "fluid") {
            $2.style(this.bodyScrollable, {
              overflowX: "hidden"
            });
          }
        }
        getColumnHeaderElement(colIndex) {
          colIndex = +colIndex;
          if (colIndex < 0)
            return null;
          return $2(`.dt-cell--col-${colIndex}`, this.header);
        }
        getRowIndexColumnWidth() {
          const rowCount = this.datamanager.getRowCount();
          const padding = 22;
          return $2.measureTextWidth(rowCount + "") + padding;
        }
      };
      var KEYCODES = {
        13: "enter",
        91: "meta",
        16: "shift",
        17: "ctrl",
        18: "alt",
        37: "left",
        38: "up",
        39: "right",
        40: "down",
        9: "tab",
        27: "esc",
        67: "c",
        70: "f",
        86: "v"
      };
      var Keyboard = class {
        constructor(element) {
          this.listeners = {};
          $2.on(element, "keydown", this.handler.bind(this));
        }
        handler(e) {
          let key = KEYCODES[e.keyCode];
          if (e.shiftKey && key !== "shift") {
            key = "shift+" + key;
          }
          if (e.ctrlKey && key !== "ctrl" || e.metaKey && key !== "meta") {
            key = "ctrl+" + key;
          }
          const listeners = this.listeners[key];
          if (listeners && listeners.length > 0) {
            for (let listener of listeners) {
              const preventBubbling = listener(e);
              if (preventBubbling === void 0 || preventBubbling === true) {
                e.preventDefault();
              }
            }
          }
        }
        on(key, listener) {
          const keys = key.split(",").map((k) => k.trim());
          keys.map((key2) => {
            this.listeners[key2] = this.listeners[key2] || [];
            this.listeners[key2].push(listener);
          });
        }
      };
      var en = {
        "Sort Ascending": "Sort Ascending",
        "Sort Descending": "Sort Descending",
        "Reset sorting": "Reset sorting",
        "Remove column": "Remove column",
        "No Data": "No Data",
        "{count} cells copied": { "1": "{count} cell copied", "default": "{count} cells copied" },
        "{count} rows selected": { "1": "{count} row selected", "default": "{count} rows selected" }
      };
      var de = {
        "Sort Ascending": "Aufsteigend sortieren",
        "Sort Descending": "Absteigend sortieren",
        "Reset sorting": "Sortierung zur\xFCcksetzen",
        "Remove column": "Spalte entfernen",
        "No Data": "Keine Daten",
        "{count} cells copied": { "1": "{count} Zelle kopiert", "default": "{count} Zellen kopiert" },
        "{count} rows selected": { "1": "{count} Zeile ausgew\xE4hlt", "default": "{count} Zeilen ausgew\xE4hlt" }
      };
      var fr = {
        "Sort Ascending": "Trier par ordre croissant",
        "Sort Descending": "Trier par ordre d\xE9croissant",
        "Reset sorting": "R\xE9initialiser le tri",
        "Remove column": "Supprimer colonne",
        "No Data": "Pas de donn\xE9es",
        "{count} cells copied": { "1": "{count} cellule copi\xE9e", "default": "{count} cellules copi\xE9es" },
        "{count} rows selected": { "1": "{count} ligne s\xE9lectionn\xE9e", "default": "{count} lignes s\xE9lectionn\xE9es" }
      };
      var it = {
        "Sort Ascending": "Ordinamento ascendente",
        "Sort Descending": "Ordinamento decrescente",
        "Reset sorting": "Azzeramento ordinamento",
        "Remove column": "Rimuovi colonna",
        "No Data": "Nessun dato",
        "{count} cells copied": { "1": "Copiato {count} cella", "default": "{count} celle copiate" },
        "{count} rows selected": { "1": "{count} linea selezionata", "default": "{count} linee selezionate" }
      };
      function getTranslations() {
        return {
          en,
          de,
          fr,
          it
        };
      }
      var TranslationManager = class {
        constructor(language) {
          this.language = language;
          this.translations = getTranslations();
        }
        addTranslations(translations) {
          this.translations = Object.assign(this.translations, translations);
        }
        translate(sourceText, args) {
          let translation = this.translations[this.language] && this.translations[this.language][sourceText] || sourceText;
          if (typeof translation === "object") {
            translation = args && args.count ? this.getPluralizedTranslation(translation, args.count) : sourceText;
          }
          return format(translation, args || {});
        }
        getPluralizedTranslation(translations, count) {
          return translations[count] || translations["default"];
        }
      };
      function filterRows(rows, filters, data) {
        let filteredRowIndices = [];
        if (Object.keys(filters).length === 0) {
          return rows.map((row) => row.meta.rowIndex);
        }
        for (let colIndex in filters) {
          const keyword = filters[colIndex];
          const filteredRows = filteredRowIndices.length ? filteredRowIndices.map((i) => rows[i]) : rows;
          const cells = filteredRows.map((row) => row[colIndex]);
          let filter = guessFilter(keyword);
          let filterMethod = getFilterMethod(rows, data, filter);
          if (filterMethod) {
            filteredRowIndices = filterMethod(filter.text, cells);
          } else {
            filteredRowIndices = cells.map((cell) => cell.rowIndex);
          }
        }
        return filteredRowIndices;
      }
      function getFilterMethod(rows, allData, filter) {
        const getFormattedValue = (cell) => {
          let formatter = CellManager.getCustomCellFormatter(cell);
          let rowData = rows[cell.rowIndex];
          if (allData && allData.data && allData.data.length) {
            rowData = allData.data[cell.rowIndex];
          }
          if (formatter && cell.content) {
            cell.html = formatter(cell.content, rows[cell.rowIndex], cell.column, rowData, filter);
            return stripHTML(cell.html);
          }
          return cell.content || "";
        };
        const stringCompareValue = (cell) => String(stripHTML(cell.html || "") || getFormattedValue(cell)).toLowerCase();
        const numberCompareValue = (cell) => parseFloat(cell.content);
        const getCompareValues = (cell, keyword) => {
          if (cell.column.compareValue) {
            const compareValues = cell.column.compareValue(cell, keyword);
            if (compareValues && Array.isArray(compareValues))
              return compareValues;
          }
          const float = numberCompareValue(cell);
          if (!isNaN(float)) {
            return [float, keyword];
          }
          return [stringCompareValue(cell), keyword];
        };
        let filterMethodMap = {
          contains(keyword, cells) {
            return cells.filter((cell) => {
              const needle = (keyword || "").toLowerCase();
              return !needle || (cell.content || "").toLowerCase().includes(needle) || stringCompareValue(cell).includes(needle);
            }).map((cell) => cell.rowIndex);
          },
          greaterThan(keyword, cells) {
            return cells.filter((cell) => {
              const [compareValue, keywordValue] = getCompareValues(cell, keyword);
              return compareValue > keywordValue;
            }).map((cell) => cell.rowIndex);
          },
          lessThan(keyword, cells) {
            return cells.filter((cell) => {
              const [compareValue, keywordValue] = getCompareValues(cell, keyword);
              return compareValue < keywordValue;
            }).map((cell) => cell.rowIndex);
          },
          equals(keyword, cells) {
            return cells.filter((cell) => {
              const value = parseFloat(cell.content);
              return value === keyword;
            }).map((cell) => cell.rowIndex);
          },
          notEquals(keyword, cells) {
            return cells.filter((cell) => {
              const value = parseFloat(cell.content);
              return value !== keyword;
            }).map((cell) => cell.rowIndex);
          },
          range(rangeValues, cells) {
            return cells.filter((cell) => {
              const values1 = getCompareValues(cell, rangeValues[0]);
              const values2 = getCompareValues(cell, rangeValues[1]);
              const value = values1[0];
              return value >= values1[1] && value <= values2[1];
            }).map((cell) => cell.rowIndex);
          },
          containsNumber(keyword, cells) {
            return cells.filter((cell) => {
              let number = parseFloat(keyword, 10);
              let string = keyword;
              let hayNumber = numberCompareValue(cell);
              let hayString = stringCompareValue(cell);
              return number === hayNumber || hayString.includes(string);
            }).map((cell) => cell.rowIndex);
          }
        };
        return filterMethodMap[filter.type];
      }
      function guessFilter(keyword = "") {
        if (keyword.length === 0)
          return {};
        let compareString = keyword;
        if ([">", "<", "="].includes(compareString[0])) {
          compareString = keyword.slice(1);
        } else if (compareString.startsWith("!=")) {
          compareString = keyword.slice(2);
        }
        if (keyword.startsWith(">")) {
          if (compareString) {
            return {
              type: "greaterThan",
              text: compareString.trim()
            };
          }
        }
        if (keyword.startsWith("<")) {
          if (compareString) {
            return {
              type: "lessThan",
              text: compareString.trim()
            };
          }
        }
        if (keyword.startsWith("=")) {
          if (isNumber(compareString)) {
            return {
              type: "equals",
              text: Number(keyword.slice(1).trim())
            };
          }
        }
        if (isNumber(compareString)) {
          return {
            type: "containsNumber",
            text: compareString
          };
        }
        if (keyword.startsWith("!=")) {
          if (isNumber(compareString)) {
            return {
              type: "notEquals",
              text: Number(keyword.slice(2).trim())
            };
          }
        }
        if (keyword.split(":").length === 2 && keyword.split(":").every((v) => isNumber(v.trim()))) {
          compareString = keyword.split(":");
          return {
            type: "range",
            text: compareString.map((v) => v.trim())
          };
        }
        return {
          type: "contains",
          text: compareString.toLowerCase()
        };
      }
      function getDefaultOptions(instance) {
        return {
          columns: [],
          data: [],
          dropdownButton: icons.chevronDown,
          headerDropdown: [
            {
              label: instance.translate("Sort Ascending"),
              action: function(column) {
                this.sortColumn(column.colIndex, "asc");
              }
            },
            {
              label: instance.translate("Sort Descending"),
              action: function(column) {
                this.sortColumn(column.colIndex, "desc");
              }
            },
            {
              label: instance.translate("Reset sorting"),
              action: function(column) {
                this.sortColumn(column.colIndex, "none");
              }
            },
            {
              label: instance.translate("Remove column"),
              action: function(column) {
                this.removeColumn(column.colIndex);
              }
            }
          ],
          events: {
            onRemoveColumn(column) {
            },
            onSwitchColumn(column1, column2) {
            },
            onSortColumn(column) {
            },
            onCheckRow(row) {
            },
            onDestroy() {
            }
          },
          hooks: {
            columnTotal: null
          },
          sortIndicator: {
            asc: "\u2191",
            desc: "\u2193",
            none: ""
          },
          overrideComponents: {},
          filterRows,
          freezeMessage: "",
          getEditor: null,
          serialNoColumn: true,
          checkboxColumn: false,
          clusterize: true,
          logs: false,
          layout: "fixed",
          noDataMessage: instance.translate("No Data"),
          cellHeight: 40,
          minimumColumnWidth: 30,
          inlineFilters: false,
          treeView: false,
          checkedRowStatus: true,
          dynamicRowHeight: false,
          pasteFromClipboard: false,
          showTotalRow: false,
          direction: "ltr",
          disableReorderColumn: false
        };
      }
      var defaultComponents = {
        DataManager,
        CellManager,
        ColumnManager,
        RowManager,
        BodyRenderer,
        Style,
        Keyboard
      };
      var DataTable2 = class {
        constructor(wrapper, options) {
          DataTable2.instances++;
          if (typeof wrapper === "string") {
            wrapper = document.querySelector(wrapper);
          }
          this.wrapper = wrapper;
          if (!(this.wrapper instanceof HTMLElement)) {
            throw new Error("Invalid argument given for `wrapper`");
          }
          this.initializeTranslations(options);
          this.setDefaultOptions();
          this.buildOptions(options);
          this.prepare();
          this.initializeComponents();
          if (this.options.data) {
            this.refresh();
            this.columnmanager.applyDefaultSortOrder();
          }
        }
        initializeTranslations(options) {
          this.language = options.language || "en";
          this.translationManager = new TranslationManager(this.language);
          if (options.translations) {
            this.translationManager.addTranslations(options.translations);
          }
        }
        setDefaultOptions() {
          this.DEFAULT_OPTIONS = getDefaultOptions(this);
        }
        buildOptions(options) {
          this.options = this.options || {};
          this.options = Object.assign(
            {},
            this.DEFAULT_OPTIONS,
            this.options || {},
            options
          );
          options.headerDropdown = options.headerDropdown || [];
          this.options.headerDropdown = [
            ...this.DEFAULT_OPTIONS.headerDropdown,
            ...options.headerDropdown
          ];
          this.events = Object.assign(
            {},
            this.DEFAULT_OPTIONS.events,
            this.options.events || {},
            options.events || {}
          );
          this.fireEvent = this.fireEvent.bind(this);
        }
        prepare() {
          this.prepareDom();
          this.unfreeze();
        }
        initializeComponents() {
          let components = Object.assign({}, defaultComponents, this.options.overrideComponents);
          let {
            Style: Style$$1,
            Keyboard: Keyboard$$1,
            DataManager: DataManager$$1,
            RowManager: RowManager$$1,
            ColumnManager: ColumnManager$$1,
            CellManager: CellManager$$1,
            BodyRenderer: BodyRenderer$$1
          } = components;
          this.style = new Style$$1(this);
          this.keyboard = new Keyboard$$1(this.wrapper);
          this.datamanager = new DataManager$$1(this.options);
          this.rowmanager = new RowManager$$1(this);
          this.columnmanager = new ColumnManager$$1(this);
          this.cellmanager = new CellManager$$1(this);
          this.bodyRenderer = new BodyRenderer$$1(this);
        }
        prepareDom() {
          this.wrapper.innerHTML = `
            <div class="datatable" dir="${this.options.direction}">
                <div class="dt-header"></div>
                <div class="dt-scrollable"></div>
                <div class="dt-footer"></div>
                <div class="dt-freeze">
                    <span class="dt-freeze__message">
                        ${this.options.freezeMessage}
                    </span>
                </div>
                <div class="dt-toast"></div>
                <div class="dt-dropdown-container"></div>
                <textarea class="dt-paste-target"></textarea>
            </div>
        `;
          this.datatableWrapper = $2(".datatable", this.wrapper);
          this.header = $2(".dt-header", this.wrapper);
          this.footer = $2(".dt-footer", this.wrapper);
          this.bodyScrollable = $2(".dt-scrollable", this.wrapper);
          this.freezeContainer = $2(".dt-freeze", this.wrapper);
          this.toastMessage = $2(".dt-toast", this.wrapper);
          this.pasteTarget = $2(".dt-paste-target", this.wrapper);
          this.dropdownContainer = $2(".dt-dropdown-container", this.wrapper);
        }
        refresh(data, columns) {
          this.datamanager.init(data, columns);
          this.render();
          this.setDimensions();
        }
        destroy() {
          this.wrapper.innerHTML = "";
          this.style.destroy();
          this.fireEvent("onDestroy");
        }
        appendRows(rows) {
          this.datamanager.appendRows(rows);
          this.rowmanager.refreshRows();
        }
        refreshRow(row, rowIndex) {
          this.rowmanager.refreshRow(row, rowIndex);
        }
        render() {
          this.renderHeader();
          this.renderBody();
        }
        renderHeader() {
          this.columnmanager.renderHeader();
        }
        renderBody() {
          this.bodyRenderer.render();
        }
        setDimensions() {
          this.style.setDimensions();
        }
        showToastMessage(message, hideAfter) {
          this.bodyRenderer.showToastMessage(message, hideAfter);
        }
        clearToastMessage() {
          this.bodyRenderer.clearToastMessage();
        }
        getColumn(colIndex) {
          return this.datamanager.getColumn(colIndex);
        }
        getColumns() {
          return this.datamanager.getColumns();
        }
        getRows() {
          return this.datamanager.getRows();
        }
        getCell(colIndex, rowIndex) {
          return this.datamanager.getCell(colIndex, rowIndex);
        }
        getColumnHeaderElement(colIndex) {
          return this.columnmanager.getColumnHeaderElement(colIndex);
        }
        getViewportHeight() {
          if (!this.viewportHeight) {
            this.viewportHeight = $2.style(this.bodyScrollable, "height");
          }
          return this.viewportHeight;
        }
        sortColumn(colIndex, sortOrder) {
          this.columnmanager.sortColumn(colIndex, sortOrder);
        }
        removeColumn(colIndex) {
          this.columnmanager.removeColumn(colIndex);
        }
        scrollToLastColumn() {
          this.datatableWrapper.scrollLeft = 9999;
        }
        freeze() {
          $2.style(this.freezeContainer, {
            display: ""
          });
        }
        unfreeze() {
          $2.style(this.freezeContainer, {
            display: "none"
          });
        }
        updateOptions(options) {
          this.buildOptions(options);
        }
        fireEvent(eventName, ...args) {
          const handlers = [
            ...this._internalEventHandlers[eventName] || [],
            this.events[eventName]
          ].filter(Boolean);
          for (let handler of handlers) {
            handler.apply(this, args);
          }
        }
        on(event, handler) {
          this._internalEventHandlers = this._internalEventHandlers || {};
          this._internalEventHandlers[event] = this._internalEventHandlers[event] || [];
          this._internalEventHandlers[event].push(handler);
        }
        log() {
          if (this.options.logs) {
            console.log.apply(console, arguments);
          }
        }
        translate(str, args) {
          return this.translationManager.translate(str, args);
        }
      };
      DataTable2.instances = 0;
      var name = "frappe-datatable";
      var version = "0.0.0-development";
      var description = "A modern datatable library for the web";
      var main = "dist/frappe-datatable.cjs.js";
      var unpkg = "dist/frappe-datatable.min.js";
      var jsdelivr = "dist/frappe-datatable.min.js";
      var scripts = { "start": "yarn run dev", "build": "rollup -c && NODE_ENV=production rollup -c", "dev": "rollup -c -w", "cy:server": "http-server -p 8989", "cy:open": "cypress open", "cy:run": "cypress run", "test": "start-server-and-test cy:server http://localhost:8989 cy:run", "test-local": "start-server-and-test cy:server http://localhost:8989 cy:open", "travis-deploy-once": "travis-deploy-once", "semantic-release": "semantic-release", "lint": "eslint src", "lint-and-build": "yarn lint && yarn build", "commit": "npx git-cz" };
      var files = ["dist", "src"];
      var devDependencies = { "autoprefixer": "^9.0.0", "chai": "3.5.0", "cypress": "^9.2.0", "cz-conventional-changelog": "^2.1.0", "deepmerge": "^2.0.1", "eslint": "^5.0.1", "eslint-config-airbnb": "^16.1.0", "eslint-config-airbnb-base": "^12.1.0", "eslint-plugin-import": "^2.11.0", "http-server": "^0.11.1", "mocha": "3.3.0", "postcss-custom-properties": "^7.0.0", "postcss-nested": "^3.0.0", "rollup": "^0.59.4", "rollup-plugin-commonjs": "^8.3.0", "rollup-plugin-eslint": "^4.0.0", "rollup-plugin-json": "^2.3.0", "rollup-plugin-node-resolve": "^3.0.3", "rollup-plugin-postcss": "^1.2.8", "rollup-plugin-uglify-es": "^0.0.1", "semantic-release": "^17.1.1", "start-server-and-test": "^1.4.1", "travis-deploy-once": "^5.0.1" };
      var repository = { "type": "git", "url": "https://github.com/frappe/datatable.git" };
      var keywords = ["datatable", "data", "grid", "table"];
      var author = "Faris Ansari";
      var license = "MIT";
      var bugs = { "url": "https://github.com/frappe/datatable/issues" };
      var homepage = "https://frappe.io/datatable";
      var dependencies = { "hyperlist": "^1.0.0-beta", "lodash": "^4.17.5", "sortablejs": "^1.7.0" };
      var config = { "commitizen": { "path": "cz-conventional-changelog" } };
      var packageJson = {
        name,
        version,
        description,
        main,
        unpkg,
        jsdelivr,
        scripts,
        files,
        devDependencies,
        repository,
        keywords,
        author,
        license,
        bugs,
        homepage,
        dependencies,
        config
      };
      DataTable2.__version__ = packageJson.version;
      module.exports = DataTable2;
    }
  });

  // frappe/public/js/frappe/data_import/import_preview.js
  var import_frappe_datatable = __toESM(require_frappe_datatable_cjs());

  // frappe/public/js/frappe/data_import/data_exporter.js
  frappe.provide("frappe.data_import");
  frappe.data_import.DataExporter = class DataExporter {
    constructor(doctype, exporting_for) {
      this.doctype = doctype;
      this.exporting_for = exporting_for;
      frappe.model.with_doctype(doctype, () => {
        this.make_dialog();
      });
    }
    make_dialog() {
      this.dialog = new frappe.ui.Dialog({
        title: __("Export Data"),
        fields: [
          {
            fieldtype: "Select",
            fieldname: "file_type",
            label: __("File Type"),
            options: ["Excel", "CSV"],
            default: "CSV"
          },
          {
            fieldtype: "Select",
            fieldname: "export_records",
            label: __("Export Type"),
            options: [
              {
                label: __("All Records"),
                value: "all"
              },
              {
                label: __("Filtered Records"),
                value: "by_filter"
              },
              {
                label: __("5 Records"),
                value: "5_records"
              },
              {
                label: __("Blank Template"),
                value: "blank_template"
              }
            ],
            default: this.exporting_for === "Insert New Records" ? "blank_template" : "all",
            change: () => {
              this.update_record_count_message();
            }
          },
          {
            fieldtype: "HTML",
            fieldname: "filter_area",
            depends_on: (doc) => doc.export_records === "by_filter"
          },
          {
            fieldtype: "Section Break"
          },
          {
            fieldtype: "HTML",
            fieldname: "select_all_buttons"
          },
          {
            label: __(this.doctype),
            fieldname: this.doctype,
            fieldtype: "MultiCheck",
            columns: 2,
            on_change: () => this.update_primary_action(),
            options: this.get_multicheck_options(this.doctype),
            sort_options: false
          },
          ...frappe.meta.get_table_fields(this.doctype).map((df) => {
            let doctype = df.options;
            let child_fieldname = df.fieldname;
            let label = df.reqd ? __("{0} ({1}) (1 row mandatory)", [__(df.label || df.fieldname, null, df.parent), __(doctype)]) : __("{0} ({1})", [
              __(df.label || df.fieldname, null, df.parent),
              __(doctype)
            ]);
            return {
              label,
              fieldname: child_fieldname,
              fieldtype: "MultiCheck",
              columns: 2,
              on_change: () => this.update_primary_action(),
              options: this.get_multicheck_options(doctype, child_fieldname)
            };
          })
        ],
        primary_action_label: __("Export"),
        primary_action: (values) => this.export_records(values),
        on_page_show: () => this.select_mandatory()
      });
      this.make_filter_area();
      this.make_select_all_buttons();
      this.update_record_count_message();
      this.dialog.show();
    }
    export_records() {
      let method = "/api/method/frappe.core.doctype.data_import.data_import.download_template";
      let multicheck_fields = this.dialog.fields.filter((df) => df.fieldtype === "MultiCheck").map((df) => df.fieldname);
      let values = this.dialog.get_values();
      let doctype_field_map = Object.assign({}, values);
      for (let key in doctype_field_map) {
        if (!multicheck_fields.includes(key)) {
          delete doctype_field_map[key];
        }
      }
      let filters = null;
      if (values.export_records === "by_filter") {
        filters = this.get_filters();
      }
      open_url_post(method, {
        doctype: this.doctype,
        file_type: values.file_type,
        export_records: values.export_records,
        export_fields: doctype_field_map,
        export_filters: filters
      });
    }
    make_filter_area() {
      this.filter_group = new frappe.ui.FilterGroup({
        parent: this.dialog.get_field("filter_area").$wrapper,
        doctype: this.doctype,
        on_change: () => {
          this.update_record_count_message();
        }
      });
    }
    make_select_all_buttons() {
      let for_insert = this.exporting_for === "Insert New Records";
      let section_title = for_insert ? __("Select Fields To Insert") : __("Select Fields To Update");
      let $select_all_buttons = $(`
			<div class="mb-3">
				<h6 class="form-section-heading uppercase">${section_title}</h6>
				<button class="btn btn-default btn-xs" data-action="select_all">
					${__("Select All")}
				</button>
				${for_insert ? `<button class="btn btn-default btn-xs" data-action="select_mandatory">
					${__("Select Mandatory")}
				</button>` : ""}
				<button class="btn btn-default btn-xs" data-action="unselect_all">
					${__("Unselect All")}
				</button>
			</div>
		`);
      frappe.utils.bind_actions_with_object($select_all_buttons, this);
      this.dialog.get_field("select_all_buttons").$wrapper.html($select_all_buttons);
    }
    select_all() {
      this.dialog.$wrapper.find(":checkbox").prop("checked", true).trigger("change");
    }
    select_mandatory() {
      let mandatory_table_fields = frappe.meta.get_table_fields(this.doctype).filter((df) => df.reqd).map((df) => df.fieldname);
      mandatory_table_fields.push(this.doctype);
      let multicheck_fields = this.dialog.fields.filter((df) => df.fieldtype === "MultiCheck").map((df) => df.fieldname).filter((doctype) => mandatory_table_fields.includes(doctype));
      let checkboxes = [].concat(
        ...multicheck_fields.map((fieldname) => {
          let field = this.dialog.get_field(fieldname);
          return field.options.filter((option) => option.danger).map((option) => option.$checkbox.find("input").get(0));
        })
      );
      this.unselect_all();
      $(checkboxes).prop("checked", true).trigger("change");
    }
    unselect_all() {
      let update_existing_records = this.dialog.get_value("exporting_for") == "Update Existing Records";
      this.dialog.$wrapper.find(`:checkbox${update_existing_records ? ":not([data-unit=name])" : ""}`).prop("checked", false).trigger("change");
    }
    update_record_count_message() {
      let export_records = this.dialog.get_value("export_records");
      let count_method = {
        all: () => frappe.db.count(this.doctype),
        by_filter: () => frappe.db.count(this.doctype, {
          filters: this.get_filters()
        }),
        blank_template: () => Promise.resolve(0),
        "5_records": () => Promise.resolve(5)
      };
      count_method[export_records]().then((value) => {
        let message = "";
        value = parseInt(value, 10);
        if (value === 0) {
          message = __("No records will be exported");
        } else if (value === 1) {
          message = __("1 record will be exported");
        } else {
          message = __("{0} records will be exported", [value]);
        }
        this.dialog.set_df_property("export_records", "description", message);
        this.update_primary_action(value);
      });
    }
    update_primary_action(no_of_records) {
      let $primary_action = this.dialog.get_primary_btn();
      if (no_of_records != null) {
        let label = "";
        if (no_of_records === 0) {
          label = __("Export");
        } else if (no_of_records === 1) {
          label = __("Export 1 record");
        } else {
          label = __("Export {0} records", [no_of_records]);
        }
        $primary_action.html(label);
      } else {
        let parent_fields = this.dialog.get_value(this.doctype);
        $primary_action.prop("disabled", parent_fields.length === 0);
      }
    }
    get_filters() {
      return this.filter_group.get_filters().map((filter) => {
        return filter.slice(0, 4);
      });
    }
    get_multicheck_options(doctype, child_fieldname = null) {
      if (!this.column_map) {
        this.column_map = get_columns_for_picker(this.doctype);
      }
      let autoname_field = null;
      let meta = frappe.get_meta(doctype);
      if (meta.autoname && meta.autoname.startsWith("field:")) {
        let fieldname = meta.autoname.slice("field:".length);
        autoname_field = frappe.meta.get_field(doctype, fieldname);
      }
      let fields = child_fieldname ? this.column_map[child_fieldname] : this.column_map[doctype];
      let is_field_mandatory = (df) => {
        if (df.reqd && this.exporting_for == "Insert New Records") {
          return true;
        }
        if (autoname_field && df.fieldname == autoname_field.fieldname) {
          return true;
        }
        if (df.fieldname === "name") {
          return true;
        }
        return false;
      };
      return fields.filter((df) => {
        if (autoname_field && df.fieldname === "name") {
          return false;
        }
        return true;
      }).map((df) => {
        return {
          label: __(df.label, null, df.parent),
          value: df.fieldname,
          danger: is_field_mandatory(df),
          checked: false,
          description: `${df.fieldname} ${df.reqd ? __("(Mandatory)") : ""}`
        };
      });
    }
  };
  function get_columns_for_picker(doctype) {
    let out = {};
    const exportable_fields = (df) => {
      let keep = true;
      if (frappe.model.no_value_type.includes(df.fieldtype)) {
        keep = false;
      }
      if (["lft", "rgt"].includes(df.fieldname)) {
        keep = false;
      }
      if (df.is_virtual) {
        keep = false;
      }
      return keep;
    };
    let doctype_fields = frappe.meta.get_docfields(doctype).filter(exportable_fields);
    out[doctype] = [
      {
        label: __("ID"),
        fieldname: "name",
        fieldtype: "Data",
        reqd: 1
      }
    ].concat(doctype_fields);
    const table_fields = frappe.meta.get_table_fields(doctype);
    table_fields.forEach((df) => {
      const cdt = df.options;
      const child_table_fields = frappe.meta.get_docfields(cdt).filter(exportable_fields);
      out[df.fieldname] = [
        {
          label: __("ID"),
          fieldname: "name",
          fieldtype: "Data",
          reqd: 1
        }
      ].concat(child_table_fields);
    });
    return out;
  }

  // frappe/public/js/frappe/data_import/import_preview.js
  frappe.provide("frappe.data_import");
  frappe.data_import.ImportPreview = class ImportPreview {
    constructor({ wrapper, doctype, preview_data, frm, import_log, events = {} }) {
      this.wrapper = wrapper;
      this.doctype = doctype;
      this.preview_data = preview_data;
      this.events = events;
      this.import_log = import_log;
      this.frm = frm;
      frappe.model.with_doctype(doctype, () => {
        this.refresh();
      });
    }
    refresh() {
      this.data = this.preview_data.data;
      this.make_wrapper();
      this.prepare_columns();
      this.prepare_data();
      this.render_datatable();
      this.setup_styles();
      this.add_actions();
    }
    make_wrapper() {
      this.wrapper.html(`
			<div>
				<div class="row">
					<div class="col-sm-12">
						<div class="table-actions margin-bottom">
						</div>
						<div class="table-preview"></div>
						<div class="table-message"></div>
					</div>
				</div>
			</div>
		`);
      frappe.utils.bind_actions_with_object(this.wrapper, this);
      this.$table_preview = this.wrapper.find(".table-preview");
    }
    prepare_columns() {
      this.columns = this.preview_data.columns.map((col, i) => {
        let df = col.df;
        let column_width = 120;
        if (col.header_title === "Sr. No") {
          return {
            id: "srno",
            name: "Sr. No",
            content: "Sr. No",
            editable: false,
            focusable: false,
            align: "left",
            width: 60
          };
        }
        if (col.skip_import) {
          let show_warnings_button = `<button class="btn btn-xs" data-action="show_column_warning" data-col="${i}">
					<i class="octicon octicon-stop"></i></button>`;
          if (!col.df) {
            column_width += 50;
          }
          let column_title2 = `<span class="indicator red">
					${col.header_title || `<i>${__("Untitled Column")}</i>`}
					${!col.df ? show_warnings_button : ""}
				</span>`;
          return {
            id: frappe.utils.get_random(6),
            name: col.header_title || (df ? df.label : "Untitled Column"),
            content: column_title2,
            skip_import: true,
            editable: false,
            focusable: false,
            align: "left",
            width: column_width,
            format: (value) => `<div class="text-muted">${value}</div>`
          };
        }
        let date_format = col.date_format ? col.date_format.replace("%Y", "yyyy").replace("%y", "yy").replace("%m", "mm").replace("%d", "dd").replace("%H", "HH").replace("%M", "mm").replace("%S", "ss").replace("%b", "Mon") : null;
        let column_title = `<span class="indicator green">
				${col.header_title || df.label}
				${date_format ? `(${date_format})` : ""}
			</span>`;
        return {
          id: df.fieldname,
          name: col.header_title,
          content: column_title,
          df,
          editable: false,
          align: "left",
          width: column_width
        };
      });
    }
    prepare_data() {
      this.data = this.data.map((row) => {
        return row.map((cell) => {
          if (cell == null) {
            return "";
          }
          return cell;
        });
      });
    }
    render_datatable() {
      if (this.datatable) {
        this.datatable.destroy();
      }
      this.datatable = new import_frappe_datatable.default(this.$table_preview.get(0), {
        data: this.data,
        columns: this.columns,
        layout: this.columns.length < 10 ? "fluid" : "fixed",
        cellHeight: 35,
        language: frappe.boot.lang,
        translations: frappe.utils.datatable.get_translations(),
        serialNoColumn: false,
        checkboxColumn: false,
        noDataMessage: __("No Data"),
        disableReorderColumn: true
      });
      let { max_rows_exceeded, max_rows_in_preview, total_number_of_rows } = this.preview_data;
      if (max_rows_exceeded) {
        let parts = [max_rows_in_preview, total_number_of_rows];
        this.wrapper.find(".table-message").html(`
				<div class="text-muted margin-top text-medium">
				${__("Showing only first {0} rows out of {1}", parts)}
				</div>
			`);
      }
      if (this.data.length === 0) {
        this.datatable.style.setStyle(".dt-scrollable", {
          height: "auto"
        });
      }
      this.datatable.style.setStyle(".dt-dropdown", {
        display: "none"
      });
    }
    setup_styles() {
      this.datatable.style.setStyle(`svg.import-success`, {
        width: "16px",
        fill: frappe.ui.color.get_color_shade("green", "dark")
      });
      let row_classes = this.datatable.getRows().filter((row) => this.is_row_imported(row)).map((row) => row.meta.rowIndex).map((i) => `.dt-row-${i} .dt-cell`).join(",");
      this.datatable.style.setStyle(row_classes, {
        pointerEvents: "none",
        backgroundColor: frappe.ui.color.get_color_shade("gray", "extra-light"),
        color: frappe.ui.color.get_color_shade("gray", "dark")
      });
    }
    add_actions() {
      let actions = [
        {
          label: __("Map Columns"),
          handler: "show_column_mapper",
          condition: this.frm.doc.status !== "Success"
        },
        {
          label: __("Export Errored Rows"),
          handler: "export_errored_rows",
          condition: this.import_log.filter((log) => !log.success).length > 0
        },
        {
          label: __("Show Warnings"),
          handler: "show_warnings",
          condition: this.preview_data.warnings.length > 0
        }
      ];
      let html = actions.filter((action) => action.condition).map((action) => {
        return `<button class="btn btn-sm btn-default" data-action="${action.handler}">
					${action.label}
				</button>
			`;
      });
      this.wrapper.find(".table-actions").html(html);
    }
    export_errored_rows() {
      this.frm.trigger("export_errored_rows");
    }
    show_warnings() {
      this.frm.scroll_to_field("import_warnings");
    }
    show_column_warning(_, $target) {
      let $warning = this.frm.get_field("import_warnings").$wrapper.find(`[data-col=${$target.data("col")}]`);
      frappe.utils.scroll_to($warning, true, 30);
    }
    show_column_mapper() {
      let column_picker_fields = get_columns_for_picker(this.doctype);
      let changed = [];
      let fields = this.preview_data.columns.map((col, i) => {
        let df = col.df;
        if (col.header_title === "Sr. No")
          return [];
        let fieldname;
        if (!df) {
          fieldname = null;
        } else if (col.map_to_field) {
          fieldname = col.map_to_field;
        } else if (col.is_child_table_field) {
          fieldname = `${col.child_table_df.fieldname}.${df.fieldname}`;
        } else {
          fieldname = df.fieldname;
        }
        return [
          {
            label: "",
            fieldtype: "Data",
            default: col.header_title,
            fieldname: `Column ${i}`,
            read_only: 1
          },
          {
            fieldtype: "Column Break"
          },
          {
            fieldtype: "Autocomplete",
            fieldname: i,
            label: "",
            max_items: Infinity,
            options: [
              {
                label: __("Don't Import"),
                value: "Don't Import"
              }
            ].concat(get_fields_as_options(this.doctype, column_picker_fields)),
            default: fieldname || "Don't Import",
            change() {
              changed.push(i);
            }
          },
          {
            fieldtype: "Section Break"
          }
        ];
      });
      fields = fields.reduce((acc, curr) => [...acc, ...curr]);
      let file_name = (this.frm.doc.import_file || "").split("/").pop();
      let parts = [file_name.bold(), this.doctype.bold()];
      fields = [
        {
          fieldtype: "HTML",
          fieldname: "heading",
          options: `
					<div class="margin-top text-muted">
					${__("Map columns from {0} to fields in {1}", parts)}
					</div>
				`
        },
        {
          fieldtype: "Section Break"
        }
      ].concat(fields);
      let dialog = new frappe.ui.Dialog({
        title: __("Map Columns"),
        fields,
        primary_action: (values) => {
          let changed_map = {};
          changed.map((i) => {
            let header_row_index = i - 1;
            changed_map[header_row_index] = values[i];
          });
          if (changed.length > 0) {
            this.events.remap_column(changed_map);
          }
          dialog.hide();
        }
      });
      dialog.$body.addClass("map-columns");
      dialog.show();
    }
    is_row_imported(row) {
      let serial_no = row[0].content;
      return this.import_log.find((log) => {
        return log.success && JSON.parse(log.row_indexes || "[]").includes(serial_no);
      });
    }
  };
  function get_fields_as_options(doctype, column_map) {
    let keys = [doctype];
    frappe.meta.get_table_fields(doctype).forEach((df) => {
      keys.push(df.fieldname);
    });
    return [].concat(
      ...keys.map((key) => {
        return column_map[key].map((df) => {
          let label = __(df.label, null, df.parent);
          let value = df.fieldname;
          if (doctype !== key) {
            let table_field = frappe.meta.get_docfield(doctype, key);
            label = `${__(df.label, null, df.parent)} (${__(table_field.label)})`;
            value = `${table_field.fieldname}.${df.fieldname}`;
          }
          return {
            label,
            value,
            description: value
          };
        });
      })
    );
  }
})();
/*! Sortable 1.15.0 - MIT | git://github.com/SortableJS/Sortable.git */
//# sourceMappingURL=data_import_tools.bundle.OT4HV4C6.js.map
