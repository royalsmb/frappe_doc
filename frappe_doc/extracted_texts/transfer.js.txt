// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transfer', {
	refresh: function(frm) {
		frm.set_value('agent_name', frappe.session.user);
	}
});
