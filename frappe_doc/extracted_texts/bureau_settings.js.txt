// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bureau Settings', {
	refresh: function(frm) {
		frm.set_value('bureau_admin', frappe.session.user);
	}
});
