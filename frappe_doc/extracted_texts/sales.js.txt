// Copyright (c) 2023, Momodou khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales', {
	
	amount: function(frm){
		update_amount_to_pay(frm);
	},
	exchange_rate: function(frm){
		update_amount_to_pay(frm);
	}

});

function update_amount_to_pay(frm){
var  amount= frm.doc.amount;
var exchange_rate = frm.doc.exchange_rate;
var total = amount * exchange_rate;
frm.set_value("total", total);

}
