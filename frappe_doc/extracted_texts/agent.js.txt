// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Agent', {
	first_name: function(frm){
		let full_name = (frm.doc.first_name || " ") + " " + (frm.doc.middle_name || " ")  + " " + (frm.doc.last_name || " ");
		frm.set_value("full_name", full_name)
	},

	last_name: function(frm){
		let full_name = (frm.doc.first_name || " ") + " " + (frm.doc.middle_name || " ")  + " " + (frm.doc.last_name || " ");
		frm.set_value("full_name", full_name)
	},

	middle_name: function(frm){
		let full_name = (frm.doc.first_name || " ") + " " + (frm.doc.middle_name || " ")  + " " + (frm.doc.last_name || " ");
		frm.set_value("full_name", full_name)
	}
	// refresh: function(frm) {

	// }
});
