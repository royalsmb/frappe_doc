// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Account Vault', {
	refresh: function(frm) {
		// check if user is a bureau admin or an agent then display only the accounts link to that bureau
		if (frappe.user.has_role("Bureau Admin") || frappe.user.has_role("Agent")){

			frm.set_query("bureau", function() {
				return {
					"filters": {
						"bureau": frm.doc.bureau
					}
				};
			});
		}
	 }
});
