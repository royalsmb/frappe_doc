# Copyright (c) 2024, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dinks.v1.config import create_invoice



class Booking(Document):
	def on_submit(self):
		schedule = frappe.new_doc("Court Schedule")
		schedule.court = self.court
		schedule.location = frappe.db.get_value("Court", self.court, "location")
		schedule.date = self.date
		schedule.start_time = self.start_time
		schedule.end_time = self.end_time
		schedule.players = self.players
		schedule.booking = self.name
		schedule.save()
		frappe.db.commit()

		item = frappe.get_doc("Item", self.court)
		location = frappe.get_doc("Location", frappe.db.get_value("Court", self.court, "location"))

		items = [{
			"item_code": item.name,
			"qty": 1,
			"rate": location.price
		}]

		create_invoice(
			items=items,
			customer=self.customer,
			payments=[],
			reference =self.name,
		)
			
	def on_cancel(self):
		schedule = frappe.get_doc("Court Schedule", {"booking": self.name})
		schedule.delete()
		frappe.db.commit()
		if frappe.db.exists("Invoice", {"dink_reference": self.name}):
			invoice = frappe.get_doc("Invoice", {"dink_reference": self.name})
			invoice.cancel()
		