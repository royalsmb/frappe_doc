# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Payout(Document):
    def validate(self):
        #check if there is enough cash in the cash account:
        branch = frappe.get_doc("Branch", self.branch)
        # if branch.account_balance < self.amount:
        #     frappe.throw("There is Not Enough Cash in This Branch ")
        
    def on_submit(self):
        #update account balance in cash account
        self.create_journal_entry()
        # updated_cash_account = cash_account.account_balance - self.amount
        # cash_account.db_set('account_balance', updated_cash_account)

        self.create_transaction()
        #append branches to to
        #update cash acocunt to specific branch
        # branch = frappe.get_doc("Branch", self.branch)
        # updated_amount = branch.account_balance - self.amount
        # branch.db_set('account_balance', updated_amount)
    
    #create a transaction after submit
    def create_transaction(self):
        branch = frappe.get_doc("Branch", self.branch)

        frappe.get_doc({
            "doctype": "Transactions",
            "transaction_type": "Payout",
            "amount": self.amount,
            "branch": branch,
            "bureau": branch.bureau,
            "mto": self.mto,
            "date": self.date
        }).insert()
        frappe.msgprint(("Transaction Created"))
    
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
                    "credit_in_account_currency": self.amount
                },
                {
                    "account": f'Write Off - {frappe.db.get_value("Bureau", branch.bureau, "abbr")}',
                    "debit_in_account_currency": self.amount,
                }
            ]
        })
        journal_entry.save(ignore_permissions=True)
        journal_entry.submit()
        frappe.msgprint("Journal Entry Created")