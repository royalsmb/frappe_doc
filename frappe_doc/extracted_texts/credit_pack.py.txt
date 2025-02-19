# Copyright (c) 2025, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CreditPack(Document):
	def validate(self):
		if not frappe.db.exists("Item", self.pack_name):
			# create new item 
			if not frappe.db.exists("Item Group", "Credit Packs"):
				self.create_item_group()
			item = frappe.new_doc("Item")
			item.item_code = self.pack_name
			item.item_name = self.pack_name
			item.item_group = "Credit Packs"
			item.is_stock_item = 0
			item.standard_rate = self.price
			item.save(ignore_permissions=True)
			frappe.db.commit()
	def create_item_group(self):
		if not frappe.db.exists("Item Group", "Credit Packs"):
			item_group = frappe.new_doc("Item Group")
			item_group.item_group_name = "Credit Packs"
			item_group.save(ignore_permissions=True)
			frappe.db.commit()
