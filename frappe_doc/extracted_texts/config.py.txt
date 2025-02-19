import frappe
import erpnext

@frappe.whitelist()
def create_invoice(items: list, payments: list, customer:str = None, shipping:dict = None, reference=None):
    try:
        if not frappe.db.exists("POS Profile", "Dink POS"):
            create_pos_profile()

        
        if not customer and not frappe.db.exists("Customer", {"email": frappe.session.user}):
            user = frappe.get_doc("User", frappe.session.user)
            name = user.full_name
            create_customer(full_name, frappe.session.user)
        if frappe.db.exists("Customer", {"email": frappe.session.user}):
            customer = frappe.get_doc("Customer", {"email": frappe.session.user}).name
        invoice = frappe.new_doc("Sales Invoice")
        invoice.customer = customer
        invoice.company = erpnext.get_default_company()
        
        for item in items:
            invoice.append("items", {
                "item_code": item.get("item_code"),
                "qty": item.get("qty"),
                "rate": item.get("rate"),
            })
        if payments:
            pos_profile = frappe.get_doc("POS Profile", "Dink POS")
            invoice.is_pos = 1
            invoice.pos_profile = pos_profile.name
            for payment in payments:
                invoice.append("payments", {
                    "mode_of_payment": payment.get("mode_of_payment"),
                    "amount": payment.get("amount")
                })
        invoice.dink_reference = reference
        
        invoice.save()
        invoice.submit()
        frappe.db.commit()
        return invoice
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
       

@frappe.whitelist()
def create_pos_profile():
    try:
        company_name = erpnext.get_default_company()
        company = frappe.get_doc("Company", company_name)
        abbr = company.abbr
        stock_settings = frappe.get_doc("Stock Settings", "Stock Settings")
        default_warehouse = stock_settings.default_warehouse
        
        pos_profile = frappe.new_doc("POS Profile")
        pos_profile.name = "Dink POS"
        pos_profile.company = company.name
        pos_profile.append("payments", {
        "mode_of_payment": "Cash",
        "default": 1
        })
        pos_profile.append("payments", {
            "mode_of_payment": "Credit Card",
        })
        pos_profile.write_off_account = company.write_off_account
        pos_profile.write_off_cost_center = company.cost_center
        pos_profile.warehouse = default_warehouse
        pos_profile.save()
        frappe.db.commit()
        return pos_profile
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
@frappe.whitelist()
def create_customer(name: str, email: str):
    try:
        customer = frappe.new_doc("Customer")
        customer.customer_name = name
        customer.email = email
        customer.save()
        frappe.db.commit()
        return customer
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

def create_item(name: str, price: float, item_group: str):
    try:
        if not frappe.db.exists("Item Group", item_group):
            item_group = frappe.new_doc("Item Group")
            item_group.item_group_name = item_group
            item_group.save()
            frappe.db.commit()
        
        item = frappe.new_doc("Item")
        item.item_name = name
        item.item_code = name
        item.item_group = item_group
        item.standard_rate = price
        item.is_stock_item = 0
        item.save()
        frappe.db.commit()
        return item
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })