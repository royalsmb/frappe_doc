# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InternalTransfer(Document):
	

	def validate(self):
		from_account_doc = frappe.get_doc("Branch", self.from_account)
		if from_account_doc.account_balance < self.amount:
			frappe.throw("Insufficent amount of Cash In " + self.from_account + " Branch")
		if self.from_account == self.to_account:
			frappe.throw("You cannot Transfer from The same account to The same account")

	def on_submit(self):
		from_account_doc = frappe.get_doc("Branch", self.from_account)
		to_account_doc = frappe.get_doc("Branch", self.to_account)
		from_account_value = from_account_doc.account_balance - self.amount
		to_account_value = to_account_doc.account_balance + self.amount
		from_account_doc.db_set('account_balance', from_account_value)
		to_account_doc.db_set('account_balance', to_account_value)
		
		
