(() => {
  var __defProp = Object.defineProperty;
  var __defProps = Object.defineProperties;
  var __getOwnPropDescs = Object.getOwnPropertyDescriptors;
  var __getOwnPropSymbols = Object.getOwnPropertySymbols;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __propIsEnum = Object.prototype.propertyIsEnumerable;
  var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
  var __spreadValues = (a, b) => {
    for (var prop in b || (b = {}))
      if (__hasOwnProp.call(b, prop))
        __defNormalProp(a, prop, b[prop]);
    if (__getOwnPropSymbols)
      for (var prop of __getOwnPropSymbols(b)) {
        if (__propIsEnum.call(b, prop))
          __defNormalProp(a, prop, b[prop]);
      }
    return a;
  };
  var __spreadProps = (a, b) => __defProps(a, __getOwnPropDescs(b));
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };

  // node_modules/@sentry/utils/esm/is.js
  var objectToString = Object.prototype.toString;
  function isError(wat) {
    switch (objectToString.call(wat)) {
      case "[object Error]":
      case "[object Exception]":
      case "[object DOMException]":
        return true;
      default:
        return isInstanceOf(wat, Error);
    }
  }
  function isBuiltin(wat, className) {
    return objectToString.call(wat) === `[object ${className}]`;
  }
  function isErrorEvent(wat) {
    return isBuiltin(wat, "ErrorEvent");
  }
  function isDOMError(wat) {
    return isBuiltin(wat, "DOMError");
  }
  function isDOMException(wat) {
    return isBuiltin(wat, "DOMException");
  }
  function isString(wat) {
    return isBuiltin(wat, "String");
  }
  function isParameterizedString(wat) {
    return typeof wat === "object" && wat !== null && "__sentry_template_string__" in wat && "__sentry_template_values__" in wat;
  }
  function isPrimitive(wat) {
    return wat === null || isParameterizedString(wat) || typeof wat !== "object" && typeof wat !== "function";
  }
  function isPlainObject(wat) {
    return isBuiltin(wat, "Object");
  }
  function isEvent(wat) {
    return typeof Event !== "undefined" && isInstanceOf(wat, Event);
  }
  function isElement(wat) {
    return typeof Element !== "undefined" && isInstanceOf(wat, Element);
  }
  function isRegExp(wat) {
    return isBuiltin(wat, "RegExp");
  }
  function isThenable(wat) {
    return Boolean(wat && wat.then && typeof wat.then === "function");
  }
  function isSyntheticEvent(wat) {
    return isPlainObject(wat) && "nativeEvent" in wat && "preventDefault" in wat && "stopPropagation" in wat;
  }
  function isNaN2(wat) {
    return typeof wat === "number" && wat !== wat;
  }
  function isInstanceOf(wat, base) {
    try {
      return wat instanceof base;
    } catch (_e) {
      return false;
    }
  }
  function isVueViewModel(wat) {
    return !!(typeof wat === "object" && wat !== null && (wat.__isVue || wat._isVue));
  }

  // node_modules/@sentry/utils/esm/string.js
  function truncate(str, max = 0) {
    if (typeof str !== "string" || max === 0) {
      return str;
    }
    return str.length <= max ? str : `${str.slice(0, max)}...`;
  }
  function safeJoin(input, delimiter) {
    if (!Array.isArray(input)) {
      return "";
    }
    const output = [];
    for (let i = 0; i < input.length; i++) {
      const value = input[i];
      try {
        if (isVueViewModel(value)) {
          output.push("[VueViewModel]");
        } else {
          output.push(String(value));
        }
      } catch (e) {
        output.push("[value cannot be serialized]");
      }
    }
    return output.join(delimiter);
  }
  function isMatchingPattern(value, pattern, requireExactStringMatch = false) {
    if (!isString(value)) {
      return false;
    }
    if (isRegExp(pattern)) {
      return pattern.test(value);
    }
    if (isString(pattern)) {
      return requireExactStringMatch ? value === pattern : value.includes(pattern);
    }
    return false;
  }
  function stringMatchesSomePattern(testString, patterns = [], requireExactStringMatch = false) {
    return patterns.some((pattern) => isMatchingPattern(testString, pattern, requireExactStringMatch));
  }

  // node_modules/@sentry/utils/esm/aggregate-errors.js
  function applyAggregateErrorsToEvent(exceptionFromErrorImplementation, parser, maxValueLimit = 250, key, limit, event, hint) {
    if (!event.exception || !event.exception.values || !hint || !isInstanceOf(hint.originalException, Error)) {
      return;
    }
    const originalException = event.exception.values.length > 0 ? event.exception.values[event.exception.values.length - 1] : void 0;
    if (originalException) {
      event.exception.values = truncateAggregateExceptions(
        aggregateExceptionsFromError(
          exceptionFromErrorImplementation,
          parser,
          limit,
          hint.originalException,
          key,
          event.exception.values,
          originalException,
          0
        ),
        maxValueLimit
      );
    }
  }
  function aggregateExceptionsFromError(exceptionFromErrorImplementation, parser, limit, error, key, prevExceptions, exception, exceptionId) {
    if (prevExceptions.length >= limit + 1) {
      return prevExceptions;
    }
    let newExceptions = [...prevExceptions];
    if (isInstanceOf(error[key], Error)) {
      applyExceptionGroupFieldsForParentException(exception, exceptionId);
      const newException = exceptionFromErrorImplementation(parser, error[key]);
      const newExceptionId = newExceptions.length;
      applyExceptionGroupFieldsForChildException(newException, key, newExceptionId, exceptionId);
      newExceptions = aggregateExceptionsFromError(
        exceptionFromErrorImplementation,
        parser,
        limit,
        error[key],
        key,
        [newException, ...newExceptions],
        newException,
        newExceptionId
      );
    }
    if (Array.isArray(error.errors)) {
      error.errors.forEach((childError, i) => {
        if (isInstanceOf(childError, Error)) {
          applyExceptionGroupFieldsForParentException(exception, exceptionId);
          const newException = exceptionFromErrorImplementation(parser, childError);
          const newExceptionId = newExceptions.length;
          applyExceptionGroupFieldsForChildException(newException, `errors[${i}]`, newExceptionId, exceptionId);
          newExceptions = aggregateExceptionsFromError(
            exceptionFromErrorImplementation,
            parser,
            limit,
            childError,
            key,
            [newException, ...newExceptions],
            newException,
            newExceptionId
          );
        }
      });
    }
    return newExceptions;
  }
  function applyExceptionGroupFieldsForParentException(exception, exceptionId) {
    exception.mechanism = exception.mechanism || { type: "generic", handled: true };
    exception.mechanism = __spreadProps(__spreadValues(__spreadValues({}, exception.mechanism), exception.type === "AggregateError" && { is_exception_group: true }), {
      exception_id: exceptionId
    });
  }
  function applyExceptionGroupFieldsForChildException(exception, source, exceptionId, parentId) {
    exception.mechanism = exception.mechanism || { type: "generic", handled: true };
    exception.mechanism = __spreadProps(__spreadValues({}, exception.mechanism), {
      type: "chained",
      source,
      exception_id: exceptionId,
      parent_id: parentId
    });
  }
  function truncateAggregateExceptions(exceptions, maxValueLength) {
    return exceptions.map((exception) => {
      if (exception.value) {
        exception.value = truncate(exception.value, maxValueLength);
      }
      return exception;
    });
  }

  // node_modules/@sentry/utils/esm/worldwide.js
  function isGlobalObj(obj) {
    return obj && obj.Math == Math ? obj : void 0;
  }
  var GLOBAL_OBJ = typeof globalThis == "object" && isGlobalObj(globalThis) || typeof window == "object" && isGlobalObj(window) || typeof self == "object" && isGlobalObj(self) || typeof global == "object" && isGlobalObj(global) || function() {
    return this;
  }() || {};
  function getGlobalObject() {
    return GLOBAL_OBJ;
  }
  function getGlobalSingleton(name, creator, obj) {
    const gbl = obj || GLOBAL_OBJ;
    const __SENTRY__ = gbl.__SENTRY__ = gbl.__SENTRY__ || {};
    const singleton = __SENTRY__[name] || (__SENTRY__[name] = creator());
    return singleton;
  }

  // node_modules/@sentry/utils/esm/browser.js
  var WINDOW = getGlobalObject();
  var DEFAULT_MAX_STRING_LENGTH = 80;
  function htmlTreeAsString(elem, options = {}) {
    if (!elem) {
      return "<unknown>";
    }
    try {
      let currentElem = elem;
      const MAX_TRAVERSE_HEIGHT = 5;
      const out = [];
      let height = 0;
      let len = 0;
      const separator = " > ";
      const sepLength = separator.length;
      let nextStr;
      const keyAttrs = Array.isArray(options) ? options : options.keyAttrs;
      const maxStringLength = !Array.isArray(options) && options.maxStringLength || DEFAULT_MAX_STRING_LENGTH;
      while (currentElem && height++ < MAX_TRAVERSE_HEIGHT) {
        nextStr = _htmlElementAsString(currentElem, keyAttrs);
        if (nextStr === "html" || height > 1 && len + out.length * sepLength + nextStr.length >= maxStringLength) {
          break;
        }
        out.push(nextStr);
        len += nextStr.length;
        currentElem = currentElem.parentNode;
      }
      return out.reverse().join(separator);
    } catch (_oO) {
      return "<unknown>";
    }
  }
  function _htmlElementAsString(el, keyAttrs) {
    const elem = el;
    const out = [];
    let className;
    let classes;
    let key;
    let attr;
    let i;
    if (!elem || !elem.tagName) {
      return "";
    }
    if (WINDOW.HTMLElement) {
      if (elem instanceof HTMLElement && elem.dataset && elem.dataset["sentryComponent"]) {
        return elem.dataset["sentryComponent"];
      }
    }
    out.push(elem.tagName.toLowerCase());
    const keyAttrPairs = keyAttrs && keyAttrs.length ? keyAttrs.filter((keyAttr) => elem.getAttribute(keyAttr)).map((keyAttr) => [keyAttr, elem.getAttribute(keyAttr)]) : null;
    if (keyAttrPairs && keyAttrPairs.length) {
      keyAttrPairs.forEach((keyAttrPair) => {
        out.push(`[${keyAttrPair[0]}="${keyAttrPair[1]}"]`);
      });
    } else {
      if (elem.id) {
        out.push(`#${elem.id}`);
      }
      className = elem.className;
      if (className && isString(className)) {
        classes = className.split(/\s+/);
        for (i = 0; i < classes.length; i++) {
          out.push(`.${classes[i]}`);
        }
      }
    }
    const allowedAttrs = ["aria-label", "type", "name", "title", "alt"];
    for (i = 0; i < allowedAttrs.length; i++) {
      key = allowedAttrs[i];
      attr = elem.getAttribute(key);
      if (attr) {
        out.push(`[${key}="${attr}"]`);
      }
    }
    return out.join("");
  }
  function getLocationHref() {
    try {
      return WINDOW.document.location.href;
    } catch (oO) {
      return "";
    }
  }
  function getComponentName(elem) {
    if (!WINDOW.HTMLElement) {
      return null;
    }
    let currentElem = elem;
    const MAX_TRAVERSE_HEIGHT = 5;
    for (let i = 0; i < MAX_TRAVERSE_HEIGHT; i++) {
      if (!currentElem) {
        return null;
      }
      if (currentElem instanceof HTMLElement && currentElem.dataset["sentryComponent"]) {
        return currentElem.dataset["sentryComponent"];
      }
      currentElem = currentElem.parentNode;
    }
    return null;
  }

  // node_modules/@sentry/utils/esm/debug-build.js
  var DEBUG_BUILD = typeof __SENTRY_DEBUG__ === "undefined" || __SENTRY_DEBUG__;

  // node_modules/@sentry/utils/esm/logger.js
  var PREFIX = "Sentry Logger ";
  var CONSOLE_LEVELS = [
    "debug",
    "info",
    "warn",
    "error",
    "log",
    "assert",
    "trace"
  ];
  var originalConsoleMethods = {};
  function consoleSandbox(callback) {
    if (!("console" in GLOBAL_OBJ)) {
      return callback();
    }
    const console2 = GLOBAL_OBJ.console;
    const wrappedFuncs = {};
    const wrappedLevels = Object.keys(originalConsoleMethods);
    wrappedLevels.forEach((level) => {
      const originalConsoleMethod = originalConsoleMethods[level];
      wrappedFuncs[level] = console2[level];
      console2[level] = originalConsoleMethod;
    });
    try {
      return callback();
    } finally {
      wrappedLevels.forEach((level) => {
        console2[level] = wrappedFuncs[level];
      });
    }
  }
  function makeLogger() {
    let enabled = false;
    const logger2 = {
      enable: () => {
        enabled = true;
      },
      disable: () => {
        enabled = false;
      },
      isEnabled: () => enabled
    };
    if (DEBUG_BUILD) {
      CONSOLE_LEVELS.forEach((name) => {
        logger2[name] = (...args) => {
          if (enabled) {
            consoleSandbox(() => {
              GLOBAL_OBJ.console[name](`${PREFIX}[${name}]:`, ...args);
            });
          }
        };
      });
    } else {
      CONSOLE_LEVELS.forEach((name) => {
        logger2[name] = () => void 0;
      });
    }
    return logger2;
  }
  var logger = makeLogger();

  // node_modules/@sentry/utils/esm/dsn.js
  var DSN_REGEX = /^(?:(\w+):)\/\/(?:(\w+)(?::(\w+)?)?@)([\w.-]+)(?::(\d+))?\/(.+)/;
  function isValidProtocol(protocol) {
    return protocol === "http" || protocol === "https";
  }
  function dsnToString(dsn, withPassword = false) {
    const { host, path, pass, port, projectId, protocol, publicKey } = dsn;
    return `${protocol}://${publicKey}${withPassword && pass ? `:${pass}` : ""}@${host}${port ? `:${port}` : ""}/${path ? `${path}/` : path}${projectId}`;
  }
  function dsnFromString(str) {
    const match = DSN_REGEX.exec(str);
    if (!match) {
      consoleSandbox(() => {
        console.error(`Invalid Sentry Dsn: ${str}`);
      });
      return void 0;
    }
    const [protocol, publicKey, pass = "", host, port = "", lastPath] = match.slice(1);
    let path = "";
    let projectId = lastPath;
    const split = projectId.split("/");
    if (split.length > 1) {
      path = split.slice(0, -1).join("/");
      projectId = split.pop();
    }
    if (projectId) {
      const projectMatch = projectId.match(/^\d+/);
      if (projectMatch) {
        projectId = projectMatch[0];
      }
    }
    return dsnFromComponents({ host, pass, path, projectId, port, protocol, publicKey });
  }
  function dsnFromComponents(components) {
    return {
      protocol: components.protocol,
      publicKey: components.publicKey || "",
      pass: components.pass || "",
      host: components.host,
      port: components.port || "",
      path: components.path || "",
      projectId: components.projectId
    };
  }
  function validateDsn(dsn) {
    if (!DEBUG_BUILD) {
      return true;
    }
    const { port, projectId, protocol } = dsn;
    const requiredComponents = ["protocol", "publicKey", "host", "projectId"];
    const hasMissingRequiredComponent = requiredComponents.find((component) => {
      if (!dsn[component]) {
        logger.error(`Invalid Sentry Dsn: ${component} missing`);
        return true;
      }
      return false;
    });
    if (hasMissingRequiredComponent) {
      return false;
    }
    if (!projectId.match(/^\d+$/)) {
      logger.error(`Invalid Sentry Dsn: Invalid projectId ${projectId}`);
      return false;
    }
    if (!isValidProtocol(protocol)) {
      logger.error(`Invalid Sentry Dsn: Invalid protocol ${protocol}`);
      return false;
    }
    if (port && isNaN(parseInt(port, 10))) {
      logger.error(`Invalid Sentry Dsn: Invalid port ${port}`);
      return false;
    }
    return true;
  }
  function makeDsn(from) {
    const components = typeof from === "string" ? dsnFromString(from) : dsnFromComponents(from);
    if (!components || !validateDsn(components)) {
      return void 0;
    }
    return components;
  }

  // node_modules/@sentry/utils/esm/error.js
  var SentryError = class extends Error {
    constructor(message, logLevel = "warn") {
      super(message);
      this.message = message;
      this.name = new.target.prototype.constructor.name;
      Object.setPrototypeOf(this, new.target.prototype);
      this.logLevel = logLevel;
    }
  };

  // node_modules/@sentry/utils/esm/object.js
  function fill(source, name, replacementFactory) {
    if (!(name in source)) {
      return;
    }
    const original = source[name];
    const wrapped = replacementFactory(original);
    if (typeof wrapped === "function") {
      markFunctionWrapped(wrapped, original);
    }
    source[name] = wrapped;
  }
  function addNonEnumerableProperty(obj, name, value) {
    try {
      Object.defineProperty(obj, name, {
        value,
        writable: true,
        configurable: true
      });
    } catch (o_O) {
      DEBUG_BUILD && logger.log(`Failed to add non-enumerable property "${name}" to object`, obj);
    }
  }
  function markFunctionWrapped(wrapped, original) {
    try {
      const proto = original.prototype || {};
      wrapped.prototype = original.prototype = proto;
      addNonEnumerableProperty(wrapped, "__sentry_original__", original);
    } catch (o_O) {
    }
  }
  function getOriginalFunction(func) {
    return func.__sentry_original__;
  }
  function urlEncode(object) {
    return Object.keys(object).map((key) => `${encodeURIComponent(key)}=${encodeURIComponent(object[key])}`).join("&");
  }
  function convertToPlainObject(value) {
    if (isError(value)) {
      return __spreadValues({
        message: value.message,
        name: value.name,
        stack: value.stack
      }, getOwnProperties(value));
    } else if (isEvent(value)) {
      const newObj = __spreadValues({
        type: value.type,
        target: serializeEventTarget(value.target),
        currentTarget: serializeEventTarget(value.currentTarget)
      }, getOwnProperties(value));
      if (typeof CustomEvent !== "undefined" && isInstanceOf(value, CustomEvent)) {
        newObj.detail = value.detail;
      }
      return newObj;
    } else {
      return value;
    }
  }
  function serializeEventTarget(target) {
    try {
      return isElement(target) ? htmlTreeAsString(target) : Object.prototype.toString.call(target);
    } catch (_oO) {
      return "<unknown>";
    }
  }
  function getOwnProperties(obj) {
    if (typeof obj === "object" && obj !== null) {
      const extractedProps = {};
      for (const property in obj) {
        if (Object.prototype.hasOwnProperty.call(obj, property)) {
          extractedProps[property] = obj[property];
        }
      }
      return extractedProps;
    } else {
      return {};
    }
  }
  function extractExceptionKeysForMessage(exception, maxLength = 40) {
    const keys = Object.keys(convertToPlainObject(exception));
    keys.sort();
    if (!keys.length) {
      return "[object has no keys]";
    }
    if (keys[0].length >= maxLength) {
      return truncate(keys[0], maxLength);
    }
    for (let includedKeys = keys.length; includedKeys > 0; includedKeys--) {
      const serialized = keys.slice(0, includedKeys).join(", ");
      if (serialized.length > maxLength) {
        continue;
      }
      if (includedKeys === keys.length) {
        return serialized;
      }
      return truncate(serialized, maxLength);
    }
    return "";
  }
  function dropUndefinedKeys(inputValue) {
    const memoizationMap = /* @__PURE__ */ new Map();
    return _dropUndefinedKeys(inputValue, memoizationMap);
  }
  function _dropUndefinedKeys(inputValue, memoizationMap) {
    if (isPojo(inputValue)) {
      const memoVal = memoizationMap.get(inputValue);
      if (memoVal !== void 0) {
        return memoVal;
      }
      const returnValue = {};
      memoizationMap.set(inputValue, returnValue);
      for (const key of Object.keys(inputValue)) {
        if (typeof inputValue[key] !== "undefined") {
          returnValue[key] = _dropUndefinedKeys(inputValue[key], memoizationMap);
        }
      }
      return returnValue;
    }
    if (Array.isArray(inputValue)) {
      const memoVal = memoizationMap.get(inputValue);
      if (memoVal !== void 0) {
        return memoVal;
      }
      const returnValue = [];
      memoizationMap.set(inputValue, returnValue);
      inputValue.forEach((item) => {
        returnValue.push(_dropUndefinedKeys(item, memoizationMap));
      });
      return returnValue;
    }
    return inputValue;
  }
  function isPojo(input) {
    if (!isPlainObject(input)) {
      return false;
    }
    try {
      const name = Object.getPrototypeOf(input).constructor.name;
      return !name || name === "Object";
    } catch (e) {
      return true;
    }
  }

  // node_modules/@sentry/utils/esm/stacktrace.js
  var STACKTRACE_FRAME_LIMIT = 50;
  var WEBPACK_ERROR_REGEXP = /\(error: (.*)\)/;
  var STRIP_FRAME_REGEXP = /captureMessage|captureException/;
  function createStackParser(...parsers) {
    const sortedParsers = parsers.sort((a, b) => a[0] - b[0]).map((p) => p[1]);
    return (stack, skipFirst = 0) => {
      const frames = [];
      const lines = stack.split("\n");
      for (let i = skipFirst; i < lines.length; i++) {
        const line = lines[i];
        if (line.length > 1024) {
          continue;
        }
        const cleanedLine = WEBPACK_ERROR_REGEXP.test(line) ? line.replace(WEBPACK_ERROR_REGEXP, "$1") : line;
        if (cleanedLine.match(/\S*Error: /)) {
          continue;
        }
        for (const parser of sortedParsers) {
          const frame = parser(cleanedLine);
          if (frame) {
            frames.push(frame);
            break;
          }
        }
        if (frames.length >= STACKTRACE_FRAME_LIMIT) {
          break;
        }
      }
      return stripSentryFramesAndReverse(frames);
    };
  }
  function stackParserFromStackParserOptions(stackParser) {
    if (Array.isArray(stackParser)) {
      return createStackParser(...stackParser);
    }
    return stackParser;
  }
  function stripSentryFramesAndReverse(stack) {
    if (!stack.length) {
      return [];
    }
    const localStack = Array.from(stack);
    if (/sentryWrapped/.test(localStack[localStack.length - 1].function || "")) {
      localStack.pop();
    }
    localStack.reverse();
    if (STRIP_FRAME_REGEXP.test(localStack[localStack.length - 1].function || "")) {
      localStack.pop();
      if (STRIP_FRAME_REGEXP.test(localStack[localStack.length - 1].function || "")) {
        localStack.pop();
      }
    }
    return localStack.slice(0, STACKTRACE_FRAME_LIMIT).map((frame) => __spreadProps(__spreadValues({}, frame), {
      filename: frame.filename || localStack[localStack.length - 1].filename,
      function: frame.function || "?"
    }));
  }
  var defaultFunctionName = "<anonymous>";
  function getFunctionName(fn) {
    try {
      if (!fn || typeof fn !== "function") {
        return defaultFunctionName;
      }
      return fn.name || defaultFunctionName;
    } catch (e) {
      return defaultFunctionName;
    }
  }

  // node_modules/@sentry/utils/esm/instrument/_handlers.js
  var handlers = {};
  var instrumented = {};
  function addHandler(type, handler) {
    handlers[type] = handlers[type] || [];
    handlers[type].push(handler);
  }
  function maybeInstrument(type, instrumentFn) {
    if (!instrumented[type]) {
      instrumentFn();
      instrumented[type] = true;
    }
  }
  function triggerHandlers(type, data) {
    const typeHandlers = type && handlers[type];
    if (!typeHandlers) {
      return;
    }
    for (const handler of typeHandlers) {
      try {
        handler(data);
      } catch (e) {
        DEBUG_BUILD && logger.error(
          `Error while triggering instrumentation handler.
Type: ${type}
Name: ${getFunctionName(handler)}
Error:`,
          e
        );
      }
    }
  }

  // node_modules/@sentry/utils/esm/instrument/console.js
  function addConsoleInstrumentationHandler(handler) {
    const type = "console";
    addHandler(type, handler);
    maybeInstrument(type, instrumentConsole);
  }
  function instrumentConsole() {
    if (!("console" in GLOBAL_OBJ)) {
      return;
    }
    CONSOLE_LEVELS.forEach(function(level) {
      if (!(level in GLOBAL_OBJ.console)) {
        return;
      }
      fill(GLOBAL_OBJ.console, level, function(originalConsoleMethod) {
        originalConsoleMethods[level] = originalConsoleMethod;
        return function(...args) {
          const handlerData = { args, level };
          triggerHandlers("console", handlerData);
          const log = originalConsoleMethods[level];
          log && log.apply(GLOBAL_OBJ.console, args);
        };
      });
    });
  }

  // node_modules/@sentry/utils/esm/misc.js
  function uuid4() {
    const gbl = GLOBAL_OBJ;
    const crypto = gbl.crypto || gbl.msCrypto;
    let getRandomByte = () => Math.random() * 16;
    try {
      if (crypto && crypto.randomUUID) {
        return crypto.randomUUID().replace(/-/g, "");
      }
      if (crypto && crypto.getRandomValues) {
        getRandomByte = () => {
          const typedArray = new Uint8Array(1);
          crypto.getRandomValues(typedArray);
          return typedArray[0];
        };
      }
    } catch (_) {
    }
    return ([1e7] + 1e3 + 4e3 + 8e3 + 1e11).replace(
      /[018]/g,
      (c) => (c ^ (getRandomByte() & 15) >> c / 4).toString(16)
    );
  }
  function getFirstException(event) {
    return event.exception && event.exception.values ? event.exception.values[0] : void 0;
  }
  function getEventDescription(event) {
    const { message, event_id: eventId } = event;
    if (message) {
      return message;
    }
    const firstException = getFirstException(event);
    if (firstException) {
      if (firstException.type && firstException.value) {
        return `${firstException.type}: ${firstException.value}`;
      }
      return firstException.type || firstException.value || eventId || "<unknown>";
    }
    return eventId || "<unknown>";
  }
  function addExceptionTypeValue(event, value, type) {
    const exception = event.exception = event.exception || {};
    const values = exception.values = exception.values || [];
    const firstException = values[0] = values[0] || {};
    if (!firstException.value) {
      firstException.value = value || "";
    }
    if (!firstException.type) {
      firstException.type = type || "Error";
    }
  }
  function addExceptionMechanism(event, newMechanism) {
    const firstException = getFirstException(event);
    if (!firstException) {
      return;
    }
    const defaultMechanism = { type: "generic", handled: true };
    const currentMechanism = firstException.mechanism;
    firstException.mechanism = __spreadValues(__spreadValues(__spreadValues({}, defaultMechanism), currentMechanism), newMechanism);
    if (newMechanism && "data" in newMechanism) {
      const mergedData = __spreadValues(__spreadValues({}, currentMechanism && currentMechanism.data), newMechanism.data);
      firstException.mechanism.data = mergedData;
    }
  }
  function checkOrSetAlreadyCaught(exception) {
    if (exception && exception.__sentry_captured__) {
      return true;
    }
    try {
      addNonEnumerableProperty(exception, "__sentry_captured__", true);
    } catch (err) {
    }
    return false;
  }
  function arrayify(maybeArray) {
    return Array.isArray(maybeArray) ? maybeArray : [maybeArray];
  }

  // node_modules/@sentry/utils/esm/instrument/dom.js
  var WINDOW2 = GLOBAL_OBJ;
  var DEBOUNCE_DURATION = 1e3;
  var debounceTimerID;
  var lastCapturedEventType;
  var lastCapturedEventTargetId;
  function addClickKeypressInstrumentationHandler(handler) {
    const type = "dom";
    addHandler(type, handler);
    maybeInstrument(type, instrumentDOM);
  }
  function instrumentDOM() {
    if (!WINDOW2.document) {
      return;
    }
    const triggerDOMHandler = triggerHandlers.bind(null, "dom");
    const globalDOMEventHandler = makeDOMEventHandler(triggerDOMHandler, true);
    WINDOW2.document.addEventListener("click", globalDOMEventHandler, false);
    WINDOW2.document.addEventListener("keypress", globalDOMEventHandler, false);
    ["EventTarget", "Node"].forEach((target) => {
      const proto = WINDOW2[target] && WINDOW2[target].prototype;
      if (!proto || !proto.hasOwnProperty || !proto.hasOwnProperty("addEventListener")) {
        return;
      }
      fill(proto, "addEventListener", function(originalAddEventListener) {
        return function(type, listener, options) {
          if (type === "click" || type == "keypress") {
            try {
              const el = this;
              const handlers2 = el.__sentry_instrumentation_handlers__ = el.__sentry_instrumentation_handlers__ || {};
              const handlerForType = handlers2[type] = handlers2[type] || { refCount: 0 };
              if (!handlerForType.handler) {
                const handler = makeDOMEventHandler(triggerDOMHandler);
                handlerForType.handler = handler;
                originalAddEventListener.call(this, type, handler, options);
              }
              handlerForType.refCount++;
            } catch (e) {
            }
          }
          return originalAddEventListener.call(this, type, listener, options);
        };
      });
      fill(
        proto,
        "removeEventListener",
        function(originalRemoveEventListener) {
          return function(type, listener, options) {
            if (type === "click" || type == "keypress") {
              try {
                const el = this;
                const handlers2 = el.__sentry_instrumentation_handlers__ || {};
                const handlerForType = handlers2[type];
                if (handlerForType) {
                  handlerForType.refCount--;
                  if (handlerForType.refCount <= 0) {
                    originalRemoveEventListener.call(this, type, handlerForType.handler, options);
                    handlerForType.handler = void 0;
                    delete handlers2[type];
                  }
                  if (Object.keys(handlers2).length === 0) {
                    delete el.__sentry_instrumentation_handlers__;
                  }
                }
              } catch (e) {
              }
            }
            return originalRemoveEventListener.call(this, type, listener, options);
          };
        }
      );
    });
  }
  function isSimilarToLastCapturedEvent(event) {
    if (event.type !== lastCapturedEventType) {
      return false;
    }
    try {
      if (!event.target || event.target._sentryId !== lastCapturedEventTargetId) {
        return false;
      }
    } catch (e) {
    }
    return true;
  }
  function shouldSkipDOMEvent(eventType, target) {
    if (eventType !== "keypress") {
      return false;
    }
    if (!target || !target.tagName) {
      return true;
    }
    if (target.tagName === "INPUT" || target.tagName === "TEXTAREA" || target.isContentEditable) {
      return false;
    }
    return true;
  }
  function makeDOMEventHandler(handler, globalListener = false) {
    return (event) => {
      if (!event || event["_sentryCaptured"]) {
        return;
      }
      const target = getEventTarget(event);
      if (shouldSkipDOMEvent(event.type, target)) {
        return;
      }
      addNonEnumerableProperty(event, "_sentryCaptured", true);
      if (target && !target._sentryId) {
        addNonEnumerableProperty(target, "_sentryId", uuid4());
      }
      const name = event.type === "keypress" ? "input" : event.type;
      if (!isSimilarToLastCapturedEvent(event)) {
        const handlerData = { event, name, global: globalListener };
        handler(handlerData);
        lastCapturedEventType = event.type;
        lastCapturedEventTargetId = target ? target._sentryId : void 0;
      }
      clearTimeout(debounceTimerID);
      debounceTimerID = WINDOW2.setTimeout(() => {
        lastCapturedEventTargetId = void 0;
        lastCapturedEventType = void 0;
      }, DEBOUNCE_DURATION);
    };
  }
  function getEventTarget(event) {
    try {
      return event.target;
    } catch (e) {
      return null;
    }
  }

  // node_modules/@sentry/utils/esm/supports.js
  var WINDOW3 = getGlobalObject();
  function supportsFetch() {
    if (!("fetch" in WINDOW3)) {
      return false;
    }
    try {
      new Headers();
      new Request("http://www.example.com");
      new Response();
      return true;
    } catch (e) {
      return false;
    }
  }
  function isNativeFetch(func) {
    return func && /^function fetch\(\)\s+\{\s+\[native code\]\s+\}$/.test(func.toString());
  }
  function supportsNativeFetch() {
    if (typeof EdgeRuntime === "string") {
      return true;
    }
    if (!supportsFetch()) {
      return false;
    }
    if (isNativeFetch(WINDOW3.fetch)) {
      return true;
    }
    let result = false;
    const doc = WINDOW3.document;
    if (doc && typeof doc.createElement === "function") {
      try {
        const sandbox = doc.createElement("iframe");
        sandbox.hidden = true;
        doc.head.appendChild(sandbox);
        if (sandbox.contentWindow && sandbox.contentWindow.fetch) {
          result = isNativeFetch(sandbox.contentWindow.fetch);
        }
        doc.head.removeChild(sandbox);
      } catch (err) {
        DEBUG_BUILD && logger.warn("Could not create sandbox iframe for pure fetch check, bailing to window.fetch: ", err);
      }
    }
    return result;
  }

  // node_modules/@sentry/utils/esm/instrument/fetch.js
  function addFetchInstrumentationHandler(handler) {
    const type = "fetch";
    addHandler(type, handler);
    maybeInstrument(type, instrumentFetch);
  }
  function instrumentFetch() {
    if (!supportsNativeFetch()) {
      return;
    }
    fill(GLOBAL_OBJ, "fetch", function(originalFetch) {
      return function(...args) {
        const { method, url } = parseFetchArgs(args);
        const handlerData = {
          args,
          fetchData: {
            method,
            url
          },
          startTimestamp: Date.now()
        };
        triggerHandlers("fetch", __spreadValues({}, handlerData));
        return originalFetch.apply(GLOBAL_OBJ, args).then(
          (response) => {
            const finishedHandlerData = __spreadProps(__spreadValues({}, handlerData), {
              endTimestamp: Date.now(),
              response
            });
            triggerHandlers("fetch", finishedHandlerData);
            return response;
          },
          (error) => {
            const erroredHandlerData = __spreadProps(__spreadValues({}, handlerData), {
              endTimestamp: Date.now(),
              error
            });
            triggerHandlers("fetch", erroredHandlerData);
            throw error;
          }
        );
      };
    });
  }
  function hasProp(obj, prop) {
    return !!obj && typeof obj === "object" && !!obj[prop];
  }
  function getUrlFromResource(resource) {
    if (typeof resource === "string") {
      return resource;
    }
    if (!resource) {
      return "";
    }
    if (hasProp(resource, "url")) {
      return resource.url;
    }
    if (resource.toString) {
      return resource.toString();
    }
    return "";
  }
  function parseFetchArgs(fetchArgs) {
    if (fetchArgs.length === 0) {
      return { method: "GET", url: "" };
    }
    if (fetchArgs.length === 2) {
      const [url, options] = fetchArgs;
      return {
        url: getUrlFromResource(url),
        method: hasProp(options, "method") ? String(options.method).toUpperCase() : "GET"
      };
    }
    const arg = fetchArgs[0];
    return {
      url: getUrlFromResource(arg),
      method: hasProp(arg, "method") ? String(arg.method).toUpperCase() : "GET"
    };
  }

  // node_modules/@sentry/utils/esm/instrument/globalError.js
  var _oldOnErrorHandler = null;
  function addGlobalErrorInstrumentationHandler(handler) {
    const type = "error";
    addHandler(type, handler);
    maybeInstrument(type, instrumentError);
  }
  function instrumentError() {
    _oldOnErrorHandler = GLOBAL_OBJ.onerror;
    GLOBAL_OBJ.onerror = function(msg, url, line, column, error) {
      const handlerData = {
        column,
        error,
        line,
        msg,
        url
      };
      triggerHandlers("error", handlerData);
      if (_oldOnErrorHandler && !_oldOnErrorHandler.__SENTRY_LOADER__) {
        return _oldOnErrorHandler.apply(this, arguments);
      }
      return false;
    };
    GLOBAL_OBJ.onerror.__SENTRY_INSTRUMENTED__ = true;
  }

  // node_modules/@sentry/utils/esm/instrument/globalUnhandledRejection.js
  var _oldOnUnhandledRejectionHandler = null;
  function addGlobalUnhandledRejectionInstrumentationHandler(handler) {
    const type = "unhandledrejection";
    addHandler(type, handler);
    maybeInstrument(type, instrumentUnhandledRejection);
  }
  function instrumentUnhandledRejection() {
    _oldOnUnhandledRejectionHandler = GLOBAL_OBJ.onunhandledrejection;
    GLOBAL_OBJ.onunhandledrejection = function(e) {
      const handlerData = e;
      triggerHandlers("unhandledrejection", handlerData);
      if (_oldOnUnhandledRejectionHandler && !_oldOnUnhandledRejectionHandler.__SENTRY_LOADER__) {
        return _oldOnUnhandledRejectionHandler.apply(this, arguments);
      }
      return true;
    };
    GLOBAL_OBJ.onunhandledrejection.__SENTRY_INSTRUMENTED__ = true;
  }

  // node_modules/@sentry/utils/esm/vendor/supportsHistory.js
  var WINDOW4 = getGlobalObject();
  function supportsHistory() {
    const chromeVar = WINDOW4.chrome;
    const isChromePackagedApp = chromeVar && chromeVar.app && chromeVar.app.runtime;
    const hasHistoryApi = "history" in WINDOW4 && !!WINDOW4.history.pushState && !!WINDOW4.history.replaceState;
    return !isChromePackagedApp && hasHistoryApi;
  }

  // node_modules/@sentry/utils/esm/instrument/history.js
  var WINDOW5 = GLOBAL_OBJ;
  var lastHref;
  function addHistoryInstrumentationHandler(handler) {
    const type = "history";
    addHandler(type, handler);
    maybeInstrument(type, instrumentHistory);
  }
  function instrumentHistory() {
    if (!supportsHistory()) {
      return;
    }
    const oldOnPopState = WINDOW5.onpopstate;
    WINDOW5.onpopstate = function(...args) {
      const to = WINDOW5.location.href;
      const from = lastHref;
      lastHref = to;
      const handlerData = { from, to };
      triggerHandlers("history", handlerData);
      if (oldOnPopState) {
        try {
          return oldOnPopState.apply(this, args);
        } catch (_oO) {
        }
      }
    };
    function historyReplacementFunction(originalHistoryFunction) {
      return function(...args) {
        const url = args.length > 2 ? args[2] : void 0;
        if (url) {
          const from = lastHref;
          const to = String(url);
          lastHref = to;
          const handlerData = { from, to };
          triggerHandlers("history", handlerData);
        }
        return originalHistoryFunction.apply(this, args);
      };
    }
    fill(WINDOW5.history, "pushState", historyReplacementFunction);
    fill(WINDOW5.history, "replaceState", historyReplacementFunction);
  }

  // node_modules/@sentry/utils/esm/instrument/xhr.js
  var WINDOW6 = GLOBAL_OBJ;
  var SENTRY_XHR_DATA_KEY = "__sentry_xhr_v3__";
  function addXhrInstrumentationHandler(handler) {
    const type = "xhr";
    addHandler(type, handler);
    maybeInstrument(type, instrumentXHR);
  }
  function instrumentXHR() {
    if (!WINDOW6.XMLHttpRequest) {
      return;
    }
    const xhrproto = XMLHttpRequest.prototype;
    fill(xhrproto, "open", function(originalOpen) {
      return function(...args) {
        const startTimestamp = Date.now();
        const method = isString(args[0]) ? args[0].toUpperCase() : void 0;
        const url = parseUrl(args[1]);
        if (!method || !url) {
          return originalOpen.apply(this, args);
        }
        this[SENTRY_XHR_DATA_KEY] = {
          method,
          url,
          request_headers: {}
        };
        if (method === "POST" && url.match(/sentry_key/)) {
          this.__sentry_own_request__ = true;
        }
        const onreadystatechangeHandler = () => {
          const xhrInfo = this[SENTRY_XHR_DATA_KEY];
          if (!xhrInfo) {
            return;
          }
          if (this.readyState === 4) {
            try {
              xhrInfo.status_code = this.status;
            } catch (e) {
            }
            const handlerData = {
              args: [method, url],
              endTimestamp: Date.now(),
              startTimestamp,
              xhr: this
            };
            triggerHandlers("xhr", handlerData);
          }
        };
        if ("onreadystatechange" in this && typeof this.onreadystatechange === "function") {
          fill(this, "onreadystatechange", function(original) {
            return function(...readyStateArgs) {
              onreadystatechangeHandler();
              return original.apply(this, readyStateArgs);
            };
          });
        } else {
          this.addEventListener("readystatechange", onreadystatechangeHandler);
        }
        fill(this, "setRequestHeader", function(original) {
          return function(...setRequestHeaderArgs) {
            const [header, value] = setRequestHeaderArgs;
            const xhrInfo = this[SENTRY_XHR_DATA_KEY];
            if (xhrInfo && isString(header) && isString(value)) {
              xhrInfo.request_headers[header.toLowerCase()] = value;
            }
            return original.apply(this, setRequestHeaderArgs);
          };
        });
        return originalOpen.apply(this, args);
      };
    });
    fill(xhrproto, "send", function(originalSend) {
      return function(...args) {
        const sentryXhrData = this[SENTRY_XHR_DATA_KEY];
        if (!sentryXhrData) {
          return originalSend.apply(this, args);
        }
        if (args[0] !== void 0) {
          sentryXhrData.body = args[0];
        }
        const handlerData = {
          args: [sentryXhrData.method, sentryXhrData.url],
          startTimestamp: Date.now(),
          xhr: this
        };
        triggerHandlers("xhr", handlerData);
        return originalSend.apply(this, args);
      };
    });
  }
  function parseUrl(url) {
    if (isString(url)) {
      return url;
    }
    try {
      return url.toString();
    } catch (e2) {
    }
    return void 0;
  }

  // node_modules/@sentry/utils/esm/env.js
  function getSDKSource() {
    return "npm";
  }

  // node_modules/@sentry/utils/esm/memo.js
  function memoBuilder() {
    const hasWeakSet = typeof WeakSet === "function";
    const inner = hasWeakSet ? /* @__PURE__ */ new WeakSet() : [];
    function memoize(obj) {
      if (hasWeakSet) {
        if (inner.has(obj)) {
          return true;
        }
        inner.add(obj);
        return false;
      }
      for (let i = 0; i < inner.length; i++) {
        const value = inner[i];
        if (value === obj) {
          return true;
        }
      }
      inner.push(obj);
      return false;
    }
    function unmemoize(obj) {
      if (hasWeakSet) {
        inner.delete(obj);
      } else {
        for (let i = 0; i < inner.length; i++) {
          if (inner[i] === obj) {
            inner.splice(i, 1);
            break;
          }
        }
      }
    }
    return [memoize, unmemoize];
  }

  // node_modules/@sentry/utils/esm/normalize.js
  function normalize(input, depth = 100, maxProperties = Infinity) {
    try {
      return visit("", input, depth, maxProperties);
    } catch (err) {
      return { ERROR: `**non-serializable** (${err})` };
    }
  }
  function normalizeToSize(object, depth = 3, maxSize = 100 * 1024) {
    const normalized = normalize(object, depth);
    if (jsonSize(normalized) > maxSize) {
      return normalizeToSize(object, depth - 1, maxSize);
    }
    return normalized;
  }
  function visit(key, value, depth = Infinity, maxProperties = Infinity, memo = memoBuilder()) {
    const [memoize, unmemoize] = memo;
    if (value == null || ["number", "boolean", "string"].includes(typeof value) && !isNaN2(value)) {
      return value;
    }
    const stringified = stringifyValue(key, value);
    if (!stringified.startsWith("[object ")) {
      return stringified;
    }
    if (value["__sentry_skip_normalization__"]) {
      return value;
    }
    const remainingDepth = typeof value["__sentry_override_normalization_depth__"] === "number" ? value["__sentry_override_normalization_depth__"] : depth;
    if (remainingDepth === 0) {
      return stringified.replace("object ", "");
    }
    if (memoize(value)) {
      return "[Circular ~]";
    }
    const valueWithToJSON = value;
    if (valueWithToJSON && typeof valueWithToJSON.toJSON === "function") {
      try {
        const jsonValue = valueWithToJSON.toJSON();
        return visit("", jsonValue, remainingDepth - 1, maxProperties, memo);
      } catch (err) {
      }
    }
    const normalized = Array.isArray(value) ? [] : {};
    let numAdded = 0;
    const visitable = convertToPlainObject(value);
    for (const visitKey in visitable) {
      if (!Object.prototype.hasOwnProperty.call(visitable, visitKey)) {
        continue;
      }
      if (numAdded >= maxProperties) {
        normalized[visitKey] = "[MaxProperties ~]";
        break;
      }
      const visitValue = visitable[visitKey];
      normalized[visitKey] = visit(visitKey, visitValue, remainingDepth - 1, maxProperties, memo);
      numAdded++;
    }
    unmemoize(value);
    return normalized;
  }
  function stringifyValue(key, value) {
    try {
      if (key === "domain" && value && typeof value === "object" && value._events) {
        return "[Domain]";
      }
      if (key === "domainEmitter") {
        return "[DomainEmitter]";
      }
      if (typeof global !== "undefined" && value === global) {
        return "[Global]";
      }
      if (typeof window !== "undefined" && value === window) {
        return "[Window]";
      }
      if (typeof document !== "undefined" && value === document) {
        return "[Document]";
      }
      if (isVueViewModel(value)) {
        return "[VueViewModel]";
      }
      if (isSyntheticEvent(value)) {
        return "[SyntheticEvent]";
      }
      if (typeof value === "number" && value !== value) {
        return "[NaN]";
      }
      if (typeof value === "function") {
        return `[Function: ${getFunctionName(value)}]`;
      }
      if (typeof value === "symbol") {
        return `[${String(value)}]`;
      }
      if (typeof value === "bigint") {
        return `[BigInt: ${String(value)}]`;
      }
      const objName = getConstructorName(value);
      if (/^HTML(\w*)Element$/.test(objName)) {
        return `[HTMLElement: ${objName}]`;
      }
      return `[object ${objName}]`;
    } catch (err) {
      return `**non-serializable** (${err})`;
    }
  }
  function getConstructorName(value) {
    const prototype = Object.getPrototypeOf(value);
    return prototype ? prototype.constructor.name : "null prototype";
  }
  function utf8Length(value) {
    return ~-encodeURI(value).split(/%..|./).length;
  }
  function jsonSize(value) {
    return utf8Length(JSON.stringify(value));
  }

  // node_modules/@sentry/utils/esm/syncpromise.js
  var States;
  (function(States2) {
    const PENDING = 0;
    States2[States2["PENDING"] = PENDING] = "PENDING";
    const RESOLVED = 1;
    States2[States2["RESOLVED"] = RESOLVED] = "RESOLVED";
    const REJECTED = 2;
    States2[States2["REJECTED"] = REJECTED] = "REJECTED";
  })(States || (States = {}));
  function resolvedSyncPromise(value) {
    return new SyncPromise((resolve) => {
      resolve(value);
    });
  }
  function rejectedSyncPromise(reason) {
    return new SyncPromise((_, reject) => {
      reject(reason);
    });
  }
  var SyncPromise = class {
    constructor(executor) {
      SyncPromise.prototype.__init.call(this);
      SyncPromise.prototype.__init2.call(this);
      SyncPromise.prototype.__init3.call(this);
      SyncPromise.prototype.__init4.call(this);
      this._state = States.PENDING;
      this._handlers = [];
      try {
        executor(this._resolve, this._reject);
      } catch (e) {
        this._reject(e);
      }
    }
    then(onfulfilled, onrejected) {
      return new SyncPromise((resolve, reject) => {
        this._handlers.push([
          false,
          (result) => {
            if (!onfulfilled) {
              resolve(result);
            } else {
              try {
                resolve(onfulfilled(result));
              } catch (e) {
                reject(e);
              }
            }
          },
          (reason) => {
            if (!onrejected) {
              reject(reason);
            } else {
              try {
                resolve(onrejected(reason));
              } catch (e) {
                reject(e);
              }
            }
          }
        ]);
        this._executeHandlers();
      });
    }
    catch(onrejected) {
      return this.then((val) => val, onrejected);
    }
    finally(onfinally) {
      return new SyncPromise((resolve, reject) => {
        let val;
        let isRejected;
        return this.then(
          (value) => {
            isRejected = false;
            val = value;
            if (onfinally) {
              onfinally();
            }
          },
          (reason) => {
            isRejected = true;
            val = reason;
            if (onfinally) {
              onfinally();
            }
          }
        ).then(() => {
          if (isRejected) {
            reject(val);
            return;
          }
          resolve(val);
        });
      });
    }
    __init() {
      this._resolve = (value) => {
        this._setResult(States.RESOLVED, value);
      };
    }
    __init2() {
      this._reject = (reason) => {
        this._setResult(States.REJECTED, reason);
      };
    }
    __init3() {
      this._setResult = (state, value) => {
        if (this._state !== States.PENDING) {
          return;
        }
        if (isThenable(value)) {
          void value.then(this._resolve, this._reject);
          return;
        }
        this._state = state;
        this._value = value;
        this._executeHandlers();
      };
    }
    __init4() {
      this._executeHandlers = () => {
        if (this._state === States.PENDING) {
          return;
        }
        const cachedHandlers = this._handlers.slice();
        this._handlers = [];
        cachedHandlers.forEach((handler) => {
          if (handler[0]) {
            return;
          }
          if (this._state === States.RESOLVED) {
            handler[1](this._value);
          }
          if (this._state === States.REJECTED) {
            handler[2](this._value);
          }
          handler[0] = true;
        });
      };
    }
  };

  // node_modules/@sentry/utils/esm/promisebuffer.js
  function makePromiseBuffer(limit) {
    const buffer = [];
    function isReady() {
      return limit === void 0 || buffer.length < limit;
    }
    function remove(task) {
      return buffer.splice(buffer.indexOf(task), 1)[0];
    }
    function add(taskProducer) {
      if (!isReady()) {
        return rejectedSyncPromise(new SentryError("Not adding Promise because buffer limit was reached."));
      }
      const task = taskProducer();
      if (buffer.indexOf(task) === -1) {
        buffer.push(task);
      }
      void task.then(() => remove(task)).then(
        null,
        () => remove(task).then(null, () => {
        })
      );
      return task;
    }
    function drain(timeout) {
      return new SyncPromise((resolve, reject) => {
        let counter = buffer.length;
        if (!counter) {
          return resolve(true);
        }
        const capturedSetTimeout = setTimeout(() => {
          if (timeout && timeout > 0) {
            resolve(false);
          }
        }, timeout);
        buffer.forEach((item) => {
          void resolvedSyncPromise(item).then(() => {
            if (!--counter) {
              clearTimeout(capturedSetTimeout);
              resolve(true);
            }
          }, reject);
        });
      });
    }
    return {
      $: buffer,
      add,
      drain
    };
  }

  // node_modules/@sentry/utils/esm/url.js
  function parseUrl2(url) {
    if (!url) {
      return {};
    }
    const match = url.match(/^(([^:/?#]+):)?(\/\/([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?$/);
    if (!match) {
      return {};
    }
    const query = match[6] || "";
    const fragment = match[8] || "";
    return {
      host: match[4],
      path: match[5],
      protocol: match[2],
      search: query,
      hash: fragment,
      relative: match[5] + query + fragment
    };
  }

  // node_modules/@sentry/utils/esm/severity.js
  var validSeverityLevels = ["fatal", "error", "warning", "log", "info", "debug"];
  function severityLevelFromString(level) {
    return level === "warn" ? "warning" : validSeverityLevels.includes(level) ? level : "log";
  }

  // node_modules/@sentry/utils/esm/time.js
  var ONE_SECOND_IN_MS = 1e3;
  function dateTimestampInSeconds() {
    return Date.now() / ONE_SECOND_IN_MS;
  }
  function createUnixTimestampInSecondsFunc() {
    const { performance } = GLOBAL_OBJ;
    if (!performance || !performance.now) {
      return dateTimestampInSeconds;
    }
    const approxStartingTimeOrigin = Date.now() - performance.now();
    const timeOrigin = performance.timeOrigin == void 0 ? approxStartingTimeOrigin : performance.timeOrigin;
    return () => {
      return (timeOrigin + performance.now()) / ONE_SECOND_IN_MS;
    };
  }
  var timestampInSeconds = createUnixTimestampInSecondsFunc();
  var _browserPerformanceTimeOriginMode;
  var browserPerformanceTimeOrigin = (() => {
    const { performance } = GLOBAL_OBJ;
    if (!performance || !performance.now) {
      _browserPerformanceTimeOriginMode = "none";
      return void 0;
    }
    const threshold = 3600 * 1e3;
    const performanceNow = performance.now();
    const dateNow = Date.now();
    const timeOriginDelta = performance.timeOrigin ? Math.abs(performance.timeOrigin + performanceNow - dateNow) : threshold;
    const timeOriginIsReliable = timeOriginDelta < threshold;
    const navigationStart = performance.timing && performance.timing.navigationStart;
    const hasNavigationStart = typeof navigationStart === "number";
    const navigationStartDelta = hasNavigationStart ? Math.abs(navigationStart + performanceNow - dateNow) : threshold;
    const navigationStartIsReliable = navigationStartDelta < threshold;
    if (timeOriginIsReliable || navigationStartIsReliable) {
      if (timeOriginDelta <= navigationStartDelta) {
        _browserPerformanceTimeOriginMode = "timeOrigin";
        return performance.timeOrigin;
      } else {
        _browserPerformanceTimeOriginMode = "navigationStart";
        return navigationStart;
      }
    }
    _browserPerformanceTimeOriginMode = "dateNow";
    return dateNow;
  })();

  // node_modules/@sentry/utils/esm/envelope.js
  function createEnvelope(headers, items = []) {
    return [headers, items];
  }
  function addItemToEnvelope(envelope, newItem) {
    const [headers, items] = envelope;
    return [headers, [...items, newItem]];
  }
  function forEachEnvelopeItem(envelope, callback) {
    const envelopeItems = envelope[1];
    for (const envelopeItem of envelopeItems) {
      const envelopeItemType = envelopeItem[0].type;
      const result = callback(envelopeItem, envelopeItemType);
      if (result) {
        return true;
      }
    }
    return false;
  }
  function encodeUTF8(input, textEncoder) {
    const utf8 = textEncoder || new TextEncoder();
    return utf8.encode(input);
  }
  function serializeEnvelope(envelope, textEncoder) {
    const [envHeaders, items] = envelope;
    let parts = JSON.stringify(envHeaders);
    function append(next) {
      if (typeof parts === "string") {
        parts = typeof next === "string" ? parts + next : [encodeUTF8(parts, textEncoder), next];
      } else {
        parts.push(typeof next === "string" ? encodeUTF8(next, textEncoder) : next);
      }
    }
    for (const item of items) {
      const [itemHeaders, payload] = item;
      append(`
${JSON.stringify(itemHeaders)}
`);
      if (typeof payload === "string" || payload instanceof Uint8Array) {
        append(payload);
      } else {
        let stringifiedPayload;
        try {
          stringifiedPayload = JSON.stringify(payload);
        } catch (e) {
          stringifiedPayload = JSON.stringify(normalize(payload));
        }
        append(stringifiedPayload);
      }
    }
    return typeof parts === "string" ? parts : concatBuffers(parts);
  }
  function concatBuffers(buffers) {
    const totalLength = buffers.reduce((acc, buf) => acc + buf.length, 0);
    const merged = new Uint8Array(totalLength);
    let offset = 0;
    for (const buffer of buffers) {
      merged.set(buffer, offset);
      offset += buffer.length;
    }
    return merged;
  }
  function createAttachmentEnvelopeItem(attachment, textEncoder) {
    const buffer = typeof attachment.data === "string" ? encodeUTF8(attachment.data, textEncoder) : attachment.data;
    return [
      dropUndefinedKeys({
        type: "attachment",
        length: buffer.length,
        filename: attachment.filename,
        content_type: attachment.contentType,
        attachment_type: attachment.attachmentType
      }),
      buffer
    ];
  }
  var ITEM_TYPE_TO_DATA_CATEGORY_MAP = {
    session: "session",
    sessions: "session",
    attachment: "attachment",
    transaction: "transaction",
    event: "error",
    client_report: "internal",
    user_report: "default",
    profile: "profile",
    replay_event: "replay",
    replay_recording: "replay",
    check_in: "monitor",
    feedback: "feedback",
    span: "span",
    statsd: "metric_bucket"
  };
  function envelopeItemTypeToDataCategory(type) {
    return ITEM_TYPE_TO_DATA_CATEGORY_MAP[type];
  }
  function getSdkMetadataForEnvelopeHeader(metadataOrEvent) {
    if (!metadataOrEvent || !metadataOrEvent.sdk) {
      return;
    }
    const { name, version } = metadataOrEvent.sdk;
    return { name, version };
  }
  function createEventEnvelopeHeaders(event, sdkInfo, tunnel, dsn) {
    const dynamicSamplingContext = event.sdkProcessingMetadata && event.sdkProcessingMetadata.dynamicSamplingContext;
    return __spreadValues(__spreadValues(__spreadValues({
      event_id: event.event_id,
      sent_at: new Date().toISOString()
    }, sdkInfo && { sdk: sdkInfo }), !!tunnel && dsn && { dsn: dsnToString(dsn) }), dynamicSamplingContext && {
      trace: dropUndefinedKeys(__spreadValues({}, dynamicSamplingContext))
    });
  }

  // node_modules/@sentry/utils/esm/clientreport.js
  function createClientReportEnvelope(discarded_events, dsn, timestamp) {
    const clientReportItem = [
      { type: "client_report" },
      {
        timestamp: timestamp || dateTimestampInSeconds(),
        discarded_events
      }
    ];
    return createEnvelope(dsn ? { dsn } : {}, [clientReportItem]);
  }

  // node_modules/@sentry/utils/esm/ratelimit.js
  var DEFAULT_RETRY_AFTER = 60 * 1e3;
  function parseRetryAfterHeader(header, now = Date.now()) {
    const headerDelay = parseInt(`${header}`, 10);
    if (!isNaN(headerDelay)) {
      return headerDelay * 1e3;
    }
    const headerDate = Date.parse(`${header}`);
    if (!isNaN(headerDate)) {
      return headerDate - now;
    }
    return DEFAULT_RETRY_AFTER;
  }
  function disabledUntil(limits, dataCategory) {
    return limits[dataCategory] || limits.all || 0;
  }
  function isRateLimited(limits, dataCategory, now = Date.now()) {
    return disabledUntil(limits, dataCategory) > now;
  }
  function updateRateLimits(limits, { statusCode, headers }, now = Date.now()) {
    const updatedRateLimits = __spreadValues({}, limits);
    const rateLimitHeader = headers && headers["x-sentry-rate-limits"];
    const retryAfterHeader = headers && headers["retry-after"];
    if (rateLimitHeader) {
      for (const limit of rateLimitHeader.trim().split(",")) {
        const [retryAfter, categories, , , namespaces] = limit.split(":", 5);
        const headerDelay = parseInt(retryAfter, 10);
        const delay = (!isNaN(headerDelay) ? headerDelay : 60) * 1e3;
        if (!categories) {
          updatedRateLimits.all = now + delay;
        } else {
          for (const category of categories.split(";")) {
            if (category === "metric_bucket") {
              if (!namespaces || namespaces.split(";").includes("custom")) {
                updatedRateLimits[category] = now + delay;
              }
            } else {
              updatedRateLimits[category] = now + delay;
            }
          }
        }
      }
    } else if (retryAfterHeader) {
      updatedRateLimits.all = now + parseRetryAfterHeader(retryAfterHeader, now);
    } else if (statusCode === 429) {
      updatedRateLimits.all = now + 60 * 1e3;
    }
    return updatedRateLimits;
  }

  // node_modules/@sentry/utils/esm/eventbuilder.js
  function parseStackFrames(stackParser, error) {
    return stackParser(error.stack || "", 1);
  }
  function exceptionFromError(stackParser, error) {
    const exception = {
      type: error.name || error.constructor.name,
      value: error.message
    };
    const frames = parseStackFrames(stackParser, error);
    if (frames.length) {
      exception.stacktrace = { frames };
    }
    return exception;
  }

  // node_modules/@sentry/core/esm/debug-build.js
  var DEBUG_BUILD2 = typeof __SENTRY_DEBUG__ === "undefined" || __SENTRY_DEBUG__;

  // node_modules/@sentry/core/esm/constants.js
  var DEFAULT_ENVIRONMENT = "production";

  // node_modules/@sentry/core/esm/eventProcessors.js
  function getGlobalEventProcessors() {
    return getGlobalSingleton("globalEventProcessors", () => []);
  }
  function addGlobalEventProcessor(callback) {
    getGlobalEventProcessors().push(callback);
  }
  function notifyEventProcessors(processors, event, hint, index = 0) {
    return new SyncPromise((resolve, reject) => {
      const processor = processors[index];
      if (event === null || typeof processor !== "function") {
        resolve(event);
      } else {
        const result = processor(__spreadValues({}, event), hint);
        DEBUG_BUILD2 && processor.id && result === null && logger.log(`Event processor "${processor.id}" dropped event`);
        if (isThenable(result)) {
          void result.then((final) => notifyEventProcessors(processors, final, hint, index + 1).then(resolve)).then(null, reject);
        } else {
          void notifyEventProcessors(processors, result, hint, index + 1).then(resolve).then(null, reject);
        }
      }
    });
  }

  // node_modules/@sentry/core/esm/session.js
  function makeSession(context) {
    const startingTime = timestampInSeconds();
    const session = {
      sid: uuid4(),
      init: true,
      timestamp: startingTime,
      started: startingTime,
      duration: 0,
      status: "ok",
      errors: 0,
      ignoreDuration: false,
      toJSON: () => sessionToJSON(session)
    };
    if (context) {
      updateSession(session, context);
    }
    return session;
  }
  function updateSession(session, context = {}) {
    if (context.user) {
      if (!session.ipAddress && context.user.ip_address) {
        session.ipAddress = context.user.ip_address;
      }
      if (!session.did && !context.did) {
        session.did = context.user.id || context.user.email || context.user.username;
      }
    }
    session.timestamp = context.timestamp || timestampInSeconds();
    if (context.abnormal_mechanism) {
      session.abnormal_mechanism = context.abnormal_mechanism;
    }
    if (context.ignoreDuration) {
      session.ignoreDuration = context.ignoreDuration;
    }
    if (context.sid) {
      session.sid = context.sid.length === 32 ? context.sid : uuid4();
    }
    if (context.init !== void 0) {
      session.init = context.init;
    }
    if (!session.did && context.did) {
      session.did = `${context.did}`;
    }
    if (typeof context.started === "number") {
      session.started = context.started;
    }
    if (session.ignoreDuration) {
      session.duration = void 0;
    } else if (typeof context.duration === "number") {
      session.duration = context.duration;
    } else {
      const duration = session.timestamp - session.started;
      session.duration = duration >= 0 ? duration : 0;
    }
    if (context.release) {
      session.release = context.release;
    }
    if (context.environment) {
      session.environment = context.environment;
    }
    if (!session.ipAddress && context.ipAddress) {
      session.ipAddress = context.ipAddress;
    }
    if (!session.userAgent && context.userAgent) {
      session.userAgent = context.userAgent;
    }
    if (typeof context.errors === "number") {
      session.errors = context.errors;
    }
    if (context.status) {
      session.status = context.status;
    }
  }
  function closeSession(session, status) {
    let context = {};
    if (status) {
      context = { status };
    } else if (session.status === "ok") {
      context = { status: "exited" };
    }
    updateSession(session, context);
  }
  function sessionToJSON(session) {
    return dropUndefinedKeys({
      sid: `${session.sid}`,
      init: session.init,
      started: new Date(session.started * 1e3).toISOString(),
      timestamp: new Date(session.timestamp * 1e3).toISOString(),
      status: session.status,
      errors: session.errors,
      did: typeof session.did === "number" || typeof session.did === "string" ? `${session.did}` : void 0,
      duration: session.duration,
      abnormal_mechanism: session.abnormal_mechanism,
      attrs: {
        release: session.release,
        environment: session.environment,
        ip_address: session.ipAddress,
        user_agent: session.userAgent
      }
    });
  }

  // node_modules/@sentry/core/esm/utils/spanUtils.js
  var TRACE_FLAG_SAMPLED = 1;
  function spanToTraceContext(span) {
    const { spanId: span_id, traceId: trace_id } = span.spanContext();
    const { data, op, parent_span_id, status, tags, origin } = spanToJSON(span);
    return dropUndefinedKeys({
      data,
      op,
      parent_span_id,
      span_id,
      status,
      tags,
      trace_id,
      origin
    });
  }
  function spanToJSON(span) {
    if (spanIsSpanClass(span)) {
      return span.getSpanJSON();
    }
    if (typeof span.toJSON === "function") {
      return span.toJSON();
    }
    return {};
  }
  function spanIsSpanClass(span) {
    return typeof span.getSpanJSON === "function";
  }
  function spanIsSampled(span) {
    const { traceFlags } = span.spanContext();
    return Boolean(traceFlags & TRACE_FLAG_SAMPLED);
  }

  // node_modules/@sentry/core/esm/utils/prepareEvent.js
  function prepareEvent(options, event, hint, scope, client, isolationScope) {
    const { normalizeDepth = 3, normalizeMaxBreadth = 1e3 } = options;
    const prepared = __spreadProps(__spreadValues({}, event), {
      event_id: event.event_id || hint.event_id || uuid4(),
      timestamp: event.timestamp || dateTimestampInSeconds()
    });
    const integrations = hint.integrations || options.integrations.map((i) => i.name);
    applyClientOptions(prepared, options);
    applyIntegrationsMetadata(prepared, integrations);
    if (event.type === void 0) {
      applyDebugIds(prepared, options.stackParser);
    }
    const finalScope = getFinalScope(scope, hint.captureContext);
    if (hint.mechanism) {
      addExceptionMechanism(prepared, hint.mechanism);
    }
    const clientEventProcessors = client && client.getEventProcessors ? client.getEventProcessors() : [];
    const data = getGlobalScope().getScopeData();
    if (isolationScope) {
      const isolationData = isolationScope.getScopeData();
      mergeScopeData(data, isolationData);
    }
    if (finalScope) {
      const finalScopeData = finalScope.getScopeData();
      mergeScopeData(data, finalScopeData);
    }
    const attachments = [...hint.attachments || [], ...data.attachments];
    if (attachments.length) {
      hint.attachments = attachments;
    }
    applyScopeDataToEvent(prepared, data);
    const eventProcessors = [
      ...clientEventProcessors,
      ...getGlobalEventProcessors(),
      ...data.eventProcessors
    ];
    const result = notifyEventProcessors(eventProcessors, prepared, hint);
    return result.then((evt) => {
      if (evt) {
        applyDebugMeta(evt);
      }
      if (typeof normalizeDepth === "number" && normalizeDepth > 0) {
        return normalizeEvent(evt, normalizeDepth, normalizeMaxBreadth);
      }
      return evt;
    });
  }
  function applyClientOptions(event, options) {
    const { environment, release, dist, maxValueLength = 250 } = options;
    if (!("environment" in event)) {
      event.environment = "environment" in options ? environment : DEFAULT_ENVIRONMENT;
    }
    if (event.release === void 0 && release !== void 0) {
      event.release = release;
    }
    if (event.dist === void 0 && dist !== void 0) {
      event.dist = dist;
    }
    if (event.message) {
      event.message = truncate(event.message, maxValueLength);
    }
    const exception = event.exception && event.exception.values && event.exception.values[0];
    if (exception && exception.value) {
      exception.value = truncate(exception.value, maxValueLength);
    }
    const request = event.request;
    if (request && request.url) {
      request.url = truncate(request.url, maxValueLength);
    }
  }
  var debugIdStackParserCache = /* @__PURE__ */ new WeakMap();
  function applyDebugIds(event, stackParser) {
    const debugIdMap = GLOBAL_OBJ._sentryDebugIds;
    if (!debugIdMap) {
      return;
    }
    let debugIdStackFramesCache;
    const cachedDebugIdStackFrameCache = debugIdStackParserCache.get(stackParser);
    if (cachedDebugIdStackFrameCache) {
      debugIdStackFramesCache = cachedDebugIdStackFrameCache;
    } else {
      debugIdStackFramesCache = /* @__PURE__ */ new Map();
      debugIdStackParserCache.set(stackParser, debugIdStackFramesCache);
    }
    const filenameDebugIdMap = Object.keys(debugIdMap).reduce((acc, debugIdStackTrace) => {
      let parsedStack;
      const cachedParsedStack = debugIdStackFramesCache.get(debugIdStackTrace);
      if (cachedParsedStack) {
        parsedStack = cachedParsedStack;
      } else {
        parsedStack = stackParser(debugIdStackTrace);
        debugIdStackFramesCache.set(debugIdStackTrace, parsedStack);
      }
      for (let i = parsedStack.length - 1; i >= 0; i--) {
        const stackFrame = parsedStack[i];
        if (stackFrame.filename) {
          acc[stackFrame.filename] = debugIdMap[debugIdStackTrace];
          break;
        }
      }
      return acc;
    }, {});
    try {
      event.exception.values.forEach((exception) => {
        exception.stacktrace.frames.forEach((frame) => {
          if (frame.filename) {
            frame.debug_id = filenameDebugIdMap[frame.filename];
          }
        });
      });
    } catch (e) {
    }
  }
  function applyDebugMeta(event) {
    const filenameDebugIdMap = {};
    try {
      event.exception.values.forEach((exception) => {
        exception.stacktrace.frames.forEach((frame) => {
          if (frame.debug_id) {
            if (frame.abs_path) {
              filenameDebugIdMap[frame.abs_path] = frame.debug_id;
            } else if (frame.filename) {
              filenameDebugIdMap[frame.filename] = frame.debug_id;
            }
            delete frame.debug_id;
          }
        });
      });
    } catch (e) {
    }
    if (Object.keys(filenameDebugIdMap).length === 0) {
      return;
    }
    event.debug_meta = event.debug_meta || {};
    event.debug_meta.images = event.debug_meta.images || [];
    const images = event.debug_meta.images;
    Object.keys(filenameDebugIdMap).forEach((filename) => {
      images.push({
        type: "sourcemap",
        code_file: filename,
        debug_id: filenameDebugIdMap[filename]
      });
    });
  }
  function applyIntegrationsMetadata(event, integrationNames) {
    if (integrationNames.length > 0) {
      event.sdk = event.sdk || {};
      event.sdk.integrations = [...event.sdk.integrations || [], ...integrationNames];
    }
  }
  function normalizeEvent(event, depth, maxBreadth) {
    if (!event) {
      return null;
    }
    const normalized = __spreadValues(__spreadValues(__spreadValues(__spreadValues(__spreadValues({}, event), event.breadcrumbs && {
      breadcrumbs: event.breadcrumbs.map((b) => __spreadValues(__spreadValues({}, b), b.data && {
        data: normalize(b.data, depth, maxBreadth)
      }))
    }), event.user && {
      user: normalize(event.user, depth, maxBreadth)
    }), event.contexts && {
      contexts: normalize(event.contexts, depth, maxBreadth)
    }), event.extra && {
      extra: normalize(event.extra, depth, maxBreadth)
    });
    if (event.contexts && event.contexts.trace && normalized.contexts) {
      normalized.contexts.trace = event.contexts.trace;
      if (event.contexts.trace.data) {
        normalized.contexts.trace.data = normalize(event.contexts.trace.data, depth, maxBreadth);
      }
    }
    if (event.spans) {
      normalized.spans = event.spans.map((span) => {
        const data = spanToJSON(span).data;
        if (data) {
          span.data = normalize(data, depth, maxBreadth);
        }
        return span;
      });
    }
    return normalized;
  }
  function getFinalScope(scope, captureContext) {
    if (!captureContext) {
      return scope;
    }
    const finalScope = scope ? scope.clone() : new Scope();
    finalScope.update(captureContext);
    return finalScope;
  }
  function parseEventHintOrCaptureContext(hint) {
    if (!hint) {
      return void 0;
    }
    if (hintIsScopeOrFunction(hint)) {
      return { captureContext: hint };
    }
    if (hintIsScopeContext(hint)) {
      return {
        captureContext: hint
      };
    }
    return hint;
  }
  function hintIsScopeOrFunction(hint) {
    return hint instanceof Scope || typeof hint === "function";
  }
  var captureContextKeys = [
    "user",
    "level",
    "extra",
    "contexts",
    "tags",
    "fingerprint",
    "requestSession",
    "propagationContext"
  ];
  function hintIsScopeContext(hint) {
    return Object.keys(hint).some((key) => captureContextKeys.includes(key));
  }

  // node_modules/@sentry/core/esm/exports.js
  function captureException(exception, hint) {
    return getCurrentHub().captureException(exception, parseEventHintOrCaptureContext(hint));
  }
  function captureEvent(event, hint) {
    return getCurrentHub().captureEvent(event, hint);
  }
  function addBreadcrumb(breadcrumb, hint) {
    getCurrentHub().addBreadcrumb(breadcrumb, hint);
  }
  function withScope(...rest) {
    const hub = getCurrentHub();
    if (rest.length === 2) {
      const [scope, callback] = rest;
      if (!scope) {
        return hub.withScope(callback);
      }
      return hub.withScope(() => {
        hub.getStackTop().scope = scope;
        return callback(scope);
      });
    }
    return hub.withScope(rest[0]);
  }
  function getClient() {
    return getCurrentHub().getClient();
  }
  function getCurrentScope() {
    return getCurrentHub().getScope();
  }
  function startSession(context) {
    const client = getClient();
    const isolationScope = getIsolationScope();
    const currentScope = getCurrentScope();
    const { release, environment = DEFAULT_ENVIRONMENT } = client && client.getOptions() || {};
    const { userAgent } = GLOBAL_OBJ.navigator || {};
    const session = makeSession(__spreadValues(__spreadValues({
      release,
      environment,
      user: currentScope.getUser() || isolationScope.getUser()
    }, userAgent && { userAgent }), context));
    const currentSession = isolationScope.getSession();
    if (currentSession && currentSession.status === "ok") {
      updateSession(currentSession, { status: "exited" });
    }
    endSession();
    isolationScope.setSession(session);
    currentScope.setSession(session);
    return session;
  }
  function endSession() {
    const isolationScope = getIsolationScope();
    const currentScope = getCurrentScope();
    const session = currentScope.getSession() || isolationScope.getSession();
    if (session) {
      closeSession(session);
    }
    _sendSessionUpdate();
    isolationScope.setSession();
    currentScope.setSession();
  }
  function _sendSessionUpdate() {
    const isolationScope = getIsolationScope();
    const currentScope = getCurrentScope();
    const client = getClient();
    const session = currentScope.getSession() || isolationScope.getSession();
    if (session && client && client.captureSession) {
      client.captureSession(session);
    }
  }
  function captureSession(end = false) {
    if (end) {
      endSession();
      return;
    }
    _sendSessionUpdate();
  }

  // node_modules/@sentry/core/esm/utils/getRootSpan.js
  function getRootSpan(span) {
    return span.transaction;
  }

  // node_modules/@sentry/core/esm/tracing/dynamicSamplingContext.js
  function getDynamicSamplingContextFromClient(trace_id, client, scope) {
    const options = client.getOptions();
    const { publicKey: public_key } = client.getDsn() || {};
    const { segment: user_segment } = scope && scope.getUser() || {};
    const dsc = dropUndefinedKeys({
      environment: options.environment || DEFAULT_ENVIRONMENT,
      release: options.release,
      user_segment,
      public_key,
      trace_id
    });
    client.emit && client.emit("createDsc", dsc);
    return dsc;
  }
  function getDynamicSamplingContextFromSpan(span) {
    const client = getClient();
    if (!client) {
      return {};
    }
    const dsc = getDynamicSamplingContextFromClient(spanToJSON(span).trace_id || "", client, getCurrentScope());
    const txn = getRootSpan(span);
    if (!txn) {
      return dsc;
    }
    const v7FrozenDsc = txn && txn._frozenDynamicSamplingContext;
    if (v7FrozenDsc) {
      return v7FrozenDsc;
    }
    const { sampleRate: maybeSampleRate, source } = txn.metadata;
    if (maybeSampleRate != null) {
      dsc.sample_rate = `${maybeSampleRate}`;
    }
    const jsonSpan = spanToJSON(txn);
    if (source && source !== "url") {
      dsc.transaction = jsonSpan.description;
    }
    dsc.sampled = String(spanIsSampled(txn));
    client.emit && client.emit("createDsc", dsc);
    return dsc;
  }

  // node_modules/@sentry/core/esm/utils/applyScopeDataToEvent.js
  function applyScopeDataToEvent(event, data) {
    const { fingerprint, span, breadcrumbs, sdkProcessingMetadata } = data;
    applyDataToEvent(event, data);
    if (span) {
      applySpanToEvent(event, span);
    }
    applyFingerprintToEvent(event, fingerprint);
    applyBreadcrumbsToEvent(event, breadcrumbs);
    applySdkMetadataToEvent(event, sdkProcessingMetadata);
  }
  function mergeScopeData(data, mergeData) {
    const {
      extra,
      tags,
      user,
      contexts,
      level,
      sdkProcessingMetadata,
      breadcrumbs,
      fingerprint,
      eventProcessors,
      attachments,
      propagationContext,
      transactionName,
      span
    } = mergeData;
    mergeAndOverwriteScopeData(data, "extra", extra);
    mergeAndOverwriteScopeData(data, "tags", tags);
    mergeAndOverwriteScopeData(data, "user", user);
    mergeAndOverwriteScopeData(data, "contexts", contexts);
    mergeAndOverwriteScopeData(data, "sdkProcessingMetadata", sdkProcessingMetadata);
    if (level) {
      data.level = level;
    }
    if (transactionName) {
      data.transactionName = transactionName;
    }
    if (span) {
      data.span = span;
    }
    if (breadcrumbs.length) {
      data.breadcrumbs = [...data.breadcrumbs, ...breadcrumbs];
    }
    if (fingerprint.length) {
      data.fingerprint = [...data.fingerprint, ...fingerprint];
    }
    if (eventProcessors.length) {
      data.eventProcessors = [...data.eventProcessors, ...eventProcessors];
    }
    if (attachments.length) {
      data.attachments = [...data.attachments, ...attachments];
    }
    data.propagationContext = __spreadValues(__spreadValues({}, data.propagationContext), propagationContext);
  }
  function mergeAndOverwriteScopeData(data, prop, mergeVal) {
    if (mergeVal && Object.keys(mergeVal).length) {
      data[prop] = __spreadValues({}, data[prop]);
      for (const key in mergeVal) {
        if (Object.prototype.hasOwnProperty.call(mergeVal, key)) {
          data[prop][key] = mergeVal[key];
        }
      }
    }
  }
  function applyDataToEvent(event, data) {
    const {
      extra,
      tags,
      user,
      contexts,
      level,
      transactionName
    } = data;
    const cleanedExtra = dropUndefinedKeys(extra);
    if (cleanedExtra && Object.keys(cleanedExtra).length) {
      event.extra = __spreadValues(__spreadValues({}, cleanedExtra), event.extra);
    }
    const cleanedTags = dropUndefinedKeys(tags);
    if (cleanedTags && Object.keys(cleanedTags).length) {
      event.tags = __spreadValues(__spreadValues({}, cleanedTags), event.tags);
    }
    const cleanedUser = dropUndefinedKeys(user);
    if (cleanedUser && Object.keys(cleanedUser).length) {
      event.user = __spreadValues(__spreadValues({}, cleanedUser), event.user);
    }
    const cleanedContexts = dropUndefinedKeys(contexts);
    if (cleanedContexts && Object.keys(cleanedContexts).length) {
      event.contexts = __spreadValues(__spreadValues({}, cleanedContexts), event.contexts);
    }
    if (level) {
      event.level = level;
    }
    if (transactionName) {
      event.transaction = transactionName;
    }
  }
  function applyBreadcrumbsToEvent(event, breadcrumbs) {
    const mergedBreadcrumbs = [...event.breadcrumbs || [], ...breadcrumbs];
    event.breadcrumbs = mergedBreadcrumbs.length ? mergedBreadcrumbs : void 0;
  }
  function applySdkMetadataToEvent(event, sdkProcessingMetadata) {
    event.sdkProcessingMetadata = __spreadValues(__spreadValues({}, event.sdkProcessingMetadata), sdkProcessingMetadata);
  }
  function applySpanToEvent(event, span) {
    event.contexts = __spreadValues({ trace: spanToTraceContext(span) }, event.contexts);
    const rootSpan = getRootSpan(span);
    if (rootSpan) {
      event.sdkProcessingMetadata = __spreadValues({
        dynamicSamplingContext: getDynamicSamplingContextFromSpan(span)
      }, event.sdkProcessingMetadata);
      const transactionName = spanToJSON(rootSpan).description;
      if (transactionName) {
        event.tags = __spreadValues({ transaction: transactionName }, event.tags);
      }
    }
  }
  function applyFingerprintToEvent(event, fingerprint) {
    event.fingerprint = event.fingerprint ? arrayify(event.fingerprint) : [];
    if (fingerprint) {
      event.fingerprint = event.fingerprint.concat(fingerprint);
    }
    if (event.fingerprint && !event.fingerprint.length) {
      delete event.fingerprint;
    }
  }

  // node_modules/@sentry/core/esm/scope.js
  var DEFAULT_MAX_BREADCRUMBS = 100;
  var globalScope;
  var Scope = class {
    constructor() {
      this._notifyingListeners = false;
      this._scopeListeners = [];
      this._eventProcessors = [];
      this._breadcrumbs = [];
      this._attachments = [];
      this._user = {};
      this._tags = {};
      this._extra = {};
      this._contexts = {};
      this._sdkProcessingMetadata = {};
      this._propagationContext = generatePropagationContext();
    }
    static clone(scope) {
      return scope ? scope.clone() : new Scope();
    }
    clone() {
      const newScope = new Scope();
      newScope._breadcrumbs = [...this._breadcrumbs];
      newScope._tags = __spreadValues({}, this._tags);
      newScope._extra = __spreadValues({}, this._extra);
      newScope._contexts = __spreadValues({}, this._contexts);
      newScope._user = this._user;
      newScope._level = this._level;
      newScope._span = this._span;
      newScope._session = this._session;
      newScope._transactionName = this._transactionName;
      newScope._fingerprint = this._fingerprint;
      newScope._eventProcessors = [...this._eventProcessors];
      newScope._requestSession = this._requestSession;
      newScope._attachments = [...this._attachments];
      newScope._sdkProcessingMetadata = __spreadValues({}, this._sdkProcessingMetadata);
      newScope._propagationContext = __spreadValues({}, this._propagationContext);
      newScope._client = this._client;
      return newScope;
    }
    setClient(client) {
      this._client = client;
    }
    getClient() {
      return this._client;
    }
    addScopeListener(callback) {
      this._scopeListeners.push(callback);
    }
    addEventProcessor(callback) {
      this._eventProcessors.push(callback);
      return this;
    }
    setUser(user) {
      this._user = user || {
        email: void 0,
        id: void 0,
        ip_address: void 0,
        segment: void 0,
        username: void 0
      };
      if (this._session) {
        updateSession(this._session, { user });
      }
      this._notifyScopeListeners();
      return this;
    }
    getUser() {
      return this._user;
    }
    getRequestSession() {
      return this._requestSession;
    }
    setRequestSession(requestSession) {
      this._requestSession = requestSession;
      return this;
    }
    setTags(tags) {
      this._tags = __spreadValues(__spreadValues({}, this._tags), tags);
      this._notifyScopeListeners();
      return this;
    }
    setTag(key, value) {
      this._tags = __spreadProps(__spreadValues({}, this._tags), { [key]: value });
      this._notifyScopeListeners();
      return this;
    }
    setExtras(extras) {
      this._extra = __spreadValues(__spreadValues({}, this._extra), extras);
      this._notifyScopeListeners();
      return this;
    }
    setExtra(key, extra) {
      this._extra = __spreadProps(__spreadValues({}, this._extra), { [key]: extra });
      this._notifyScopeListeners();
      return this;
    }
    setFingerprint(fingerprint) {
      this._fingerprint = fingerprint;
      this._notifyScopeListeners();
      return this;
    }
    setLevel(level) {
      this._level = level;
      this._notifyScopeListeners();
      return this;
    }
    setTransactionName(name) {
      this._transactionName = name;
      this._notifyScopeListeners();
      return this;
    }
    setContext(key, context) {
      if (context === null) {
        delete this._contexts[key];
      } else {
        this._contexts[key] = context;
      }
      this._notifyScopeListeners();
      return this;
    }
    setSpan(span) {
      this._span = span;
      this._notifyScopeListeners();
      return this;
    }
    getSpan() {
      return this._span;
    }
    getTransaction() {
      const span = this._span;
      return span && span.transaction;
    }
    setSession(session) {
      if (!session) {
        delete this._session;
      } else {
        this._session = session;
      }
      this._notifyScopeListeners();
      return this;
    }
    getSession() {
      return this._session;
    }
    update(captureContext) {
      if (!captureContext) {
        return this;
      }
      const scopeToMerge = typeof captureContext === "function" ? captureContext(this) : captureContext;
      if (scopeToMerge instanceof Scope) {
        const scopeData = scopeToMerge.getScopeData();
        this._tags = __spreadValues(__spreadValues({}, this._tags), scopeData.tags);
        this._extra = __spreadValues(__spreadValues({}, this._extra), scopeData.extra);
        this._contexts = __spreadValues(__spreadValues({}, this._contexts), scopeData.contexts);
        if (scopeData.user && Object.keys(scopeData.user).length) {
          this._user = scopeData.user;
        }
        if (scopeData.level) {
          this._level = scopeData.level;
        }
        if (scopeData.fingerprint.length) {
          this._fingerprint = scopeData.fingerprint;
        }
        if (scopeToMerge.getRequestSession()) {
          this._requestSession = scopeToMerge.getRequestSession();
        }
        if (scopeData.propagationContext) {
          this._propagationContext = scopeData.propagationContext;
        }
      } else if (isPlainObject(scopeToMerge)) {
        const scopeContext = captureContext;
        this._tags = __spreadValues(__spreadValues({}, this._tags), scopeContext.tags);
        this._extra = __spreadValues(__spreadValues({}, this._extra), scopeContext.extra);
        this._contexts = __spreadValues(__spreadValues({}, this._contexts), scopeContext.contexts);
        if (scopeContext.user) {
          this._user = scopeContext.user;
        }
        if (scopeContext.level) {
          this._level = scopeContext.level;
        }
        if (scopeContext.fingerprint) {
          this._fingerprint = scopeContext.fingerprint;
        }
        if (scopeContext.requestSession) {
          this._requestSession = scopeContext.requestSession;
        }
        if (scopeContext.propagationContext) {
          this._propagationContext = scopeContext.propagationContext;
        }
      }
      return this;
    }
    clear() {
      this._breadcrumbs = [];
      this._tags = {};
      this._extra = {};
      this._user = {};
      this._contexts = {};
      this._level = void 0;
      this._transactionName = void 0;
      this._fingerprint = void 0;
      this._requestSession = void 0;
      this._span = void 0;
      this._session = void 0;
      this._notifyScopeListeners();
      this._attachments = [];
      this._propagationContext = generatePropagationContext();
      return this;
    }
    addBreadcrumb(breadcrumb, maxBreadcrumbs) {
      const maxCrumbs = typeof maxBreadcrumbs === "number" ? maxBreadcrumbs : DEFAULT_MAX_BREADCRUMBS;
      if (maxCrumbs <= 0) {
        return this;
      }
      const mergedBreadcrumb = __spreadValues({
        timestamp: dateTimestampInSeconds()
      }, breadcrumb);
      const breadcrumbs = this._breadcrumbs;
      breadcrumbs.push(mergedBreadcrumb);
      this._breadcrumbs = breadcrumbs.length > maxCrumbs ? breadcrumbs.slice(-maxCrumbs) : breadcrumbs;
      this._notifyScopeListeners();
      return this;
    }
    getLastBreadcrumb() {
      return this._breadcrumbs[this._breadcrumbs.length - 1];
    }
    clearBreadcrumbs() {
      this._breadcrumbs = [];
      this._notifyScopeListeners();
      return this;
    }
    addAttachment(attachment) {
      this._attachments.push(attachment);
      return this;
    }
    getAttachments() {
      const data = this.getScopeData();
      return data.attachments;
    }
    clearAttachments() {
      this._attachments = [];
      return this;
    }
    getScopeData() {
      const {
        _breadcrumbs,
        _attachments,
        _contexts,
        _tags,
        _extra,
        _user,
        _level,
        _fingerprint,
        _eventProcessors,
        _propagationContext,
        _sdkProcessingMetadata,
        _transactionName,
        _span
      } = this;
      return {
        breadcrumbs: _breadcrumbs,
        attachments: _attachments,
        contexts: _contexts,
        tags: _tags,
        extra: _extra,
        user: _user,
        level: _level,
        fingerprint: _fingerprint || [],
        eventProcessors: _eventProcessors,
        propagationContext: _propagationContext,
        sdkProcessingMetadata: _sdkProcessingMetadata,
        transactionName: _transactionName,
        span: _span
      };
    }
    applyToEvent(event, hint = {}, additionalEventProcessors = []) {
      applyScopeDataToEvent(event, this.getScopeData());
      const eventProcessors = [
        ...additionalEventProcessors,
        ...getGlobalEventProcessors(),
        ...this._eventProcessors
      ];
      return notifyEventProcessors(eventProcessors, event, hint);
    }
    setSDKProcessingMetadata(newData) {
      this._sdkProcessingMetadata = __spreadValues(__spreadValues({}, this._sdkProcessingMetadata), newData);
      return this;
    }
    setPropagationContext(context) {
      this._propagationContext = context;
      return this;
    }
    getPropagationContext() {
      return this._propagationContext;
    }
    captureException(exception, hint) {
      const eventId = hint && hint.event_id ? hint.event_id : uuid4();
      if (!this._client) {
        logger.warn("No client configured on scope - will not capture exception!");
        return eventId;
      }
      const syntheticException = new Error("Sentry syntheticException");
      this._client.captureException(
        exception,
        __spreadProps(__spreadValues({
          originalException: exception,
          syntheticException
        }, hint), {
          event_id: eventId
        }),
        this
      );
      return eventId;
    }
    captureMessage(message, level, hint) {
      const eventId = hint && hint.event_id ? hint.event_id : uuid4();
      if (!this._client) {
        logger.warn("No client configured on scope - will not capture message!");
        return eventId;
      }
      const syntheticException = new Error(message);
      this._client.captureMessage(
        message,
        level,
        __spreadProps(__spreadValues({
          originalException: message,
          syntheticException
        }, hint), {
          event_id: eventId
        }),
        this
      );
      return eventId;
    }
    captureEvent(event, hint) {
      const eventId = hint && hint.event_id ? hint.event_id : uuid4();
      if (!this._client) {
        logger.warn("No client configured on scope - will not capture event!");
        return eventId;
      }
      this._client.captureEvent(event, __spreadProps(__spreadValues({}, hint), { event_id: eventId }), this);
      return eventId;
    }
    _notifyScopeListeners() {
      if (!this._notifyingListeners) {
        this._notifyingListeners = true;
        this._scopeListeners.forEach((callback) => {
          callback(this);
        });
        this._notifyingListeners = false;
      }
    }
  };
  function getGlobalScope() {
    if (!globalScope) {
      globalScope = new Scope();
    }
    return globalScope;
  }
  function generatePropagationContext() {
    return {
      traceId: uuid4(),
      spanId: uuid4().substring(16)
    };
  }

  // node_modules/@sentry/core/esm/version.js
  var SDK_VERSION = "7.119.1";

  // node_modules/@sentry/core/esm/hub.js
  var API_VERSION = parseFloat(SDK_VERSION);
  var DEFAULT_BREADCRUMBS = 100;
  var Hub = class {
    constructor(client, scope, isolationScope, _version = API_VERSION) {
      this._version = _version;
      let assignedScope;
      if (!scope) {
        assignedScope = new Scope();
        assignedScope.setClient(client);
      } else {
        assignedScope = scope;
      }
      let assignedIsolationScope;
      if (!isolationScope) {
        assignedIsolationScope = new Scope();
        assignedIsolationScope.setClient(client);
      } else {
        assignedIsolationScope = isolationScope;
      }
      this._stack = [{ scope: assignedScope }];
      if (client) {
        this.bindClient(client);
      }
      this._isolationScope = assignedIsolationScope;
    }
    isOlderThan(version) {
      return this._version < version;
    }
    bindClient(client) {
      const top = this.getStackTop();
      top.client = client;
      top.scope.setClient(client);
      if (client && client.setupIntegrations) {
        client.setupIntegrations();
      }
    }
    pushScope() {
      const scope = this.getScope().clone();
      this.getStack().push({
        client: this.getClient(),
        scope
      });
      return scope;
    }
    popScope() {
      if (this.getStack().length <= 1)
        return false;
      return !!this.getStack().pop();
    }
    withScope(callback) {
      const scope = this.pushScope();
      let maybePromiseResult;
      try {
        maybePromiseResult = callback(scope);
      } catch (e) {
        this.popScope();
        throw e;
      }
      if (isThenable(maybePromiseResult)) {
        return maybePromiseResult.then(
          (res) => {
            this.popScope();
            return res;
          },
          (e) => {
            this.popScope();
            throw e;
          }
        );
      }
      this.popScope();
      return maybePromiseResult;
    }
    getClient() {
      return this.getStackTop().client;
    }
    getScope() {
      return this.getStackTop().scope;
    }
    getIsolationScope() {
      return this._isolationScope;
    }
    getStack() {
      return this._stack;
    }
    getStackTop() {
      return this._stack[this._stack.length - 1];
    }
    captureException(exception, hint) {
      const eventId = this._lastEventId = hint && hint.event_id ? hint.event_id : uuid4();
      const syntheticException = new Error("Sentry syntheticException");
      this.getScope().captureException(exception, __spreadProps(__spreadValues({
        originalException: exception,
        syntheticException
      }, hint), {
        event_id: eventId
      }));
      return eventId;
    }
    captureMessage(message, level, hint) {
      const eventId = this._lastEventId = hint && hint.event_id ? hint.event_id : uuid4();
      const syntheticException = new Error(message);
      this.getScope().captureMessage(message, level, __spreadProps(__spreadValues({
        originalException: message,
        syntheticException
      }, hint), {
        event_id: eventId
      }));
      return eventId;
    }
    captureEvent(event, hint) {
      const eventId = hint && hint.event_id ? hint.event_id : uuid4();
      if (!event.type) {
        this._lastEventId = eventId;
      }
      this.getScope().captureEvent(event, __spreadProps(__spreadValues({}, hint), { event_id: eventId }));
      return eventId;
    }
    lastEventId() {
      return this._lastEventId;
    }
    addBreadcrumb(breadcrumb, hint) {
      const { scope, client } = this.getStackTop();
      if (!client)
        return;
      const { beforeBreadcrumb = null, maxBreadcrumbs = DEFAULT_BREADCRUMBS } = client.getOptions && client.getOptions() || {};
      if (maxBreadcrumbs <= 0)
        return;
      const timestamp = dateTimestampInSeconds();
      const mergedBreadcrumb = __spreadValues({ timestamp }, breadcrumb);
      const finalBreadcrumb = beforeBreadcrumb ? consoleSandbox(() => beforeBreadcrumb(mergedBreadcrumb, hint)) : mergedBreadcrumb;
      if (finalBreadcrumb === null)
        return;
      if (client.emit) {
        client.emit("beforeAddBreadcrumb", finalBreadcrumb, hint);
      }
      scope.addBreadcrumb(finalBreadcrumb, maxBreadcrumbs);
    }
    setUser(user) {
      this.getScope().setUser(user);
      this.getIsolationScope().setUser(user);
    }
    setTags(tags) {
      this.getScope().setTags(tags);
      this.getIsolationScope().setTags(tags);
    }
    setExtras(extras) {
      this.getScope().setExtras(extras);
      this.getIsolationScope().setExtras(extras);
    }
    setTag(key, value) {
      this.getScope().setTag(key, value);
      this.getIsolationScope().setTag(key, value);
    }
    setExtra(key, extra) {
      this.getScope().setExtra(key, extra);
      this.getIsolationScope().setExtra(key, extra);
    }
    setContext(name, context) {
      this.getScope().setContext(name, context);
      this.getIsolationScope().setContext(name, context);
    }
    configureScope(callback) {
      const { scope, client } = this.getStackTop();
      if (client) {
        callback(scope);
      }
    }
    run(callback) {
      const oldHub = makeMain(this);
      try {
        callback(this);
      } finally {
        makeMain(oldHub);
      }
    }
    getIntegration(integration) {
      const client = this.getClient();
      if (!client)
        return null;
      try {
        return client.getIntegration(integration);
      } catch (_oO) {
        DEBUG_BUILD2 && logger.warn(`Cannot retrieve integration ${integration.id} from the current Hub`);
        return null;
      }
    }
    startTransaction(context, customSamplingContext) {
      const result = this._callExtensionMethod("startTransaction", context, customSamplingContext);
      if (DEBUG_BUILD2 && !result) {
        const client = this.getClient();
        if (!client) {
          logger.warn(
            "Tracing extension 'startTransaction' is missing. You should 'init' the SDK before calling 'startTransaction'"
          );
        } else {
          logger.warn(`Tracing extension 'startTransaction' has not been added. Call 'addTracingExtensions' before calling 'init':
Sentry.addTracingExtensions();
Sentry.init({...});
`);
        }
      }
      return result;
    }
    traceHeaders() {
      return this._callExtensionMethod("traceHeaders");
    }
    captureSession(endSession2 = false) {
      if (endSession2) {
        return this.endSession();
      }
      this._sendSessionUpdate();
    }
    endSession() {
      const layer = this.getStackTop();
      const scope = layer.scope;
      const session = scope.getSession();
      if (session) {
        closeSession(session);
      }
      this._sendSessionUpdate();
      scope.setSession();
    }
    startSession(context) {
      const { scope, client } = this.getStackTop();
      const { release, environment = DEFAULT_ENVIRONMENT } = client && client.getOptions() || {};
      const { userAgent } = GLOBAL_OBJ.navigator || {};
      const session = makeSession(__spreadValues(__spreadValues({
        release,
        environment,
        user: scope.getUser()
      }, userAgent && { userAgent }), context));
      const currentSession = scope.getSession && scope.getSession();
      if (currentSession && currentSession.status === "ok") {
        updateSession(currentSession, { status: "exited" });
      }
      this.endSession();
      scope.setSession(session);
      return session;
    }
    shouldSendDefaultPii() {
      const client = this.getClient();
      const options = client && client.getOptions();
      return Boolean(options && options.sendDefaultPii);
    }
    _sendSessionUpdate() {
      const { scope, client } = this.getStackTop();
      const session = scope.getSession();
      if (session && client && client.captureSession) {
        client.captureSession(session);
      }
    }
    _callExtensionMethod(method, ...args) {
      const carrier = getMainCarrier();
      const sentry = carrier.__SENTRY__;
      if (sentry && sentry.extensions && typeof sentry.extensions[method] === "function") {
        return sentry.extensions[method].apply(this, args);
      }
      DEBUG_BUILD2 && logger.warn(`Extension method ${method} couldn't be found, doing nothing.`);
    }
  };
  function getMainCarrier() {
    GLOBAL_OBJ.__SENTRY__ = GLOBAL_OBJ.__SENTRY__ || {
      extensions: {},
      hub: void 0
    };
    return GLOBAL_OBJ;
  }
  function makeMain(hub) {
    const registry = getMainCarrier();
    const oldHub = getHubFromCarrier(registry);
    setHubOnCarrier(registry, hub);
    return oldHub;
  }
  function getCurrentHub() {
    const registry = getMainCarrier();
    if (registry.__SENTRY__ && registry.__SENTRY__.acs) {
      const hub = registry.__SENTRY__.acs.getCurrentHub();
      if (hub) {
        return hub;
      }
    }
    return getGlobalHub(registry);
  }
  function getIsolationScope() {
    return getCurrentHub().getIsolationScope();
  }
  function getGlobalHub(registry = getMainCarrier()) {
    if (!hasHubOnCarrier(registry) || getHubFromCarrier(registry).isOlderThan(API_VERSION)) {
      setHubOnCarrier(registry, new Hub());
    }
    return getHubFromCarrier(registry);
  }
  function hasHubOnCarrier(carrier) {
    return !!(carrier && carrier.__SENTRY__ && carrier.__SENTRY__.hub);
  }
  function getHubFromCarrier(carrier) {
    return getGlobalSingleton("hub", () => new Hub(), carrier);
  }
  function setHubOnCarrier(carrier, hub) {
    if (!carrier)
      return false;
    const __SENTRY__ = carrier.__SENTRY__ = carrier.__SENTRY__ || {};
    __SENTRY__.hub = hub;
    return true;
  }

  // node_modules/@sentry/core/esm/envelope.js
  function enhanceEventWithSdkInfo(event, sdkInfo) {
    if (!sdkInfo) {
      return event;
    }
    event.sdk = event.sdk || {};
    event.sdk.name = event.sdk.name || sdkInfo.name;
    event.sdk.version = event.sdk.version || sdkInfo.version;
    event.sdk.integrations = [...event.sdk.integrations || [], ...sdkInfo.integrations || []];
    event.sdk.packages = [...event.sdk.packages || [], ...sdkInfo.packages || []];
    return event;
  }
  function createSessionEnvelope(session, dsn, metadata, tunnel) {
    const sdkInfo = getSdkMetadataForEnvelopeHeader(metadata);
    const envelopeHeaders = __spreadValues(__spreadValues({
      sent_at: new Date().toISOString()
    }, sdkInfo && { sdk: sdkInfo }), !!tunnel && dsn && { dsn: dsnToString(dsn) });
    const envelopeItem = "aggregates" in session ? [{ type: "sessions" }, session] : [{ type: "session" }, session.toJSON()];
    return createEnvelope(envelopeHeaders, [envelopeItem]);
  }
  function createEventEnvelope(event, dsn, metadata, tunnel) {
    const sdkInfo = getSdkMetadataForEnvelopeHeader(metadata);
    const eventType = event.type && event.type !== "replay_event" ? event.type : "event";
    enhanceEventWithSdkInfo(event, metadata && metadata.sdk);
    const envelopeHeaders = createEventEnvelopeHeaders(event, sdkInfo, tunnel, dsn);
    delete event.sdkProcessingMetadata;
    const eventItem = [{ type: eventType }, event];
    return createEnvelope(envelopeHeaders, [eventItem]);
  }

  // node_modules/@sentry/core/esm/api.js
  var SENTRY_API_VERSION = "7";
  function getBaseApiEndpoint(dsn) {
    const protocol = dsn.protocol ? `${dsn.protocol}:` : "";
    const port = dsn.port ? `:${dsn.port}` : "";
    return `${protocol}//${dsn.host}${port}${dsn.path ? `/${dsn.path}` : ""}/api/`;
  }
  function _getIngestEndpoint(dsn) {
    return `${getBaseApiEndpoint(dsn)}${dsn.projectId}/envelope/`;
  }
  function _encodedAuth(dsn, sdkInfo) {
    return urlEncode(__spreadValues({
      sentry_key: dsn.publicKey,
      sentry_version: SENTRY_API_VERSION
    }, sdkInfo && { sentry_client: `${sdkInfo.name}/${sdkInfo.version}` }));
  }
  function getEnvelopeEndpointWithUrlEncodedAuth(dsn, tunnelOrOptions = {}) {
    const tunnel = typeof tunnelOrOptions === "string" ? tunnelOrOptions : tunnelOrOptions.tunnel;
    const sdkInfo = typeof tunnelOrOptions === "string" || !tunnelOrOptions._metadata ? void 0 : tunnelOrOptions._metadata.sdk;
    return tunnel ? tunnel : `${_getIngestEndpoint(dsn)}?${_encodedAuth(dsn, sdkInfo)}`;
  }

  // node_modules/@sentry/core/esm/integration.js
  var installedIntegrations = [];
  function filterDuplicates(integrations) {
    const integrationsByName = {};
    integrations.forEach((currentInstance) => {
      const { name } = currentInstance;
      const existingInstance = integrationsByName[name];
      if (existingInstance && !existingInstance.isDefaultInstance && currentInstance.isDefaultInstance) {
        return;
      }
      integrationsByName[name] = currentInstance;
    });
    return Object.keys(integrationsByName).map((k) => integrationsByName[k]);
  }
  function getIntegrationsToSetup(options) {
    const defaultIntegrations2 = options.defaultIntegrations || [];
    const userIntegrations = options.integrations;
    defaultIntegrations2.forEach((integration) => {
      integration.isDefaultInstance = true;
    });
    let integrations;
    if (Array.isArray(userIntegrations)) {
      integrations = [...defaultIntegrations2, ...userIntegrations];
    } else if (typeof userIntegrations === "function") {
      integrations = arrayify(userIntegrations(defaultIntegrations2));
    } else {
      integrations = defaultIntegrations2;
    }
    const finalIntegrations = filterDuplicates(integrations);
    const debugIndex = findIndex(finalIntegrations, (integration) => integration.name === "Debug");
    if (debugIndex !== -1) {
      const [debugInstance] = finalIntegrations.splice(debugIndex, 1);
      finalIntegrations.push(debugInstance);
    }
    return finalIntegrations;
  }
  function setupIntegrations(client, integrations) {
    const integrationIndex = {};
    integrations.forEach((integration) => {
      if (integration) {
        setupIntegration(client, integration, integrationIndex);
      }
    });
    return integrationIndex;
  }
  function afterSetupIntegrations(client, integrations) {
    for (const integration of integrations) {
      if (integration && integration.afterAllSetup) {
        integration.afterAllSetup(client);
      }
    }
  }
  function setupIntegration(client, integration, integrationIndex) {
    if (integrationIndex[integration.name]) {
      DEBUG_BUILD2 && logger.log(`Integration skipped because it was already installed: ${integration.name}`);
      return;
    }
    integrationIndex[integration.name] = integration;
    if (installedIntegrations.indexOf(integration.name) === -1) {
      integration.setupOnce(addGlobalEventProcessor, getCurrentHub);
      installedIntegrations.push(integration.name);
    }
    if (integration.setup && typeof integration.setup === "function") {
      integration.setup(client);
    }
    if (client.on && typeof integration.preprocessEvent === "function") {
      const callback = integration.preprocessEvent.bind(integration);
      client.on("preprocessEvent", (event, hint) => callback(event, hint, client));
    }
    if (client.addEventProcessor && typeof integration.processEvent === "function") {
      const callback = integration.processEvent.bind(integration);
      const processor = Object.assign((event, hint) => callback(event, hint, client), {
        id: integration.name
      });
      client.addEventProcessor(processor);
    }
    DEBUG_BUILD2 && logger.log(`Integration installed: ${integration.name}`);
  }
  function findIndex(arr, callback) {
    for (let i = 0; i < arr.length; i++) {
      if (callback(arr[i]) === true) {
        return i;
      }
    }
    return -1;
  }
  function convertIntegrationFnToClass(name, fn) {
    return Object.assign(
      function ConvertedIntegration(...args) {
        return fn(...args);
      },
      { id: name }
    );
  }
  function defineIntegration(fn) {
    return fn;
  }

  // node_modules/@sentry/core/esm/metrics/utils.js
  function serializeMetricBuckets(metricBucketItems) {
    let out = "";
    for (const item of metricBucketItems) {
      const tagEntries = Object.entries(item.tags);
      const maybeTags = tagEntries.length > 0 ? `|#${tagEntries.map(([key, value]) => `${key}:${value}`).join(",")}` : "";
      out += `${item.name}@${item.unit}:${item.metric}|${item.metricType}${maybeTags}|T${item.timestamp}
`;
    }
    return out;
  }

  // node_modules/@sentry/core/esm/metrics/envelope.js
  function createMetricEnvelope(metricBucketItems, dsn, metadata, tunnel) {
    const headers = {
      sent_at: new Date().toISOString()
    };
    if (metadata && metadata.sdk) {
      headers.sdk = {
        name: metadata.sdk.name,
        version: metadata.sdk.version
      };
    }
    if (!!tunnel && dsn) {
      headers.dsn = dsnToString(dsn);
    }
    const item = createMetricEnvelopeItem(metricBucketItems);
    return createEnvelope(headers, [item]);
  }
  function createMetricEnvelopeItem(metricBucketItems) {
    const payload = serializeMetricBuckets(metricBucketItems);
    const metricHeaders = {
      type: "statsd",
      length: payload.length
    };
    return [metricHeaders, payload];
  }

  // node_modules/@sentry/core/esm/baseclient.js
  var ALREADY_SEEN_ERROR = "Not capturing exception because it's already been captured.";
  var BaseClient = class {
    constructor(options) {
      this._options = options;
      this._integrations = {};
      this._integrationsInitialized = false;
      this._numProcessing = 0;
      this._outcomes = {};
      this._hooks = {};
      this._eventProcessors = [];
      if (options.dsn) {
        this._dsn = makeDsn(options.dsn);
      } else {
        DEBUG_BUILD2 && logger.warn("No DSN provided, client will not send events.");
      }
      if (this._dsn) {
        const url = getEnvelopeEndpointWithUrlEncodedAuth(this._dsn, options);
        this._transport = options.transport(__spreadProps(__spreadValues({
          tunnel: this._options.tunnel,
          recordDroppedEvent: this.recordDroppedEvent.bind(this)
        }, options.transportOptions), {
          url
        }));
      }
    }
    captureException(exception, hint, scope) {
      if (checkOrSetAlreadyCaught(exception)) {
        DEBUG_BUILD2 && logger.log(ALREADY_SEEN_ERROR);
        return;
      }
      let eventId = hint && hint.event_id;
      this._process(
        this.eventFromException(exception, hint).then((event) => this._captureEvent(event, hint, scope)).then((result) => {
          eventId = result;
        })
      );
      return eventId;
    }
    captureMessage(message, level, hint, scope) {
      let eventId = hint && hint.event_id;
      const eventMessage = isParameterizedString(message) ? message : String(message);
      const promisedEvent = isPrimitive(message) ? this.eventFromMessage(eventMessage, level, hint) : this.eventFromException(message, hint);
      this._process(
        promisedEvent.then((event) => this._captureEvent(event, hint, scope)).then((result) => {
          eventId = result;
        })
      );
      return eventId;
    }
    captureEvent(event, hint, scope) {
      if (hint && hint.originalException && checkOrSetAlreadyCaught(hint.originalException)) {
        DEBUG_BUILD2 && logger.log(ALREADY_SEEN_ERROR);
        return;
      }
      let eventId = hint && hint.event_id;
      const sdkProcessingMetadata = event.sdkProcessingMetadata || {};
      const capturedSpanScope = sdkProcessingMetadata.capturedSpanScope;
      this._process(
        this._captureEvent(event, hint, capturedSpanScope || scope).then((result) => {
          eventId = result;
        })
      );
      return eventId;
    }
    captureSession(session) {
      if (!(typeof session.release === "string")) {
        DEBUG_BUILD2 && logger.warn("Discarded session because of missing or non-string release");
      } else {
        this.sendSession(session);
        updateSession(session, { init: false });
      }
    }
    getDsn() {
      return this._dsn;
    }
    getOptions() {
      return this._options;
    }
    getSdkMetadata() {
      return this._options._metadata;
    }
    getTransport() {
      return this._transport;
    }
    flush(timeout) {
      const transport = this._transport;
      if (transport) {
        if (this.metricsAggregator) {
          this.metricsAggregator.flush();
        }
        return this._isClientDoneProcessing(timeout).then((clientFinished) => {
          return transport.flush(timeout).then((transportFlushed) => clientFinished && transportFlushed);
        });
      } else {
        return resolvedSyncPromise(true);
      }
    }
    close(timeout) {
      return this.flush(timeout).then((result) => {
        this.getOptions().enabled = false;
        if (this.metricsAggregator) {
          this.metricsAggregator.close();
        }
        return result;
      });
    }
    getEventProcessors() {
      return this._eventProcessors;
    }
    addEventProcessor(eventProcessor) {
      this._eventProcessors.push(eventProcessor);
    }
    setupIntegrations(forceInitialize) {
      if (forceInitialize && !this._integrationsInitialized || this._isEnabled() && !this._integrationsInitialized) {
        this._setupIntegrations();
      }
    }
    init() {
      if (this._isEnabled()) {
        this._setupIntegrations();
      }
    }
    getIntegrationById(integrationId) {
      return this.getIntegrationByName(integrationId);
    }
    getIntegrationByName(integrationName) {
      return this._integrations[integrationName];
    }
    getIntegration(integration) {
      try {
        return this._integrations[integration.id] || null;
      } catch (_oO) {
        DEBUG_BUILD2 && logger.warn(`Cannot retrieve integration ${integration.id} from the current Client`);
        return null;
      }
    }
    addIntegration(integration) {
      const isAlreadyInstalled = this._integrations[integration.name];
      setupIntegration(this, integration, this._integrations);
      if (!isAlreadyInstalled) {
        afterSetupIntegrations(this, [integration]);
      }
    }
    sendEvent(event, hint = {}) {
      this.emit("beforeSendEvent", event, hint);
      let env = createEventEnvelope(event, this._dsn, this._options._metadata, this._options.tunnel);
      for (const attachment of hint.attachments || []) {
        env = addItemToEnvelope(
          env,
          createAttachmentEnvelopeItem(
            attachment,
            this._options.transportOptions && this._options.transportOptions.textEncoder
          )
        );
      }
      const promise = this._sendEnvelope(env);
      if (promise) {
        promise.then((sendResponse) => this.emit("afterSendEvent", event, sendResponse), null);
      }
    }
    sendSession(session) {
      const env = createSessionEnvelope(session, this._dsn, this._options._metadata, this._options.tunnel);
      this._sendEnvelope(env);
    }
    recordDroppedEvent(reason, category, eventOrCount) {
      if (this._options.sendClientReports) {
        const count = typeof eventOrCount === "number" ? eventOrCount : 1;
        const key = `${reason}:${category}`;
        DEBUG_BUILD2 && logger.log(`Recording outcome: "${key}"${count > 1 ? ` (${count} times)` : ""}`);
        this._outcomes[key] = (this._outcomes[key] || 0) + count;
      }
    }
    captureAggregateMetrics(metricBucketItems) {
      DEBUG_BUILD2 && logger.log(`Flushing aggregated metrics, number of metrics: ${metricBucketItems.length}`);
      const metricsEnvelope = createMetricEnvelope(
        metricBucketItems,
        this._dsn,
        this._options._metadata,
        this._options.tunnel
      );
      this._sendEnvelope(metricsEnvelope);
    }
    on(hook, callback) {
      if (!this._hooks[hook]) {
        this._hooks[hook] = [];
      }
      this._hooks[hook].push(callback);
    }
    emit(hook, ...rest) {
      if (this._hooks[hook]) {
        this._hooks[hook].forEach((callback) => callback(...rest));
      }
    }
    _setupIntegrations() {
      const { integrations } = this._options;
      this._integrations = setupIntegrations(this, integrations);
      afterSetupIntegrations(this, integrations);
      this._integrationsInitialized = true;
    }
    _updateSessionFromEvent(session, event) {
      let crashed = false;
      let errored = false;
      const exceptions = event.exception && event.exception.values;
      if (exceptions) {
        errored = true;
        for (const ex of exceptions) {
          const mechanism = ex.mechanism;
          if (mechanism && mechanism.handled === false) {
            crashed = true;
            break;
          }
        }
      }
      const sessionNonTerminal = session.status === "ok";
      const shouldUpdateAndSend = sessionNonTerminal && session.errors === 0 || sessionNonTerminal && crashed;
      if (shouldUpdateAndSend) {
        updateSession(session, __spreadProps(__spreadValues({}, crashed && { status: "crashed" }), {
          errors: session.errors || Number(errored || crashed)
        }));
        this.captureSession(session);
      }
    }
    _isClientDoneProcessing(timeout) {
      return new SyncPromise((resolve) => {
        let ticked = 0;
        const tick = 1;
        const interval = setInterval(() => {
          if (this._numProcessing == 0) {
            clearInterval(interval);
            resolve(true);
          } else {
            ticked += tick;
            if (timeout && ticked >= timeout) {
              clearInterval(interval);
              resolve(false);
            }
          }
        }, tick);
      });
    }
    _isEnabled() {
      return this.getOptions().enabled !== false && this._transport !== void 0;
    }
    _prepareEvent(event, hint, scope, isolationScope = getIsolationScope()) {
      const options = this.getOptions();
      const integrations = Object.keys(this._integrations);
      if (!hint.integrations && integrations.length > 0) {
        hint.integrations = integrations;
      }
      this.emit("preprocessEvent", event, hint);
      return prepareEvent(options, event, hint, scope, this, isolationScope).then((evt) => {
        if (evt === null) {
          return evt;
        }
        const propagationContext = __spreadValues(__spreadValues({}, isolationScope.getPropagationContext()), scope ? scope.getPropagationContext() : void 0);
        const trace = evt.contexts && evt.contexts.trace;
        if (!trace && propagationContext) {
          const { traceId: trace_id, spanId, parentSpanId, dsc } = propagationContext;
          evt.contexts = __spreadValues({
            trace: {
              trace_id,
              span_id: spanId,
              parent_span_id: parentSpanId
            }
          }, evt.contexts);
          const dynamicSamplingContext = dsc ? dsc : getDynamicSamplingContextFromClient(trace_id, this, scope);
          evt.sdkProcessingMetadata = __spreadValues({
            dynamicSamplingContext
          }, evt.sdkProcessingMetadata);
        }
        return evt;
      });
    }
    _captureEvent(event, hint = {}, scope) {
      return this._processEvent(event, hint, scope).then(
        (finalEvent) => {
          return finalEvent.event_id;
        },
        (reason) => {
          if (DEBUG_BUILD2) {
            const sentryError = reason;
            if (sentryError.logLevel === "log") {
              logger.log(sentryError.message);
            } else {
              logger.warn(sentryError);
            }
          }
          return void 0;
        }
      );
    }
    _processEvent(event, hint, scope) {
      const options = this.getOptions();
      const { sampleRate } = options;
      const isTransaction = isTransactionEvent(event);
      const isError2 = isErrorEvent2(event);
      const eventType = event.type || "error";
      const beforeSendLabel = `before send for type \`${eventType}\``;
      if (isError2 && typeof sampleRate === "number" && Math.random() > sampleRate) {
        this.recordDroppedEvent("sample_rate", "error", event);
        return rejectedSyncPromise(
          new SentryError(
            `Discarding event because it's not included in the random sample (sampling rate = ${sampleRate})`,
            "log"
          )
        );
      }
      const dataCategory = eventType === "replay_event" ? "replay" : eventType;
      const sdkProcessingMetadata = event.sdkProcessingMetadata || {};
      const capturedSpanIsolationScope = sdkProcessingMetadata.capturedSpanIsolationScope;
      return this._prepareEvent(event, hint, scope, capturedSpanIsolationScope).then((prepared) => {
        if (prepared === null) {
          this.recordDroppedEvent("event_processor", dataCategory, event);
          throw new SentryError("An event processor returned `null`, will not send event.", "log");
        }
        const isInternalException = hint.data && hint.data.__sentry__ === true;
        if (isInternalException) {
          return prepared;
        }
        const result = processBeforeSend(options, prepared, hint);
        return _validateBeforeSendResult(result, beforeSendLabel);
      }).then((processedEvent) => {
        if (processedEvent === null) {
          this.recordDroppedEvent("before_send", dataCategory, event);
          if (isTransaction) {
            const spans = event.spans || [];
            const spanCount = 1 + spans.length;
            this.recordDroppedEvent("before_send", "span", spanCount);
          }
          throw new SentryError(`${beforeSendLabel} returned \`null\`, will not send event.`, "log");
        }
        const session = scope && scope.getSession();
        if (!isTransaction && session) {
          this._updateSessionFromEvent(session, processedEvent);
        }
        if (isTransaction) {
          const spanCountBefore = processedEvent.sdkProcessingMetadata && processedEvent.sdkProcessingMetadata.spanCountBeforeProcessing || 0;
          const spanCountAfter = processedEvent.spans ? processedEvent.spans.length : 0;
          const droppedSpanCount = spanCountBefore - spanCountAfter;
          if (droppedSpanCount > 0) {
            this.recordDroppedEvent("before_send", "span", droppedSpanCount);
          }
        }
        const transactionInfo = processedEvent.transaction_info;
        if (isTransaction && transactionInfo && processedEvent.transaction !== event.transaction) {
          const source = "custom";
          processedEvent.transaction_info = __spreadProps(__spreadValues({}, transactionInfo), {
            source
          });
        }
        this.sendEvent(processedEvent, hint);
        return processedEvent;
      }).then(null, (reason) => {
        if (reason instanceof SentryError) {
          throw reason;
        }
        this.captureException(reason, {
          data: {
            __sentry__: true
          },
          originalException: reason
        });
        throw new SentryError(
          `Event processing pipeline threw an error, original event will not be sent. Details have been sent as a new event.
Reason: ${reason}`
        );
      });
    }
    _process(promise) {
      this._numProcessing++;
      void promise.then(
        (value) => {
          this._numProcessing--;
          return value;
        },
        (reason) => {
          this._numProcessing--;
          return reason;
        }
      );
    }
    _sendEnvelope(envelope) {
      this.emit("beforeEnvelope", envelope);
      if (this._isEnabled() && this._transport) {
        return this._transport.send(envelope).then(null, (reason) => {
          DEBUG_BUILD2 && logger.error("Error while sending event:", reason);
        });
      } else {
        DEBUG_BUILD2 && logger.error("Transport disabled");
      }
    }
    _clearOutcomes() {
      const outcomes = this._outcomes;
      this._outcomes = {};
      return Object.keys(outcomes).map((key) => {
        const [reason, category] = key.split(":");
        return {
          reason,
          category,
          quantity: outcomes[key]
        };
      });
    }
  };
  function _validateBeforeSendResult(beforeSendResult, beforeSendLabel) {
    const invalidValueError = `${beforeSendLabel} must return \`null\` or a valid event.`;
    if (isThenable(beforeSendResult)) {
      return beforeSendResult.then(
        (event) => {
          if (!isPlainObject(event) && event !== null) {
            throw new SentryError(invalidValueError);
          }
          return event;
        },
        (e) => {
          throw new SentryError(`${beforeSendLabel} rejected with ${e}`);
        }
      );
    } else if (!isPlainObject(beforeSendResult) && beforeSendResult !== null) {
      throw new SentryError(invalidValueError);
    }
    return beforeSendResult;
  }
  function processBeforeSend(options, event, hint) {
    const { beforeSend, beforeSendTransaction } = options;
    if (isErrorEvent2(event) && beforeSend) {
      return beforeSend(event, hint);
    }
    if (isTransactionEvent(event) && beforeSendTransaction) {
      if (event.spans) {
        const spanCountBefore = event.spans.length;
        event.sdkProcessingMetadata = __spreadProps(__spreadValues({}, event.sdkProcessingMetadata), {
          spanCountBeforeProcessing: spanCountBefore
        });
      }
      return beforeSendTransaction(event, hint);
    }
    return event;
  }
  function isErrorEvent2(event) {
    return event.type === void 0;
  }
  function isTransactionEvent(event) {
    return event.type === "transaction";
  }

  // node_modules/@sentry/core/esm/sdk.js
  function initAndBind(clientClass, options) {
    if (options.debug === true) {
      if (DEBUG_BUILD2) {
        logger.enable();
      } else {
        consoleSandbox(() => {
          console.warn("[Sentry] Cannot initialize SDK with `debug` option using a non-debug bundle.");
        });
      }
    }
    const scope = getCurrentScope();
    scope.update(options.initialScope);
    const client = new clientClass(options);
    setCurrentClient(client);
    initializeClient(client);
  }
  function setCurrentClient(client) {
    const hub = getCurrentHub();
    const top = hub.getStackTop();
    top.client = client;
    top.scope.setClient(client);
  }
  function initializeClient(client) {
    if (client.init) {
      client.init();
    } else if (client.setupIntegrations) {
      client.setupIntegrations();
    }
  }

  // node_modules/@sentry/core/esm/transports/base.js
  var DEFAULT_TRANSPORT_BUFFER_SIZE = 30;
  function createTransport(options, makeRequest, buffer = makePromiseBuffer(
    options.bufferSize || DEFAULT_TRANSPORT_BUFFER_SIZE
  )) {
    let rateLimits = {};
    const flush2 = (timeout) => buffer.drain(timeout);
    function send(envelope) {
      const filteredEnvelopeItems = [];
      forEachEnvelopeItem(envelope, (item, type) => {
        const dataCategory = envelopeItemTypeToDataCategory(type);
        if (isRateLimited(rateLimits, dataCategory)) {
          const event = getEventForEnvelopeItem(item, type);
          options.recordDroppedEvent("ratelimit_backoff", dataCategory, event);
        } else {
          filteredEnvelopeItems.push(item);
        }
      });
      if (filteredEnvelopeItems.length === 0) {
        return resolvedSyncPromise();
      }
      const filteredEnvelope = createEnvelope(envelope[0], filteredEnvelopeItems);
      const recordEnvelopeLoss = (reason) => {
        forEachEnvelopeItem(filteredEnvelope, (item, type) => {
          const event = getEventForEnvelopeItem(item, type);
          options.recordDroppedEvent(reason, envelopeItemTypeToDataCategory(type), event);
        });
      };
      const requestTask = () => makeRequest({ body: serializeEnvelope(filteredEnvelope, options.textEncoder) }).then(
        (response) => {
          if (response.statusCode !== void 0 && (response.statusCode < 200 || response.statusCode >= 300)) {
            DEBUG_BUILD2 && logger.warn(`Sentry responded with status code ${response.statusCode} to sent event.`);
          }
          rateLimits = updateRateLimits(rateLimits, response);
          return response;
        },
        (error) => {
          recordEnvelopeLoss("network_error");
          throw error;
        }
      );
      return buffer.add(requestTask).then(
        (result) => result,
        (error) => {
          if (error instanceof SentryError) {
            DEBUG_BUILD2 && logger.error("Skipped sending event because buffer is full.");
            recordEnvelopeLoss("queue_overflow");
            return resolvedSyncPromise();
          } else {
            throw error;
          }
        }
      );
    }
    send.__sentry__baseTransport__ = true;
    return {
      send,
      flush: flush2
    };
  }
  function getEventForEnvelopeItem(item, type) {
    if (type !== "event" && type !== "transaction") {
      return void 0;
    }
    return Array.isArray(item) ? item[1] : void 0;
  }

  // node_modules/@sentry/core/esm/utils/sdkMetadata.js
  function applySdkMetadata(options, name, names = [name], source = "npm") {
    const metadata = options._metadata || {};
    if (!metadata.sdk) {
      metadata.sdk = {
        name: `sentry.javascript.${name}`,
        packages: names.map((name2) => ({
          name: `${source}:@sentry/${name2}`,
          version: SDK_VERSION
        })),
        version: SDK_VERSION
      };
    }
    options._metadata = metadata;
  }

  // node_modules/@sentry/core/esm/integrations/inboundfilters.js
  var DEFAULT_IGNORE_ERRORS = [
    /^Script error\.?$/,
    /^Javascript error: Script error\.? on line 0$/,
    /^ResizeObserver loop completed with undelivered notifications.$/,
    /^Cannot redefine property: googletag$/
  ];
  var DEFAULT_IGNORE_TRANSACTIONS = [
    /^.*\/healthcheck$/,
    /^.*\/healthy$/,
    /^.*\/live$/,
    /^.*\/ready$/,
    /^.*\/heartbeat$/,
    /^.*\/health$/,
    /^.*\/healthz$/
  ];
  var INTEGRATION_NAME = "InboundFilters";
  var _inboundFiltersIntegration = (options = {}) => {
    return {
      name: INTEGRATION_NAME,
      setupOnce() {
      },
      processEvent(event, _hint, client) {
        const clientOptions = client.getOptions();
        const mergedOptions = _mergeOptions(options, clientOptions);
        return _shouldDropEvent(event, mergedOptions) ? null : event;
      }
    };
  };
  var inboundFiltersIntegration = defineIntegration(_inboundFiltersIntegration);
  var InboundFilters = convertIntegrationFnToClass(
    INTEGRATION_NAME,
    inboundFiltersIntegration
  );
  function _mergeOptions(internalOptions = {}, clientOptions = {}) {
    return {
      allowUrls: [...internalOptions.allowUrls || [], ...clientOptions.allowUrls || []],
      denyUrls: [...internalOptions.denyUrls || [], ...clientOptions.denyUrls || []],
      ignoreErrors: [
        ...internalOptions.ignoreErrors || [],
        ...clientOptions.ignoreErrors || [],
        ...internalOptions.disableErrorDefaults ? [] : DEFAULT_IGNORE_ERRORS
      ],
      ignoreTransactions: [
        ...internalOptions.ignoreTransactions || [],
        ...clientOptions.ignoreTransactions || [],
        ...internalOptions.disableTransactionDefaults ? [] : DEFAULT_IGNORE_TRANSACTIONS
      ],
      ignoreInternal: internalOptions.ignoreInternal !== void 0 ? internalOptions.ignoreInternal : true
    };
  }
  function _shouldDropEvent(event, options) {
    if (options.ignoreInternal && _isSentryError(event)) {
      DEBUG_BUILD2 && logger.warn(`Event dropped due to being internal Sentry Error.
Event: ${getEventDescription(event)}`);
      return true;
    }
    if (_isIgnoredError(event, options.ignoreErrors)) {
      DEBUG_BUILD2 && logger.warn(
        `Event dropped due to being matched by \`ignoreErrors\` option.
Event: ${getEventDescription(event)}`
      );
      return true;
    }
    if (_isIgnoredTransaction(event, options.ignoreTransactions)) {
      DEBUG_BUILD2 && logger.warn(
        `Event dropped due to being matched by \`ignoreTransactions\` option.
Event: ${getEventDescription(event)}`
      );
      return true;
    }
    if (_isDeniedUrl(event, options.denyUrls)) {
      DEBUG_BUILD2 && logger.warn(
        `Event dropped due to being matched by \`denyUrls\` option.
Event: ${getEventDescription(
          event
        )}.
Url: ${_getEventFilterUrl(event)}`
      );
      return true;
    }
    if (!_isAllowedUrl(event, options.allowUrls)) {
      DEBUG_BUILD2 && logger.warn(
        `Event dropped due to not being matched by \`allowUrls\` option.
Event: ${getEventDescription(
          event
        )}.
Url: ${_getEventFilterUrl(event)}`
      );
      return true;
    }
    return false;
  }
  function _isIgnoredError(event, ignoreErrors) {
    if (event.type || !ignoreErrors || !ignoreErrors.length) {
      return false;
    }
    return _getPossibleEventMessages(event).some((message) => stringMatchesSomePattern(message, ignoreErrors));
  }
  function _isIgnoredTransaction(event, ignoreTransactions) {
    if (event.type !== "transaction" || !ignoreTransactions || !ignoreTransactions.length) {
      return false;
    }
    const name = event.transaction;
    return name ? stringMatchesSomePattern(name, ignoreTransactions) : false;
  }
  function _isDeniedUrl(event, denyUrls) {
    if (!denyUrls || !denyUrls.length) {
      return false;
    }
    const url = _getEventFilterUrl(event);
    return !url ? false : stringMatchesSomePattern(url, denyUrls);
  }
  function _isAllowedUrl(event, allowUrls) {
    if (!allowUrls || !allowUrls.length) {
      return true;
    }
    const url = _getEventFilterUrl(event);
    return !url ? true : stringMatchesSomePattern(url, allowUrls);
  }
  function _getPossibleEventMessages(event) {
    const possibleMessages = [];
    if (event.message) {
      possibleMessages.push(event.message);
    }
    let lastException;
    try {
      lastException = event.exception.values[event.exception.values.length - 1];
    } catch (e) {
    }
    if (lastException) {
      if (lastException.value) {
        possibleMessages.push(lastException.value);
        if (lastException.type) {
          possibleMessages.push(`${lastException.type}: ${lastException.value}`);
        }
      }
    }
    if (DEBUG_BUILD2 && possibleMessages.length === 0) {
      logger.error(`Could not extract message for event ${getEventDescription(event)}`);
    }
    return possibleMessages;
  }
  function _isSentryError(event) {
    try {
      return event.exception.values[0].type === "SentryError";
    } catch (e) {
    }
    return false;
  }
  function _getLastValidUrl(frames = []) {
    for (let i = frames.length - 1; i >= 0; i--) {
      const frame = frames[i];
      if (frame && frame.filename !== "<anonymous>" && frame.filename !== "[native code]") {
        return frame.filename || null;
      }
    }
    return null;
  }
  function _getEventFilterUrl(event) {
    try {
      let frames;
      try {
        frames = event.exception.values[0].stacktrace.frames;
      } catch (e) {
      }
      return frames ? _getLastValidUrl(frames) : null;
    } catch (oO) {
      DEBUG_BUILD2 && logger.error(`Cannot extract url for event ${getEventDescription(event)}`);
      return null;
    }
  }

  // node_modules/@sentry/core/esm/integrations/functiontostring.js
  var originalFunctionToString;
  var INTEGRATION_NAME2 = "FunctionToString";
  var SETUP_CLIENTS = /* @__PURE__ */ new WeakMap();
  var _functionToStringIntegration = () => {
    return {
      name: INTEGRATION_NAME2,
      setupOnce() {
        originalFunctionToString = Function.prototype.toString;
        try {
          Function.prototype.toString = function(...args) {
            const originalFunction = getOriginalFunction(this);
            const context = SETUP_CLIENTS.has(getClient()) && originalFunction !== void 0 ? originalFunction : this;
            return originalFunctionToString.apply(context, args);
          };
        } catch (e) {
        }
      },
      setup(client) {
        SETUP_CLIENTS.set(client, true);
      }
    };
  };
  var functionToStringIntegration = defineIntegration(_functionToStringIntegration);
  var FunctionToString = convertIntegrationFnToClass(
    INTEGRATION_NAME2,
    functionToStringIntegration
  );

  // node_modules/@sentry/core/esm/integrations/linkederrors.js
  var DEFAULT_KEY = "cause";
  var DEFAULT_LIMIT = 5;
  var INTEGRATION_NAME3 = "LinkedErrors";
  var _linkedErrorsIntegration = (options = {}) => {
    const limit = options.limit || DEFAULT_LIMIT;
    const key = options.key || DEFAULT_KEY;
    return {
      name: INTEGRATION_NAME3,
      setupOnce() {
      },
      preprocessEvent(event, hint, client) {
        const options2 = client.getOptions();
        applyAggregateErrorsToEvent(
          exceptionFromError,
          options2.stackParser,
          options2.maxValueLength,
          key,
          limit,
          event,
          hint
        );
      }
    };
  };
  var linkedErrorsIntegration = defineIntegration(_linkedErrorsIntegration);
  var LinkedErrors = convertIntegrationFnToClass(INTEGRATION_NAME3, linkedErrorsIntegration);

  // node_modules/@sentry/core/esm/integrations/index.js
  var integrations_exports = {};
  __export(integrations_exports, {
    FunctionToString: () => FunctionToString,
    InboundFilters: () => InboundFilters,
    LinkedErrors: () => LinkedErrors
  });

  // node_modules/@sentry/core/esm/index.js
  var Integrations = integrations_exports;

  // node_modules/@sentry/browser/esm/helpers.js
  var WINDOW7 = GLOBAL_OBJ;
  var ignoreOnError = 0;
  function shouldIgnoreOnError() {
    return ignoreOnError > 0;
  }
  function ignoreNextOnError() {
    ignoreOnError++;
    setTimeout(() => {
      ignoreOnError--;
    });
  }
  function wrap(fn, options = {}, before) {
    if (typeof fn !== "function") {
      return fn;
    }
    try {
      const wrapper = fn.__sentry_wrapped__;
      if (wrapper) {
        if (typeof wrapper === "function") {
          return wrapper;
        } else {
          return fn;
        }
      }
      if (getOriginalFunction(fn)) {
        return fn;
      }
    } catch (e) {
      return fn;
    }
    const sentryWrapped = function() {
      const args = Array.prototype.slice.call(arguments);
      try {
        if (before && typeof before === "function") {
          before.apply(this, arguments);
        }
        const wrappedArguments = args.map((arg) => wrap(arg, options));
        return fn.apply(this, wrappedArguments);
      } catch (ex) {
        ignoreNextOnError();
        withScope((scope) => {
          scope.addEventProcessor((event) => {
            if (options.mechanism) {
              addExceptionTypeValue(event, void 0, void 0);
              addExceptionMechanism(event, options.mechanism);
            }
            event.extra = __spreadProps(__spreadValues({}, event.extra), {
              arguments: args
            });
            return event;
          });
          captureException(ex);
        });
        throw ex;
      }
    };
    try {
      for (const property in fn) {
        if (Object.prototype.hasOwnProperty.call(fn, property)) {
          sentryWrapped[property] = fn[property];
        }
      }
    } catch (_oO) {
    }
    markFunctionWrapped(sentryWrapped, fn);
    addNonEnumerableProperty(fn, "__sentry_wrapped__", sentryWrapped);
    try {
      const descriptor = Object.getOwnPropertyDescriptor(sentryWrapped, "name");
      if (descriptor.configurable) {
        Object.defineProperty(sentryWrapped, "name", {
          get() {
            return fn.name;
          }
        });
      }
    } catch (_oO) {
    }
    return sentryWrapped;
  }

  // node_modules/@sentry/browser/esm/debug-build.js
  var DEBUG_BUILD3 = typeof __SENTRY_DEBUG__ === "undefined" || __SENTRY_DEBUG__;

  // node_modules/@sentry/browser/esm/eventbuilder.js
  function exceptionFromError2(stackParser, ex) {
    const frames = parseStackFrames2(stackParser, ex);
    const exception = {
      type: ex && ex.name,
      value: extractMessage(ex)
    };
    if (frames.length) {
      exception.stacktrace = { frames };
    }
    if (exception.type === void 0 && exception.value === "") {
      exception.value = "Unrecoverable error caught";
    }
    return exception;
  }
  function eventFromPlainObject(stackParser, exception, syntheticException, isUnhandledRejection) {
    const client = getClient();
    const normalizeDepth = client && client.getOptions().normalizeDepth;
    const event = {
      exception: {
        values: [
          {
            type: isEvent(exception) ? exception.constructor.name : isUnhandledRejection ? "UnhandledRejection" : "Error",
            value: getNonErrorObjectExceptionValue(exception, { isUnhandledRejection })
          }
        ]
      },
      extra: {
        __serialized__: normalizeToSize(exception, normalizeDepth)
      }
    };
    if (syntheticException) {
      const frames = parseStackFrames2(stackParser, syntheticException);
      if (frames.length) {
        event.exception.values[0].stacktrace = { frames };
      }
    }
    return event;
  }
  function eventFromError(stackParser, ex) {
    return {
      exception: {
        values: [exceptionFromError2(stackParser, ex)]
      }
    };
  }
  function parseStackFrames2(stackParser, ex) {
    const stacktrace = ex.stacktrace || ex.stack || "";
    const popSize = getPopSize(ex);
    try {
      return stackParser(stacktrace, popSize);
    } catch (e) {
    }
    return [];
  }
  var reactMinifiedRegexp = /Minified React error #\d+;/i;
  function getPopSize(ex) {
    if (ex) {
      if (typeof ex.framesToPop === "number") {
        return ex.framesToPop;
      }
      if (reactMinifiedRegexp.test(ex.message)) {
        return 1;
      }
    }
    return 0;
  }
  function extractMessage(ex) {
    const message = ex && ex.message;
    if (!message) {
      return "No error message";
    }
    if (message.error && typeof message.error.message === "string") {
      return message.error.message;
    }
    return message;
  }
  function eventFromException(stackParser, exception, hint, attachStacktrace) {
    const syntheticException = hint && hint.syntheticException || void 0;
    const event = eventFromUnknownInput2(stackParser, exception, syntheticException, attachStacktrace);
    addExceptionMechanism(event);
    event.level = "error";
    if (hint && hint.event_id) {
      event.event_id = hint.event_id;
    }
    return resolvedSyncPromise(event);
  }
  function eventFromMessage2(stackParser, message, level = "info", hint, attachStacktrace) {
    const syntheticException = hint && hint.syntheticException || void 0;
    const event = eventFromString(stackParser, message, syntheticException, attachStacktrace);
    event.level = level;
    if (hint && hint.event_id) {
      event.event_id = hint.event_id;
    }
    return resolvedSyncPromise(event);
  }
  function eventFromUnknownInput2(stackParser, exception, syntheticException, attachStacktrace, isUnhandledRejection) {
    let event;
    if (isErrorEvent(exception) && exception.error) {
      const errorEvent = exception;
      return eventFromError(stackParser, errorEvent.error);
    }
    if (isDOMError(exception) || isDOMException(exception)) {
      const domException = exception;
      if ("stack" in exception) {
        event = eventFromError(stackParser, exception);
      } else {
        const name = domException.name || (isDOMError(domException) ? "DOMError" : "DOMException");
        const message = domException.message ? `${name}: ${domException.message}` : name;
        event = eventFromString(stackParser, message, syntheticException, attachStacktrace);
        addExceptionTypeValue(event, message);
      }
      if ("code" in domException) {
        event.tags = __spreadProps(__spreadValues({}, event.tags), { "DOMException.code": `${domException.code}` });
      }
      return event;
    }
    if (isError(exception)) {
      return eventFromError(stackParser, exception);
    }
    if (isPlainObject(exception) || isEvent(exception)) {
      const objectException = exception;
      event = eventFromPlainObject(stackParser, objectException, syntheticException, isUnhandledRejection);
      addExceptionMechanism(event, {
        synthetic: true
      });
      return event;
    }
    event = eventFromString(stackParser, exception, syntheticException, attachStacktrace);
    addExceptionTypeValue(event, `${exception}`, void 0);
    addExceptionMechanism(event, {
      synthetic: true
    });
    return event;
  }
  function eventFromString(stackParser, message, syntheticException, attachStacktrace) {
    const event = {};
    if (attachStacktrace && syntheticException) {
      const frames = parseStackFrames2(stackParser, syntheticException);
      if (frames.length) {
        event.exception = {
          values: [{ value: message, stacktrace: { frames } }]
        };
      }
    }
    if (isParameterizedString(message)) {
      const { __sentry_template_string__, __sentry_template_values__ } = message;
      event.logentry = {
        message: __sentry_template_string__,
        params: __sentry_template_values__
      };
      return event;
    }
    event.message = message;
    return event;
  }
  function getNonErrorObjectExceptionValue(exception, { isUnhandledRejection }) {
    const keys = extractExceptionKeysForMessage(exception);
    const captureType = isUnhandledRejection ? "promise rejection" : "exception";
    if (isErrorEvent(exception)) {
      return `Event \`ErrorEvent\` captured as ${captureType} with message \`${exception.message}\``;
    }
    if (isEvent(exception)) {
      const className = getObjectClassName(exception);
      return `Event \`${className}\` (type=${exception.type}) captured as ${captureType}`;
    }
    return `Object captured as ${captureType} with keys: ${keys}`;
  }
  function getObjectClassName(obj) {
    try {
      const prototype = Object.getPrototypeOf(obj);
      return prototype ? prototype.constructor.name : void 0;
    } catch (e) {
    }
  }

  // node_modules/@sentry/browser/esm/userfeedback.js
  function createUserFeedbackEnvelope(feedback, {
    metadata,
    tunnel,
    dsn
  }) {
    const headers = __spreadValues(__spreadValues({
      event_id: feedback.event_id,
      sent_at: new Date().toISOString()
    }, metadata && metadata.sdk && {
      sdk: {
        name: metadata.sdk.name,
        version: metadata.sdk.version
      }
    }), !!tunnel && !!dsn && { dsn: dsnToString(dsn) });
    const item = createUserFeedbackEnvelopeItem(feedback);
    return createEnvelope(headers, [item]);
  }
  function createUserFeedbackEnvelopeItem(feedback) {
    const feedbackHeaders = {
      type: "user_report"
    };
    return [feedbackHeaders, feedback];
  }

  // node_modules/@sentry/browser/esm/client.js
  var BrowserClient = class extends BaseClient {
    constructor(options) {
      const sdkSource = WINDOW7.SENTRY_SDK_SOURCE || getSDKSource();
      applySdkMetadata(options, "browser", ["browser"], sdkSource);
      super(options);
      if (options.sendClientReports && WINDOW7.document) {
        WINDOW7.document.addEventListener("visibilitychange", () => {
          if (WINDOW7.document.visibilityState === "hidden") {
            this._flushOutcomes();
          }
        });
      }
    }
    eventFromException(exception, hint) {
      return eventFromException(this._options.stackParser, exception, hint, this._options.attachStacktrace);
    }
    eventFromMessage(message, level = "info", hint) {
      return eventFromMessage2(this._options.stackParser, message, level, hint, this._options.attachStacktrace);
    }
    captureUserFeedback(feedback) {
      if (!this._isEnabled()) {
        DEBUG_BUILD3 && logger.warn("SDK not enabled, will not capture user feedback.");
        return;
      }
      const envelope = createUserFeedbackEnvelope(feedback, {
        metadata: this.getSdkMetadata(),
        dsn: this.getDsn(),
        tunnel: this.getOptions().tunnel
      });
      this._sendEnvelope(envelope);
    }
    _prepareEvent(event, hint, scope) {
      event.platform = event.platform || "javascript";
      return super._prepareEvent(event, hint, scope);
    }
    _flushOutcomes() {
      const outcomes = this._clearOutcomes();
      if (outcomes.length === 0) {
        DEBUG_BUILD3 && logger.log("No outcomes to send");
        return;
      }
      if (!this._dsn) {
        DEBUG_BUILD3 && logger.log("No dsn provided, will not send outcomes");
        return;
      }
      DEBUG_BUILD3 && logger.log("Sending outcomes:", outcomes);
      const envelope = createClientReportEnvelope(outcomes, this._options.tunnel && dsnToString(this._dsn));
      this._sendEnvelope(envelope);
    }
  };

  // node_modules/@sentry/browser/esm/transports/utils.js
  var cachedFetchImpl = void 0;
  function getNativeFetchImplementation() {
    if (cachedFetchImpl) {
      return cachedFetchImpl;
    }
    if (isNativeFetch(WINDOW7.fetch)) {
      return cachedFetchImpl = WINDOW7.fetch.bind(WINDOW7);
    }
    const document2 = WINDOW7.document;
    let fetchImpl = WINDOW7.fetch;
    if (document2 && typeof document2.createElement === "function") {
      try {
        const sandbox = document2.createElement("iframe");
        sandbox.hidden = true;
        document2.head.appendChild(sandbox);
        const contentWindow = sandbox.contentWindow;
        if (contentWindow && contentWindow.fetch) {
          fetchImpl = contentWindow.fetch;
        }
        document2.head.removeChild(sandbox);
      } catch (e) {
        DEBUG_BUILD3 && logger.warn("Could not create sandbox iframe for pure fetch check, bailing to window.fetch: ", e);
      }
    }
    return cachedFetchImpl = fetchImpl.bind(WINDOW7);
  }
  function clearCachedFetchImplementation() {
    cachedFetchImpl = void 0;
  }

  // node_modules/@sentry/browser/esm/transports/fetch.js
  function makeFetchTransport(options, nativeFetch = getNativeFetchImplementation()) {
    let pendingBodySize = 0;
    let pendingCount = 0;
    function makeRequest(request) {
      const requestSize = request.body.length;
      pendingBodySize += requestSize;
      pendingCount++;
      const requestOptions = __spreadValues({
        body: request.body,
        method: "POST",
        referrerPolicy: "origin",
        headers: options.headers,
        keepalive: pendingBodySize <= 6e4 && pendingCount < 15
      }, options.fetchOptions);
      try {
        return nativeFetch(options.url, requestOptions).then((response) => {
          pendingBodySize -= requestSize;
          pendingCount--;
          return {
            statusCode: response.status,
            headers: {
              "x-sentry-rate-limits": response.headers.get("X-Sentry-Rate-Limits"),
              "retry-after": response.headers.get("Retry-After")
            }
          };
        });
      } catch (e) {
        clearCachedFetchImplementation();
        pendingBodySize -= requestSize;
        pendingCount--;
        return rejectedSyncPromise(e);
      }
    }
    return createTransport(options, makeRequest);
  }

  // node_modules/@sentry/browser/esm/transports/xhr.js
  var XHR_READYSTATE_DONE = 4;
  function makeXHRTransport(options) {
    function makeRequest(request) {
      return new SyncPromise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.onerror = reject;
        xhr.onreadystatechange = () => {
          if (xhr.readyState === XHR_READYSTATE_DONE) {
            resolve({
              statusCode: xhr.status,
              headers: {
                "x-sentry-rate-limits": xhr.getResponseHeader("X-Sentry-Rate-Limits"),
                "retry-after": xhr.getResponseHeader("Retry-After")
              }
            });
          }
        };
        xhr.open("POST", options.url);
        for (const header in options.headers) {
          if (Object.prototype.hasOwnProperty.call(options.headers, header)) {
            xhr.setRequestHeader(header, options.headers[header]);
          }
        }
        xhr.send(request.body);
      });
    }
    return createTransport(options, makeRequest);
  }

  // node_modules/@sentry/browser/esm/stack-parsers.js
  var UNKNOWN_FUNCTION = "?";
  var CHROME_PRIORITY = 30;
  var WINJS_PRIORITY = 40;
  var GECKO_PRIORITY = 50;
  function createFrame(filename, func, lineno, colno) {
    const frame = {
      filename,
      function: func,
      in_app: true
    };
    if (lineno !== void 0) {
      frame.lineno = lineno;
    }
    if (colno !== void 0) {
      frame.colno = colno;
    }
    return frame;
  }
  var chromeRegex = /^\s*at (?:(.+?\)(?: \[.+\])?|.*?) ?\((?:address at )?)?(?:async )?((?:<anonymous>|[-a-z]+:|.*bundle|\/)?.*?)(?::(\d+))?(?::(\d+))?\)?\s*$/i;
  var chromeEvalRegex = /\((\S*)(?::(\d+))(?::(\d+))\)/;
  var chromeStackParserFn = (line) => {
    const parts = chromeRegex.exec(line);
    if (parts) {
      const isEval = parts[2] && parts[2].indexOf("eval") === 0;
      if (isEval) {
        const subMatch = chromeEvalRegex.exec(parts[2]);
        if (subMatch) {
          parts[2] = subMatch[1];
          parts[3] = subMatch[2];
          parts[4] = subMatch[3];
        }
      }
      const [func, filename] = extractSafariExtensionDetails(parts[1] || UNKNOWN_FUNCTION, parts[2]);
      return createFrame(filename, func, parts[3] ? +parts[3] : void 0, parts[4] ? +parts[4] : void 0);
    }
    return;
  };
  var chromeStackLineParser = [CHROME_PRIORITY, chromeStackParserFn];
  var geckoREgex = /^\s*(.*?)(?:\((.*?)\))?(?:^|@)?((?:[-a-z]+)?:\/.*?|\[native code\]|[^@]*(?:bundle|\d+\.js)|\/[\w\-. /=]+)(?::(\d+))?(?::(\d+))?\s*$/i;
  var geckoEvalRegex = /(\S+) line (\d+)(?: > eval line \d+)* > eval/i;
  var gecko = (line) => {
    const parts = geckoREgex.exec(line);
    if (parts) {
      const isEval = parts[3] && parts[3].indexOf(" > eval") > -1;
      if (isEval) {
        const subMatch = geckoEvalRegex.exec(parts[3]);
        if (subMatch) {
          parts[1] = parts[1] || "eval";
          parts[3] = subMatch[1];
          parts[4] = subMatch[2];
          parts[5] = "";
        }
      }
      let filename = parts[3];
      let func = parts[1] || UNKNOWN_FUNCTION;
      [func, filename] = extractSafariExtensionDetails(func, filename);
      return createFrame(filename, func, parts[4] ? +parts[4] : void 0, parts[5] ? +parts[5] : void 0);
    }
    return;
  };
  var geckoStackLineParser = [GECKO_PRIORITY, gecko];
  var winjsRegex = /^\s*at (?:((?:\[object object\])?.+) )?\(?((?:[-a-z]+):.*?):(\d+)(?::(\d+))?\)?\s*$/i;
  var winjs = (line) => {
    const parts = winjsRegex.exec(line);
    return parts ? createFrame(parts[2], parts[1] || UNKNOWN_FUNCTION, +parts[3], parts[4] ? +parts[4] : void 0) : void 0;
  };
  var winjsStackLineParser = [WINJS_PRIORITY, winjs];
  var defaultStackLineParsers = [chromeStackLineParser, geckoStackLineParser, winjsStackLineParser];
  var defaultStackParser = createStackParser(...defaultStackLineParsers);
  var extractSafariExtensionDetails = (func, filename) => {
    const isSafariExtension = func.indexOf("safari-extension") !== -1;
    const isSafariWebExtension = func.indexOf("safari-web-extension") !== -1;
    return isSafariExtension || isSafariWebExtension ? [
      func.indexOf("@") !== -1 ? func.split("@")[0] : UNKNOWN_FUNCTION,
      isSafariExtension ? `safari-extension:${filename}` : `safari-web-extension:${filename}`
    ] : [func, filename];
  };

  // node_modules/@sentry/browser/esm/integrations/breadcrumbs.js
  var MAX_ALLOWED_STRING_LENGTH = 1024;
  var INTEGRATION_NAME4 = "Breadcrumbs";
  var _breadcrumbsIntegration = (options = {}) => {
    const _options = __spreadValues({
      console: true,
      dom: true,
      fetch: true,
      history: true,
      sentry: true,
      xhr: true
    }, options);
    return {
      name: INTEGRATION_NAME4,
      setupOnce() {
      },
      setup(client) {
        if (_options.console) {
          addConsoleInstrumentationHandler(_getConsoleBreadcrumbHandler(client));
        }
        if (_options.dom) {
          addClickKeypressInstrumentationHandler(_getDomBreadcrumbHandler(client, _options.dom));
        }
        if (_options.xhr) {
          addXhrInstrumentationHandler(_getXhrBreadcrumbHandler(client));
        }
        if (_options.fetch) {
          addFetchInstrumentationHandler(_getFetchBreadcrumbHandler(client));
        }
        if (_options.history) {
          addHistoryInstrumentationHandler(_getHistoryBreadcrumbHandler(client));
        }
        if (_options.sentry && client.on) {
          client.on("beforeSendEvent", _getSentryBreadcrumbHandler(client));
        }
      }
    };
  };
  var breadcrumbsIntegration = defineIntegration(_breadcrumbsIntegration);
  var Breadcrumbs = convertIntegrationFnToClass(INTEGRATION_NAME4, breadcrumbsIntegration);
  function _getSentryBreadcrumbHandler(client) {
    return function addSentryBreadcrumb(event) {
      if (getClient() !== client) {
        return;
      }
      addBreadcrumb(
        {
          category: `sentry.${event.type === "transaction" ? "transaction" : "event"}`,
          event_id: event.event_id,
          level: event.level,
          message: getEventDescription(event)
        },
        {
          event
        }
      );
    };
  }
  function _getDomBreadcrumbHandler(client, dom) {
    return function _innerDomBreadcrumb(handlerData) {
      if (getClient() !== client) {
        return;
      }
      let target;
      let componentName;
      let keyAttrs = typeof dom === "object" ? dom.serializeAttribute : void 0;
      let maxStringLength = typeof dom === "object" && typeof dom.maxStringLength === "number" ? dom.maxStringLength : void 0;
      if (maxStringLength && maxStringLength > MAX_ALLOWED_STRING_LENGTH) {
        DEBUG_BUILD3 && logger.warn(
          `\`dom.maxStringLength\` cannot exceed ${MAX_ALLOWED_STRING_LENGTH}, but a value of ${maxStringLength} was configured. Sentry will use ${MAX_ALLOWED_STRING_LENGTH} instead.`
        );
        maxStringLength = MAX_ALLOWED_STRING_LENGTH;
      }
      if (typeof keyAttrs === "string") {
        keyAttrs = [keyAttrs];
      }
      try {
        const event = handlerData.event;
        const element = _isEvent(event) ? event.target : event;
        target = htmlTreeAsString(element, { keyAttrs, maxStringLength });
        componentName = getComponentName(element);
      } catch (e) {
        target = "<unknown>";
      }
      if (target.length === 0) {
        return;
      }
      const breadcrumb = {
        category: `ui.${handlerData.name}`,
        message: target
      };
      if (componentName) {
        breadcrumb.data = { "ui.component_name": componentName };
      }
      addBreadcrumb(breadcrumb, {
        event: handlerData.event,
        name: handlerData.name,
        global: handlerData.global
      });
    };
  }
  function _getConsoleBreadcrumbHandler(client) {
    return function _consoleBreadcrumb(handlerData) {
      if (getClient() !== client) {
        return;
      }
      const breadcrumb = {
        category: "console",
        data: {
          arguments: handlerData.args,
          logger: "console"
        },
        level: severityLevelFromString(handlerData.level),
        message: safeJoin(handlerData.args, " ")
      };
      if (handlerData.level === "assert") {
        if (handlerData.args[0] === false) {
          breadcrumb.message = `Assertion failed: ${safeJoin(handlerData.args.slice(1), " ") || "console.assert"}`;
          breadcrumb.data.arguments = handlerData.args.slice(1);
        } else {
          return;
        }
      }
      addBreadcrumb(breadcrumb, {
        input: handlerData.args,
        level: handlerData.level
      });
    };
  }
  function _getXhrBreadcrumbHandler(client) {
    return function _xhrBreadcrumb(handlerData) {
      if (getClient() !== client) {
        return;
      }
      const { startTimestamp, endTimestamp } = handlerData;
      const sentryXhrData = handlerData.xhr[SENTRY_XHR_DATA_KEY];
      if (!startTimestamp || !endTimestamp || !sentryXhrData) {
        return;
      }
      const { method, url, status_code, body } = sentryXhrData;
      const data = {
        method,
        url,
        status_code
      };
      const hint = {
        xhr: handlerData.xhr,
        input: body,
        startTimestamp,
        endTimestamp
      };
      addBreadcrumb(
        {
          category: "xhr",
          data,
          type: "http"
        },
        hint
      );
    };
  }
  function _getFetchBreadcrumbHandler(client) {
    return function _fetchBreadcrumb(handlerData) {
      if (getClient() !== client) {
        return;
      }
      const { startTimestamp, endTimestamp } = handlerData;
      if (!endTimestamp) {
        return;
      }
      if (handlerData.fetchData.url.match(/sentry_key/) && handlerData.fetchData.method === "POST") {
        return;
      }
      if (handlerData.error) {
        const data = handlerData.fetchData;
        const hint = {
          data: handlerData.error,
          input: handlerData.args,
          startTimestamp,
          endTimestamp
        };
        addBreadcrumb(
          {
            category: "fetch",
            data,
            level: "error",
            type: "http"
          },
          hint
        );
      } else {
        const response = handlerData.response;
        const data = __spreadProps(__spreadValues({}, handlerData.fetchData), {
          status_code: response && response.status
        });
        const hint = {
          input: handlerData.args,
          response,
          startTimestamp,
          endTimestamp
        };
        addBreadcrumb(
          {
            category: "fetch",
            data,
            type: "http"
          },
          hint
        );
      }
    };
  }
  function _getHistoryBreadcrumbHandler(client) {
    return function _historyBreadcrumb(handlerData) {
      if (getClient() !== client) {
        return;
      }
      let from = handlerData.from;
      let to = handlerData.to;
      const parsedLoc = parseUrl2(WINDOW7.location.href);
      let parsedFrom = from ? parseUrl2(from) : void 0;
      const parsedTo = parseUrl2(to);
      if (!parsedFrom || !parsedFrom.path) {
        parsedFrom = parsedLoc;
      }
      if (parsedLoc.protocol === parsedTo.protocol && parsedLoc.host === parsedTo.host) {
        to = parsedTo.relative;
      }
      if (parsedLoc.protocol === parsedFrom.protocol && parsedLoc.host === parsedFrom.host) {
        from = parsedFrom.relative;
      }
      addBreadcrumb({
        category: "navigation",
        data: {
          from,
          to
        }
      });
    };
  }
  function _isEvent(event) {
    return !!event && !!event.target;
  }

  // node_modules/@sentry/browser/esm/integrations/dedupe.js
  var INTEGRATION_NAME5 = "Dedupe";
  var _dedupeIntegration = () => {
    let previousEvent;
    return {
      name: INTEGRATION_NAME5,
      setupOnce() {
      },
      processEvent(currentEvent) {
        if (currentEvent.type) {
          return currentEvent;
        }
        try {
          if (_shouldDropEvent2(currentEvent, previousEvent)) {
            DEBUG_BUILD3 && logger.warn("Event dropped due to being a duplicate of previously captured event.");
            return null;
          }
        } catch (_oO) {
        }
        return previousEvent = currentEvent;
      }
    };
  };
  var dedupeIntegration = defineIntegration(_dedupeIntegration);
  var Dedupe = convertIntegrationFnToClass(INTEGRATION_NAME5, dedupeIntegration);
  function _shouldDropEvent2(currentEvent, previousEvent) {
    if (!previousEvent) {
      return false;
    }
    if (_isSameMessageEvent(currentEvent, previousEvent)) {
      return true;
    }
    if (_isSameExceptionEvent(currentEvent, previousEvent)) {
      return true;
    }
    return false;
  }
  function _isSameMessageEvent(currentEvent, previousEvent) {
    const currentMessage = currentEvent.message;
    const previousMessage = previousEvent.message;
    if (!currentMessage && !previousMessage) {
      return false;
    }
    if (currentMessage && !previousMessage || !currentMessage && previousMessage) {
      return false;
    }
    if (currentMessage !== previousMessage) {
      return false;
    }
    if (!_isSameFingerprint(currentEvent, previousEvent)) {
      return false;
    }
    if (!_isSameStacktrace(currentEvent, previousEvent)) {
      return false;
    }
    return true;
  }
  function _isSameExceptionEvent(currentEvent, previousEvent) {
    const previousException = _getExceptionFromEvent(previousEvent);
    const currentException = _getExceptionFromEvent(currentEvent);
    if (!previousException || !currentException) {
      return false;
    }
    if (previousException.type !== currentException.type || previousException.value !== currentException.value) {
      return false;
    }
    if (!_isSameFingerprint(currentEvent, previousEvent)) {
      return false;
    }
    if (!_isSameStacktrace(currentEvent, previousEvent)) {
      return false;
    }
    return true;
  }
  function _isSameStacktrace(currentEvent, previousEvent) {
    let currentFrames = _getFramesFromEvent(currentEvent);
    let previousFrames = _getFramesFromEvent(previousEvent);
    if (!currentFrames && !previousFrames) {
      return true;
    }
    if (currentFrames && !previousFrames || !currentFrames && previousFrames) {
      return false;
    }
    currentFrames = currentFrames;
    previousFrames = previousFrames;
    if (previousFrames.length !== currentFrames.length) {
      return false;
    }
    for (let i = 0; i < previousFrames.length; i++) {
      const frameA = previousFrames[i];
      const frameB = currentFrames[i];
      if (frameA.filename !== frameB.filename || frameA.lineno !== frameB.lineno || frameA.colno !== frameB.colno || frameA.function !== frameB.function) {
        return false;
      }
    }
    return true;
  }
  function _isSameFingerprint(currentEvent, previousEvent) {
    let currentFingerprint = currentEvent.fingerprint;
    let previousFingerprint = previousEvent.fingerprint;
    if (!currentFingerprint && !previousFingerprint) {
      return true;
    }
    if (currentFingerprint && !previousFingerprint || !currentFingerprint && previousFingerprint) {
      return false;
    }
    currentFingerprint = currentFingerprint;
    previousFingerprint = previousFingerprint;
    try {
      return !!(currentFingerprint.join("") === previousFingerprint.join(""));
    } catch (_oO) {
      return false;
    }
  }
  function _getExceptionFromEvent(event) {
    return event.exception && event.exception.values && event.exception.values[0];
  }
  function _getFramesFromEvent(event) {
    const exception = event.exception;
    if (exception) {
      try {
        return exception.values[0].stacktrace.frames;
      } catch (_oO) {
        return void 0;
      }
    }
    return void 0;
  }

  // node_modules/@sentry/browser/esm/integrations/globalhandlers.js
  var INTEGRATION_NAME6 = "GlobalHandlers";
  var _globalHandlersIntegration = (options = {}) => {
    const _options = __spreadValues({
      onerror: true,
      onunhandledrejection: true
    }, options);
    return {
      name: INTEGRATION_NAME6,
      setupOnce() {
        Error.stackTraceLimit = 50;
      },
      setup(client) {
        if (_options.onerror) {
          _installGlobalOnErrorHandler(client);
          globalHandlerLog("onerror");
        }
        if (_options.onunhandledrejection) {
          _installGlobalOnUnhandledRejectionHandler(client);
          globalHandlerLog("onunhandledrejection");
        }
      }
    };
  };
  var globalHandlersIntegration = defineIntegration(_globalHandlersIntegration);
  var GlobalHandlers = convertIntegrationFnToClass(
    INTEGRATION_NAME6,
    globalHandlersIntegration
  );
  function _installGlobalOnErrorHandler(client) {
    addGlobalErrorInstrumentationHandler((data) => {
      const { stackParser, attachStacktrace } = getOptions();
      if (getClient() !== client || shouldIgnoreOnError()) {
        return;
      }
      const { msg, url, line, column, error } = data;
      const event = error === void 0 && isString(msg) ? _eventFromIncompleteOnError(msg, url, line, column) : _enhanceEventWithInitialFrame(
        eventFromUnknownInput2(stackParser, error || msg, void 0, attachStacktrace, false),
        url,
        line,
        column
      );
      event.level = "error";
      captureEvent(event, {
        originalException: error,
        mechanism: {
          handled: false,
          type: "onerror"
        }
      });
    });
  }
  function _installGlobalOnUnhandledRejectionHandler(client) {
    addGlobalUnhandledRejectionInstrumentationHandler((e) => {
      const { stackParser, attachStacktrace } = getOptions();
      if (getClient() !== client || shouldIgnoreOnError()) {
        return;
      }
      const error = _getUnhandledRejectionError(e);
      const event = isPrimitive(error) ? _eventFromRejectionWithPrimitive(error) : eventFromUnknownInput2(stackParser, error, void 0, attachStacktrace, true);
      event.level = "error";
      captureEvent(event, {
        originalException: error,
        mechanism: {
          handled: false,
          type: "onunhandledrejection"
        }
      });
    });
  }
  function _getUnhandledRejectionError(error) {
    if (isPrimitive(error)) {
      return error;
    }
    const e = error;
    try {
      if ("reason" in e) {
        return e.reason;
      } else if ("detail" in e && "reason" in e.detail) {
        return e.detail.reason;
      }
    } catch (e2) {
    }
    return error;
  }
  function _eventFromRejectionWithPrimitive(reason) {
    return {
      exception: {
        values: [
          {
            type: "UnhandledRejection",
            value: `Non-Error promise rejection captured with value: ${String(reason)}`
          }
        ]
      }
    };
  }
  function _eventFromIncompleteOnError(msg, url, line, column) {
    const ERROR_TYPES_RE = /^(?:[Uu]ncaught (?:exception: )?)?(?:((?:Eval|Internal|Range|Reference|Syntax|Type|URI|)Error): )?(.*)$/i;
    let message = isErrorEvent(msg) ? msg.message : msg;
    let name = "Error";
    const groups = message.match(ERROR_TYPES_RE);
    if (groups) {
      name = groups[1];
      message = groups[2];
    }
    const event = {
      exception: {
        values: [
          {
            type: name,
            value: message
          }
        ]
      }
    };
    return _enhanceEventWithInitialFrame(event, url, line, column);
  }
  function _enhanceEventWithInitialFrame(event, url, line, column) {
    const e = event.exception = event.exception || {};
    const ev = e.values = e.values || [];
    const ev0 = ev[0] = ev[0] || {};
    const ev0s = ev0.stacktrace = ev0.stacktrace || {};
    const ev0sf = ev0s.frames = ev0s.frames || [];
    const colno = isNaN(parseInt(column, 10)) ? void 0 : column;
    const lineno = isNaN(parseInt(line, 10)) ? void 0 : line;
    const filename = isString(url) && url.length > 0 ? url : getLocationHref();
    if (ev0sf.length === 0) {
      ev0sf.push({
        colno,
        filename,
        function: "?",
        in_app: true,
        lineno
      });
    }
    return event;
  }
  function globalHandlerLog(type) {
    DEBUG_BUILD3 && logger.log(`Global Handler attached: ${type}`);
  }
  function getOptions() {
    const client = getClient();
    const options = client && client.getOptions() || {
      stackParser: () => [],
      attachStacktrace: false
    };
    return options;
  }

  // node_modules/@sentry/browser/esm/integrations/httpcontext.js
  var INTEGRATION_NAME7 = "HttpContext";
  var _httpContextIntegration = () => {
    return {
      name: INTEGRATION_NAME7,
      setupOnce() {
      },
      preprocessEvent(event) {
        if (!WINDOW7.navigator && !WINDOW7.location && !WINDOW7.document) {
          return;
        }
        const url = event.request && event.request.url || WINDOW7.location && WINDOW7.location.href;
        const { referrer } = WINDOW7.document || {};
        const { userAgent } = WINDOW7.navigator || {};
        const headers = __spreadValues(__spreadValues(__spreadValues({}, event.request && event.request.headers), referrer && { Referer: referrer }), userAgent && { "User-Agent": userAgent });
        const request = __spreadProps(__spreadValues(__spreadValues({}, event.request), url && { url }), { headers });
        event.request = request;
      }
    };
  };
  var httpContextIntegration = defineIntegration(_httpContextIntegration);
  var HttpContext = convertIntegrationFnToClass(INTEGRATION_NAME7, httpContextIntegration);

  // node_modules/@sentry/browser/esm/integrations/linkederrors.js
  var DEFAULT_KEY2 = "cause";
  var DEFAULT_LIMIT2 = 5;
  var INTEGRATION_NAME8 = "LinkedErrors";
  var _linkedErrorsIntegration2 = (options = {}) => {
    const limit = options.limit || DEFAULT_LIMIT2;
    const key = options.key || DEFAULT_KEY2;
    return {
      name: INTEGRATION_NAME8,
      setupOnce() {
      },
      preprocessEvent(event, hint, client) {
        const options2 = client.getOptions();
        applyAggregateErrorsToEvent(
          exceptionFromError2,
          options2.stackParser,
          options2.maxValueLength,
          key,
          limit,
          event,
          hint
        );
      }
    };
  };
  var linkedErrorsIntegration2 = defineIntegration(_linkedErrorsIntegration2);
  var LinkedErrors2 = convertIntegrationFnToClass(INTEGRATION_NAME8, linkedErrorsIntegration2);

  // node_modules/@sentry/browser/esm/integrations/trycatch.js
  var DEFAULT_EVENT_TARGET = [
    "EventTarget",
    "Window",
    "Node",
    "ApplicationCache",
    "AudioTrackList",
    "BroadcastChannel",
    "ChannelMergerNode",
    "CryptoOperation",
    "EventSource",
    "FileReader",
    "HTMLUnknownElement",
    "IDBDatabase",
    "IDBRequest",
    "IDBTransaction",
    "KeyOperation",
    "MediaController",
    "MessagePort",
    "ModalWindow",
    "Notification",
    "SVGElementInstance",
    "Screen",
    "SharedWorker",
    "TextTrack",
    "TextTrackCue",
    "TextTrackList",
    "WebSocket",
    "WebSocketWorker",
    "Worker",
    "XMLHttpRequest",
    "XMLHttpRequestEventTarget",
    "XMLHttpRequestUpload"
  ];
  var INTEGRATION_NAME9 = "TryCatch";
  var _browserApiErrorsIntegration = (options = {}) => {
    const _options = __spreadValues({
      XMLHttpRequest: true,
      eventTarget: true,
      requestAnimationFrame: true,
      setInterval: true,
      setTimeout: true
    }, options);
    return {
      name: INTEGRATION_NAME9,
      setupOnce() {
        if (_options.setTimeout) {
          fill(WINDOW7, "setTimeout", _wrapTimeFunction);
        }
        if (_options.setInterval) {
          fill(WINDOW7, "setInterval", _wrapTimeFunction);
        }
        if (_options.requestAnimationFrame) {
          fill(WINDOW7, "requestAnimationFrame", _wrapRAF);
        }
        if (_options.XMLHttpRequest && "XMLHttpRequest" in WINDOW7) {
          fill(XMLHttpRequest.prototype, "send", _wrapXHR);
        }
        const eventTargetOption = _options.eventTarget;
        if (eventTargetOption) {
          const eventTarget = Array.isArray(eventTargetOption) ? eventTargetOption : DEFAULT_EVENT_TARGET;
          eventTarget.forEach(_wrapEventTarget);
        }
      }
    };
  };
  var browserApiErrorsIntegration = defineIntegration(_browserApiErrorsIntegration);
  var TryCatch = convertIntegrationFnToClass(
    INTEGRATION_NAME9,
    browserApiErrorsIntegration
  );
  function _wrapTimeFunction(original) {
    return function(...args) {
      const originalCallback = args[0];
      args[0] = wrap(originalCallback, {
        mechanism: {
          data: { function: getFunctionName(original) },
          handled: false,
          type: "instrument"
        }
      });
      return original.apply(this, args);
    };
  }
  function _wrapRAF(original) {
    return function(callback) {
      return original.apply(this, [
        wrap(callback, {
          mechanism: {
            data: {
              function: "requestAnimationFrame",
              handler: getFunctionName(original)
            },
            handled: false,
            type: "instrument"
          }
        })
      ]);
    };
  }
  function _wrapXHR(originalSend) {
    return function(...args) {
      const xhr = this;
      const xmlHttpRequestProps = ["onload", "onerror", "onprogress", "onreadystatechange"];
      xmlHttpRequestProps.forEach((prop) => {
        if (prop in xhr && typeof xhr[prop] === "function") {
          fill(xhr, prop, function(original) {
            const wrapOptions = {
              mechanism: {
                data: {
                  function: prop,
                  handler: getFunctionName(original)
                },
                handled: false,
                type: "instrument"
              }
            };
            const originalFunction = getOriginalFunction(original);
            if (originalFunction) {
              wrapOptions.mechanism.data.handler = getFunctionName(originalFunction);
            }
            return wrap(original, wrapOptions);
          });
        }
      });
      return originalSend.apply(this, args);
    };
  }
  function _wrapEventTarget(target) {
    const globalObject = WINDOW7;
    const proto = globalObject[target] && globalObject[target].prototype;
    if (!proto || !proto.hasOwnProperty || !proto.hasOwnProperty("addEventListener")) {
      return;
    }
    fill(proto, "addEventListener", function(original) {
      return function(eventName, fn, options) {
        try {
          if (typeof fn.handleEvent === "function") {
            fn.handleEvent = wrap(fn.handleEvent, {
              mechanism: {
                data: {
                  function: "handleEvent",
                  handler: getFunctionName(fn),
                  target
                },
                handled: false,
                type: "instrument"
              }
            });
          }
        } catch (err) {
        }
        return original.apply(this, [
          eventName,
          wrap(fn, {
            mechanism: {
              data: {
                function: "addEventListener",
                handler: getFunctionName(fn),
                target
              },
              handled: false,
              type: "instrument"
            }
          }),
          options
        ]);
      };
    });
    fill(
      proto,
      "removeEventListener",
      function(originalRemoveEventListener) {
        return function(eventName, fn, options) {
          const wrappedEventHandler = fn;
          try {
            const originalEventHandler = wrappedEventHandler && wrappedEventHandler.__sentry_wrapped__;
            if (originalEventHandler) {
              originalRemoveEventListener.call(this, eventName, originalEventHandler, options);
            }
          } catch (e) {
          }
          return originalRemoveEventListener.call(this, eventName, wrappedEventHandler, options);
        };
      }
    );
  }

  // node_modules/@sentry/browser/esm/sdk.js
  var defaultIntegrations = [
    inboundFiltersIntegration(),
    functionToStringIntegration(),
    browserApiErrorsIntegration(),
    breadcrumbsIntegration(),
    globalHandlersIntegration(),
    linkedErrorsIntegration2(),
    dedupeIntegration(),
    httpContextIntegration()
  ];
  function getDefaultIntegrations(_options) {
    return [
      ...defaultIntegrations
    ];
  }
  function init(options = {}) {
    if (options.defaultIntegrations === void 0) {
      options.defaultIntegrations = getDefaultIntegrations();
    }
    if (options.release === void 0) {
      if (typeof __SENTRY_RELEASE__ === "string") {
        options.release = __SENTRY_RELEASE__;
      }
      if (WINDOW7.SENTRY_RELEASE && WINDOW7.SENTRY_RELEASE.id) {
        options.release = WINDOW7.SENTRY_RELEASE.id;
      }
    }
    if (options.autoSessionTracking === void 0) {
      options.autoSessionTracking = true;
    }
    if (options.sendClientReports === void 0) {
      options.sendClientReports = true;
    }
    const clientOptions = __spreadProps(__spreadValues({}, options), {
      stackParser: stackParserFromStackParserOptions(options.stackParser || defaultStackParser),
      integrations: getIntegrationsToSetup(options),
      transport: options.transport || (supportsFetch() ? makeFetchTransport : makeXHRTransport)
    });
    initAndBind(BrowserClient, clientOptions);
    if (options.autoSessionTracking) {
      startSessionTracking();
    }
  }
  function startSessionTracking() {
    if (typeof WINDOW7.document === "undefined") {
      DEBUG_BUILD3 && logger.warn("Session tracking in non-browser environment with @sentry/browser is not supported.");
      return;
    }
    startSession({ ignoreDuration: true });
    captureSession();
    addHistoryInstrumentationHandler(({ from, to }) => {
      if (from !== void 0 && from !== to) {
        startSession({ ignoreDuration: true });
        captureSession();
      }
    });
  }

  // node_modules/@sentry/browser/esm/integrations/index.js
  var integrations_exports2 = {};
  __export(integrations_exports2, {
    Breadcrumbs: () => Breadcrumbs,
    Dedupe: () => Dedupe,
    GlobalHandlers: () => GlobalHandlers,
    HttpContext: () => HttpContext,
    LinkedErrors: () => LinkedErrors2,
    TryCatch: () => TryCatch
  });

  // node_modules/@sentry/browser/esm/index.js
  var windowIntegrations = {};
  if (WINDOW7.Sentry && WINDOW7.Sentry.Integrations) {
    windowIntegrations = WINDOW7.Sentry.Integrations;
  }
  var INTEGRATIONS = __spreadValues(__spreadValues(__spreadValues({}, windowIntegrations), Integrations), integrations_exports2);

  // frappe/public/js/sentry.bundle.js
  var _a, _b, _c;
  init({
    dsn: frappe.boot.sentry_dsn,
    release: (_b = (_a = frappe == null ? void 0 : frappe.boot) == null ? void 0 : _a.versions) == null ? void 0 : _b.frappe,
    autoSessionTracking: false,
    initialScope: {
      user: { id: frappe.boot.sitename },
      tags: { frappe_user: (_c = frappe.boot.user.name) != null ? _c : "Unidentified" }
    },
    beforeSend(event, hint) {
      if (hint.originalException instanceof Error && hint.originalException.stack && hint.originalException.stack.includes("frappe.throw")) {
        return null;
      }
      return event;
    }
  });
})();
//# sourceMappingURL=sentry.bundle.SI3DB3BY.js.map
