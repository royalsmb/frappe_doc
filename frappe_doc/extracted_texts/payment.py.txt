import frappe
import requests
import razorpay
import datetime
from frappe import _
from frappe.utils import cint


@frappe.whitelist()
def create_invoice():
    doc = frappe.get_doc("Sales Invoice", "ACC-SINV-2024-00001")
    settings = frappe.get_doc("Razorpay Settings")
    id = settings.api_key
    secret = settings.get_password("api_secret")
    client = razorpay.Client(auth=(id, secret))

    items = []
    for item in doc.items:
        items.append({
            "name": item.item_code,
            "quantity": item.qty,
            "amount": cint(item.rate) * (100)
        })
    customer = {
        "name": doc.customer
    }
    data = {
        "type": "invoice",
        "description": "Invoice for the month of January 2020",
        "customer": customer,
        "line_items": items,
    }
    response = client.invoice.create(data)
    return response.get('short_url')

