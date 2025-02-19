# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Sales(Document):
	def validate(self):
		cash_account = frappe.get_doc('Account Type', self.currency)
		if cash_account.account_balance < self.total:
			frappe.throw("Insufficient amount of " + self.currency + " to Perform This Transaction")

	def on_submit(self):
		cash_account = frappe.get_doc('Account Type', 'GMD')
		cash = cash_account.account_balance + self.total
		cash_account.db_set("account_balance", cash)


		account_type = frappe.get_doc('Account Type', self.currency_name)
		account_balance = account_type.account_balance - self.amount
		account_type.db_set('account_balance', account_balance)