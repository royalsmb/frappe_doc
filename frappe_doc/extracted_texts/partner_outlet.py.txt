# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PartnerOutlet(Document):
	def validate(self):
		#check if partner is already existing
		if frappe.db.exists('Partner Outlet', {'bureau_id': self.bureau_id}):
			frappe.throw('Partner Outlet already exists')
	
	#set the autoname
	def autoname(self):
		self.name = f'{self.bureau_name}'
	