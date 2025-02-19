/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
import{e as o,w as s}from"./p-ead0d463.js";import{f as t,s as e}from"./p-12a8643e.js";import{c as r}from"./p-1b3ffb2f.js";import"./p-06fee233.js";const a=()=>{const a=window;a.addEventListener("statusTap",(()=>{o((()=>{const o=document.elementFromPoint(a.innerWidth/2,a.innerHeight/2);if(!o)return;const f=t(o);f&&new Promise((o=>r(f,o))).then((()=>{s((async()=>{f.style.setProperty("--overflow","hidden"),await e(f,300),f.style.removeProperty("--overflow")}))}))}))}))};export{a as startStatusTap}