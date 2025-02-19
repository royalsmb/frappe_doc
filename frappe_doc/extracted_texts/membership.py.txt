import frappe
from dinks.config import validate_request_params
from inspect import signature
from frappe.utils import today, getdate, now
from frappe.core.utils import find
from dinks.v1.config import create_customer

@frappe.whitelist()
def get_membership_plans():
    try:
        plans = frappe.get_all("Subscription Plan")
        data = []
        for plan in plans:
            doc = frappe.get_doc("Subscription Plan", plan.name)
            benefits = frappe.get_all("Plan Benefits", {"parent": doc.name}, ["benefit"])
            data.append({
                "plan_id": doc.name,
                "plan_name": doc.plan_name,
                "description": doc.custom_description,
                "duration":f"{doc.billing_interval_count} {doc.billing_interval.lower()}s",
                "price": doc.cost,
                "benefits": benefits
                
            })
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Membership plans fetched successffully",
            "data": data
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def purchase_membership(plan_id: str):
    try:
        import erpnext
        if not frappe.db.exists("Subscription Plan", plan_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid Plan Id"
            })
            return
        
        if not frappe.db.exists("Customer", frappe.session.user):
            user = frappe.session.user
            full_name = frappe.db.get_value("User", user, "full_name")
            customer = create_customer(full_name, user)
        else:
            customer = frappe.get_doc("Customer", frappe.session.user)
        
        subscriptions = frappe.get_all("Subscription", {"party": customer.name})
        for subscription in subscriptions:
            doc = frappe.get_doc("Subscription", subscription.name)
            for plan in doc.plans:
                if plan.plan == plan_id:
                    frappe.local.response.update({
                        "http_status_code": 400,
                        "error": "You have already purchased this plan"
                    })
                    return

        subscription = frappe.new_doc("Subscription")
        subscription.party_type = "Customer"
        subscription.party = customer.name
        subscription.start_date = today()
        subscription.company = erpnext.get_default_company()
        subscriptiongenerate_invoice_at = "Beginning of the current subscription period"
        subscription.append("plans", {
            "plan": plan_id,
            "qty": 1,
        })
        subscription.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Membership plan purchased successfully",
            "data": {
                "subscription_id": subscription.name,
                "plan_id": plan_id,
                "price": frappe.db.get_value("Subscription Plan", plan_id, "cost"),
                "start_date": subscription.start_date,
                "end_date": subscription.end_date,
                "susbcription_date": subscription.start_date,
            }
        })


    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def get_membership_status():
    try:
        if frappe.db.exists("Customer", {"email": frappe.session.user}):
            customer = frappe.get_doc("Customer", {"email": frappe.session.user})
            active_subscription = frappe.get_doc("Subscription", {"party": customer.name, "status": "Active"})
            if active_subscription:
                plan = frappe.get_doc("Subscription Plan", active_subscription.plans[0].plan)
                active_membership = {
                    "membership_name": plan.name,
                    "validity_days": f"{plan.billing_interval_count} {plan.billing_interval.lower()}s",
                    "price": plan.cost,
                    "purchase_date": getdate(active_subscription.creation),
                    "expiry_date": active_subscription.end_date
                }
            subscriptions = frappe.get_all("Subscription", {"party": customer.name})
            purcahse_history = []
            for subscription in subscriptions:
                doc = frappe.get_doc("Subscription", subscription.name)
                plan = frappe.get_doc("Subscription Plan", doc.plans[0].plan)
                purcahse_history.append({
                    "membership_name": plan.name,
                    "validity_days": f"{plan.billing_interval_count} {plan.billing_interval.lower()}s",
                    "price": plan.cost,
                    "purchase_date": getdate(doc.creation),
                    "expiry_date": doc.end_date
                })
            frappe.local.response.update({
                "http_status_code": 200,
                "message": "Membership status fetched successfully",
                "data": {
                    "active_membership": active_membership,
                    "purchase_history": purcahse_history
                }
            })
        else:
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "User has no active subscriptions"
            })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
    