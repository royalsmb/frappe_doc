# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transfer(Document):
	def on_submit(self):
		self.create_journal_entry()
		self.create_transaction()

	#create journal entry
    def create_journal_entry(self):
		branch = frappe.get_doc("Branch", self.branch)
		journal_entry = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Journal Entry",
            "company": frappe.db.get_value("Bureau", branch.bureau, "business_name"),
            "posting_date": self.date,
            "accounts": [
                {
                    "account": f'{branch.branch_name} - {frappe.db.get_value("Bureau", branch.bureau, "abbr")}',
                    "debit_in_account_currency": self.amount
                },
                {
                    "account": f'Write Off - {frappe.db.get_value("Bureau", branch.bureau, "abbr")}',
                    "credit_in_account_currency": self.amount,
                }
            ]
        })
        journal_entry.save(ignore_permissions=True)
        journal_entry.submit()
        frappe.msgprint("Journal Entry Created")
		
	def create_transaction(self):
		branch = frappe.get_doc("Branch", self.branch)
		frappe.get_doc({
            "doctype": "Transactions",
            "transaction_type": "Transfer",
            "amount": self.amount,
            "branch": branch,
            "bureau": branch.bureau,
            "mto": self.mto,
            "date": self.date
			}).insert()