# Copyright (c) 2024, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dinks.v1.config import create_item
from frappe.utils import cint, flt


class Court(Document):
	def validate(self):
		if not frappe.db.exists("Item", self.name):
			self.create_item()
			
	def create_item(self):
		try:
			price = flt(frappe.db.get_value("Location", self.location, "price"))
			if not frappe.db.exists("Item Group", "Court"):
				item_group = frappe.new_doc("Item Group")
				item_group.item_group_name = "Court"
				item_group.save()
				frappe.db.commit()
			
			item = frappe.new_doc("Item")
			item.item_name = self.name
			item.item_code = self.name
			item.item_group = "Court"
			item.standard_rate = price
			item.is_stock_item = 0
			item.save()
			frappe.db.commit()
			return item
		except Exception as e:
			frappe.local.response.update({
				"http_status_code": 400,
				"error": str(e)
			})