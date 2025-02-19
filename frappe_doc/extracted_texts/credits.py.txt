import frappe
from dinks.v1.config import create_customer
from frappe.utils import flt, getdate, add_to_date, cint

@frappe.whitelist()
def get_packs():
    try:
        packs = frappe.get_all("Credit Pack", ["name", "pack_name", "hours", "validity_days", "price", "description"])
        data = []
        for pack in packs:
            data.append({
                "pack_id": pack.name,
                "pack_name": pack.pack_name,
                "hours": pack.hours,
                "validity_days": pack.validity_days,
                "price": pack.price,
                "description": pack.description
            })
        return {
            "success_key": 1,
            "message": "Credit packs fetched successfully",
            "data": data
        }
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
    
@frappe.whitelist()
def purchase_credit_pack(plan_id:str, payment_method:str, payment_id:str=None):
    try:
        user = frappe.session.user
        if not frappe.db.exists("Customer", {"email": user}):
            full_name = frappe.db.get_value("User", user, "full_name")
            create_customer(full_name, user)
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
        customer = frappe.get_doc("Customer", {"email": user})
        credit_transaction = frappe.new_doc("Credit Transaction")
        credit_transaction.customer = customer.name
        credit_transaction.plan = plan.name
        credit_transaction.payment_method = payment_method
        credit_transaction.payment_id = payment_id
        credit_transaction.save()
        credit_transaction.submit()
        frappe.db.commit()
        frappe.local.response.update({
            "http_status_code": 200,
            "message": {
                "user_id": user,
                "pack_name": plan.pack_name,
                "hours": plan.hours,
                "price": plan.price,
                "validity_days": plan.validity_days,
                "total_credits": customer.credit_balance,
                "expiry_date": add_to_date(credit_transaction.creation, days=cint(plan.validity_days), as_string=True),
                "transaction_id": credit_transaction.name,
                "purchase_date": getdate(credit_transaction.creation)
            }
        })
    except Exception as e:
        frappe.log_error(f"Error purchasing credit pack: {str(e)}", "Purchase Credit Pack")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)

        })

@frappe.whitelist()
def get_purchase_history():
    try:
        user = frappe.session.user
        customer = frappe.get_doc("Customer", {"email": user})
        credits = frappe.db.get_value("Customer", customer.name, "credit_balance")
        transactions = frappe.get_all("Credit Transaction", {"customer": customer.name}, ["name", "plan"])
        purchase_history = []
        total_credits_purchased = 0
        for transaction in transactions:

            last_doc = frappe.get_doc("Credit Transaction", transaction.name)
            plan = frappe.get_doc("Credit Pack", transaction.plan)
            total_credits_purchased += flt(plan.hours)
            purchase_history.append({
                "pack_name": plan.pack_name,
                "hours": plan.hours,
                "price": plan.price,
                "purchase_date": getdate(transaction.creation),
                "expiry_date": add_to_date(transaction.creation, days=cint(plan.validity_days), as_string=True)
            })


        return {
            "success_key": 1,
            "message": "Purchased credits fetched successfully",
            "data": {
                "available_credits": credits,
                "total_credits_purchased": total_credits_purchased,
                "last_purcahsed":{
                    "pack_name": plan.pack_name,
                    "hours": plan.hours,
                    "price": plan.price,
                    "purchase_date": getdate(last_doc.creation),
                    "expiry_date": add_to_date(last_doc.creation, days=cint(plan.validity_days), as_string=True)
                    
                },
                "purchase_history": purchase_history
            }
        }
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })