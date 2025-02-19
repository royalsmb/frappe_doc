// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase', {
	
		amount: function(frm){
			update_amount_to_receive(frm);
		},
		exchange_rate: function(frm){
			update_amount_to_receive(frm);
		}
	
});

function update_amount_to_receive(frm){
	var  amount= frm.doc.amount;
	var exchange_rate = frm.doc.exchange_rate;
	var total = amount * exchange_rate;
	frm.set_value("total", total);

}
