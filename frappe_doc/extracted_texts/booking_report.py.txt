# Copyright (c) 2024, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"fieldname": "time",
			"label": "Time",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "court",
			"label": "Court",
			"fieldtype": "Data",
			"width": 200
		},
		# court number
		{
			"fieldname": "court_number",
			"label": "Court Number",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"filedname": "customer",
			"label": "Customer",
			"fieldtype": "Data",
			"width": 200
		},
		# amount
		{
			"fieldname": "amount",
			"label": "Amount",
			"fieldtype": "Currency",
			"width": 200
		},
		# status
		{
			"fieldname": "status",
			"label": "Status",
			"fieldtype": "Data",
			"width": 200
		},


	]

def get_data(filters):
	bookings = frappe.get_all("Booking", fields=["name", "date", "time_period", "court", "customer", "players", "pay_at_court"])
	
		
	data = []
	for booking in bookings:
		location = frappe.db.get_value("Location Courts", booking.court, "court")
		if getdate(filters.get("date")) and getdate(filters.get("date")) != getdate(booking.date):
			continue
		if filters.get("location") and filters.get("location") != location:
			continue
		if booking.pay_at_court == 0:
			status = "Paid"
		else:
			status = "Not Paid"
		amount = 0
		if frappe.db.exists("Sales Invoice", {"custom_booking_id": booking.name}):
			amount = frappe.db.get_value("Sales Invoice",  {"custom_booking_id": booking.name}, "total")
		
		data.append({

			"time": booking.time_period,
			"court": booking.court,
			"court_number": frappe.db.get_value("Location Courts", booking.court, "court_number"),
			"customer": booking.customer,
			"amount": amount,
			"status": status



		})
	return data