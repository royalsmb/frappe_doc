(() => {
  // ../erpnext/erpnext/public/js/website_utils.js
  if (!window.erpnext)
    window.erpnext = {};
  erpnext.subscribe_to_newsletter = function(opts, btn) {
    return frappe.call({
      type: "POST",
      method: "frappe.email.doctype.newsletter.newsletter.subscribe",
      btn,
      args: { email: opts.email },
      callback: opts.callback
    });
  };
})();
//# sourceMappingURL=erpnext-web.bundle.253I7LT4.js.map
