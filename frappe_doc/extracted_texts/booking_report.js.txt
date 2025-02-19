// Copyright (c) 2024, Erpera and contributors
// For license information, please see license.txt

frappe.query_reports["Booking Report"] = {
	"filters": [
		{
			"fieldname": "date",
			"Label": "Date",
			"fieldtype": "Date",
			
		},
		// location
		{
			"fieldname": "location",
			"Label": "Loction",
			"fieldtype": "Link",
			"Options": "Location Courts"
		}

	],
	"formatter": function(value, row, column, data, default_formatter) {
		if (column.fieldname == "status") {
			if (value == "Paid") {
				value = `<b style="color:green">${value}</b>`
			}
			else if (value == "Not Paid") {
				value = `<b style="color:orange">${value}</b>`
			}
			
			
		}
		return default_formatter(value, row, column, data);
	}
};
