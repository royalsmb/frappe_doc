# Copyright (c) 2025, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dinks.v1.config import create_invoice




class CreditTransaction(Document):
	def on_submit(self):
		try:
			purchase_credit_pack(self.plan, self.payment_method)
			credits = frappe.db.get_value("Credit Pack", self.plan, "hours")
			balance = frappe.db.get_value("Customer", self.customer, "credit_balance") + credits
			frappe.db.set_value("Customer", self.customer, "credit_balance", balance)
			frppe.db.commit()
		except Exception as e:
			frappe.log_error(f"Error purchasing credit pack: {str(e)}", "Purchase Credit Pack")
def purchase_credit_pack(plan_id:str, payment_method:str):
    try:
        if not frappe.db.exists("Credit Pack", plan_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid pack id"
            })
            return
        if not frappe.db.exists("Mode of Payment", payment_method):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid payment method"
            })
            return
        plan = frappe.get_doc("Credit Pack", plan_id)
        items = [{
            "item_code": plan.pack_name,
            "qty": 1,
            "rate": plan.price
        }]
        payments = [{
            "mode_of_payment": payment_method,
            "amount": plan.price
        }]
        create_invoice(items, payments)
        
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Credit pack purchased successfully"
        })
    except Exception as e:
        frappe.log_error(f"Error purchasing credit pack: {str(e)}", "Purchase Credit Pack")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)

        })

        