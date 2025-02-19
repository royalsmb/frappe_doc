(() => {
  // frappe/public/js/lib/posthog.js
  !function(t, e) {
    var o, n, p, r;
    e.__SV || (window.posthog = e, e._i = [], e.init = function(i, s, a) {
      function g(t2, e2) {
        var o2 = e2.split(".");
        2 == o2.length && (t2 = t2[o2[0]], e2 = o2[1]), t2[e2] = function() {
          t2.push([e2].concat(Array.prototype.slice.call(arguments, 0)));
        };
      }
      (p = t.createElement("script")).type = "text/javascript", p.async = true, p.src = s.api_host + "/static/array.js", (r = t.getElementsByTagName("script")[0]).parentNode.insertBefore(p, r);
      var u = e;
      for (void 0 !== a ? u = e[a] = [] : a = "posthog", u.people = u.people || [], u.toString = function(t2) {
        var e2 = "posthog";
        return "posthog" !== a && (e2 += "." + a), t2 || (e2 += " (stub)"), e2;
      }, u.people.toString = function() {
        return u.toString(1) + ".people (stub)";
      }, o = "capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags".split(" "), n = 0; n < o.length; n++)
        g(u, o[n]);
      e._i.push([i, s, a]);
    }, e.__SV = 1);
  }(document, window.posthog || []);

  // frappe/public/js/telemetry/index.js
  var TelemetryManager = class {
    constructor() {
      this.enabled = false;
      this.project_id = frappe.boot.posthog_project_id;
      this.telemetry_host = frappe.boot.posthog_host;
      this.site_age = frappe.boot.telemetry_site_age;
      if (cint(frappe.boot.enable_telemetry) && this.project_id && this.telemetry_host) {
        this.enabled = true;
      }
    }
    initialize() {
      if (!this.enabled)
        return;
      let disable_decide = !this.should_record_session();
      try {
        posthog.init(this.project_id, {
          api_host: this.telemetry_host,
          autocapture: false,
          capture_pageview: false,
          capture_pageleave: false,
          advanced_disable_decide: disable_decide
        });
        posthog.identify(frappe.boot.sitename);
        this.send_heartbeat();
        this.register_pageview_handler();
      } catch (e) {
        console.trace("Failed to initialize telemetry", e);
        this.enabled = false;
      }
    }
    capture(event, app, props) {
      if (!this.enabled)
        return;
      posthog.capture(`${app}_${event}`, props);
    }
    disable() {
      this.enabled = false;
    }
    can_enable() {
      if (cint(navigator.doNotTrack)) {
        return false;
      }
      let posthog_available = Boolean(this.telemetry_host && this.project_id);
      let sentry_available = Boolean(frappe.boot.sentry_dsn);
      return posthog_available || sentry_available;
    }
    send_heartbeat() {
      var _a, _b;
      const KEY = "ph_last_heartbeat";
      const now = frappe.datetime.system_datetime(true);
      const last = localStorage.getItem(KEY);
      if (!last || moment(now).diff(moment(last), "hours") > 12) {
        localStorage.setItem(KEY, now.toISOString());
        this.capture("heartbeat", "frappe", { frappe_version: (_b = (_a = frappe.boot) == null ? void 0 : _a.versions) == null ? void 0 : _b.frappe });
      }
    }
    register_pageview_handler() {
      if (this.site_age && this.site_age > 6) {
        return;
      }
      frappe.router.on("change", () => {
        posthog.capture("$pageview");
      });
    }
    should_record_session() {
      let start = frappe.boot.sysdefaults.session_recording_start;
      if (!start)
        return;
      let start_datetime = frappe.datetime.str_to_obj(start);
      let now = frappe.datetime.now_datetime();
      return frappe.datetime.get_minute_diff(now, start_datetime) < 120;
    }
  };
  frappe.telemetry = new TelemetryManager();
  frappe.telemetry.initialize();
})();
//# sourceMappingURL=telemetry.bundle.ZJBT5ETW.js.map
