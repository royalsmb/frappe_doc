# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TopUp(Document):

	def on_submit(self):
		#update account balance in cash account
		cash_account = frappe.get_doc('Account Type', 'GMD')
		updated_cash_account = cash_account.account_balance + self.amount
		cash_account.db_set('account_balance', updated_cash_account)

		#update cash acocunt to specific branch
		branch_account = frappe.get_doc("Branch", self.branch)
		updated_branch_account = branch_account.account_balance + self.amount
		branch_account.db_set('account_balance', updated_branch_account)
		
	
