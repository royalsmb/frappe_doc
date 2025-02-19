from frappe.utils.data import cint
import requests
import frappe
from frappe.utils import getdate, now, flt

api_key = frappe.local.conf.shopify_api_key

@frappe.whitelist()
def set_shopify(limit=250):
    base_url = "https://doeraa.myshopify.com/admin/api/2021-04/orders.json"
    headers = {
        "X-Shopify-Access-Token": api_key,
    }
    orders = []
    url = f"{base_url}?limit={limit}"
    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            response_data = response.json()
            orders.extend(response_data.get('orders', []))
            
            # Get the 'Link' header from the response headers
            link_header = response.headers.get('Link')
            if link_header:
                # Parse the 'Link' header to find the next page URL
                links = link_header.split(',')
                next_url = None
                for link in links:
                    if 'rel="next"' in link:
                        next_url = link[link.find('<') + 1:link.find('>')]
                        break
                url = next_url
            else:
                url = None
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Error fetching Shopify data: {e}")
            break
    return orders
@frappe.whitelist()
def get_single_shopify_data(order_id):
    base_url = f"https://doeraa.myshopify.com/admin/api/2021-04/orders/{order_id}.json"
    headers = {
        "X-Shopify-Access-Token": api_key
    }
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        order_data = response.json().get('order')
        return order_data
    except requests.exceptions.RequestException as e:
        frappe.log_error(f"Error fetching Shopify data: {e}")
        return e

@frappe.whitelist()
def get_shopify_data():
   
    base_url = "https://doeraa.myshopify.com/admin/api/2021-04/orders.json"
    headers = {
        "X-Shopify-Access-Token": api_key
    }
    orders = []
    # # All orders except draft
    url = f"{base_url}?limit=250"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    orders = response.json()

    #remove duplicate items from the sales order
    
    return create_sales_order(orders.get('orders', []))

@frappe.whitelist()
def sync_shopify_orders(limit=250):
    """
    Manually trigger the synchronization of Shopify orders and create Sales Orders in the system.
    """
    try:
        shopify_orders = set_shopify(limit) 
        sales_orders = create_sales_order(shopify_orders)          
        return f"{len(sales_orders)} Sales Orders created successfully!"
    except Exception as e:
        # Log and notify the user about any errors during synchronization
        frappe.log_error(f"Error during Shopify order sync: {e}")
        frappe.throw(f"An error occurred while syncing Shopify orders: {e}")

    

def create_sales_order(orders):
    sales_order_names = []
    for order in orders:
        try:
            # Check if sales order exists; if not, then create
            if frappe.db.exists("Sales Order", {"shopify_order_id": order.get("id")}):
                continue
            customer_data = order.get("customer")
            if not customer_data:
                frappe.log_error(f"No customer data for order {order.get('id')}")
                continue
            
            customer_name = f"{customer_data.get('first_name')} {customer_data.get('last_name')}"
            customer = create_customer(customer_name)
            address = get_address(order, customer_name)
            items = get_items(order)
            taxes = get_taxes(order)
            sales_order = frappe.get_doc({
                "doctype": "Sales Order",
                "company": "Doeraa Private Limited",
                "customer": customer,
                "customer_address": address,
                "items": items,
                "tax_category": get_tax_category(order),
                "taxes": taxes,
                "delivery_date": now(),
                'transaction_date': getdate(order.get('created_at')),
                'shopify_order_id': order.get('id'),
                'shopify_order_number': order.get('name'),
                "discount_amount": flt(calculate_discount(order)),
                
            })
            frappe.flags.ignore_validate = True
            sales_order.insert(ignore_permissions=True)
            create_shipping_charges(order)
            frappe.db.commit()
            sales_order_names.append(sales_order.name)
        except Exception as e:
            frappe.log_error(f"Error creating sales order: {e}")
    return sales_order_names
def calculate_discount(order):
    discount_codes = order.get('discount_codes', [])
    if discount_codes:
        discount = discount_codes[0].get('amount')
        return discount
    return 0
def get_tax_category(order):   
    province = order.get('billing_address', {}).get('province')
    if province == "Gujarat":
        category = "In-state"
    else:
        category = "Out-state"
    return category

@frappe.whitelist()
def get_items(order):
    order_items = order.get('line_items', [])
    items = []

    for item in order_items:
        # Check if item is available; if not, then create
        if not frappe.db.exists("Item", item.get('sku')):
            item_code = item.get('sku')
            item_name = item.get('name')
            create_item(item_code, item_name)
        
        items.append({
            "item_code": item.get('sku'),
            "item_name": item.get('name')[:140],
            "rate": item.get('price'),
            "qty": item.get('quantity'),
            "warehouse": "Finished Goods - DPL",
            "delivery_date": now(),
            "uom": "Meter",
            "gst_treatment": "Taxable"
        })
    return items

def create_item(item_code, item_name):
    item = frappe.get_doc({
        "doctype": "Item",
        "item_code": item_code,
        "item_name": item_name,
        "item_group": "Products",
        "gst_hsn_code": "998821",
        "uom": "Meter",
    })
    item.insert(ignore_permissions=True)
    frappe.db.commit()

def get_taxes(order):
    taxes = []
    tax_included = order.get('taxes_included')
    tax_category = get_tax_category(order)
    if tax_category == "Out-state":
                taxes.append({
                    "charge_type": "On Net Total",
                    "account_head": "Output Tax IGST - DPL",
                    "cost_center": "Main - DPL",
                    "rate": 5,
                    "description": "IGST - 5.00%",
                    "included_in_print_rate": tax_included
                })
    else:
        taxes.append({
            "charge_type": "On Net Total",
            "account_head": "Output Tax CGST - DPL",
            "cost_center": "Main - DPL",
            "rate": 2.5,
            "description": "SGST - 2.50%",
            "included_in_print_rate": tax_included
        })
        taxes.append({
            "charge_type": "On Net Total",
            "account_head": "Output Tax SGST - DPL",
            "cost_center": "Main - DPL",
            "rate": 2.5,
            "description": "CGST - 2.50%",
            "included_in_print_rate": tax_included
        })
    return taxes

def create_customer(customer_name):
    if frappe.db.exists("Customer", {"customer_name": customer_name}):
        customer = frappe.get_doc("Customer", {"customer_name": customer_name})
    else:
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": customer_name
        })
        customer.insert(ignore_permissions=True)
        frappe.db.commit()
    return customer.name

def get_address(order, customer_name):
    address = order.get("shipping_address")
    if not address:
        return None
    
    if frappe.db.exists("Address", {"address_title": customer_name}):
        customer_address = frappe.get_doc("Address", {"address_title": customer_name})
    else:
        customer_address = frappe.get_doc({
            "doctype": "Address",
            "address_title": customer_name,
            "address_line1": address.get("address1")[:140],
            "city": address.get("city"),
            "state": address.get("province"),
            "country": address.get("country"),
            "pincode": address.get("zip")
        })
        customer_address.insert(ignore_permissions=True)
        frappe.db.commit()
    return customer_address.name

@frappe.whitelist()
def taxees():
    order_id = "5453587153150"
    base_url = f"https://doeraa.myshopify.com/admin/api/2021-04/orders/{order_id}.json"
    headers = {
        "X-Shopify-Access-Token": api_key
    }
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        order_data = response.json().get('order')
        tax_lines = order_data.get('tax_lines', [])
        tax_included = order_data.get('taxes_included')
        return {"tax_lines": tax_lines, "tax_included": tax_included}
    except requests.exceptions.RequestException as e:
        frappe.log_error(f"Error fetching Shopify data: {e}")
        return "Error"
@frappe.whitelist()
def update_shipping_carhges(orders):
     sales_orders = []
     for order in orders.get('orders', []):
        try:
            sales_order = frappe.get_doc("Sales Order", {"shopify_order_id": order.get("id"), "docstatus": 0})
            shipping_lines = order.get('shipping_lines', [])
            if not shipping_lines:
                continue

            if shipping_lines:
                charge = shipping_lines[0].get('price')
                if float(charge) > 0:
                    append_item(sales_order, "SHIPPING CHARGES", "SHIPPING CHARGES", charge, 1, "Finished Goods - DPL", getdate(now()), "Nos")
                sales_orders.append(charge)
                                   
        except Exception as e:
            frappe.log_error(f"Error updating shipping charges: {e}")
     return sales_orders
def append_item(sales_order, item_code, item_name, rate, qty, warehouse, delivery_date, uom):
    sales_order.append("items", {
        "item_code": item_code,
        "item_name": item_name,
        "rate": rate,
        "qty": qty,
        "warehouse": warehouse,
        "delivery_date": delivery_date,
        "uom": uom
    })
    sales_order.save()
    frappe.db.commit()
 
@frappe.whitelist()
def shipping_charges():   
    base_url = "https://doeraa.myshopify.com/admin/api/2021-04/orders.json"
    headers = {
        "X-Shopify-Access-Token": api_key
    }
    orders = []
    # # All orders except draft
    url = f"{base_url}?limit=250"
    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            response_data = response.json()
            orders.extend(response_data.get('orders', []))
            
            # Get the 'Link' header from the response headers
            link_header = response.headers.get('Link')
            if link_header:
                # Parse the 'Link' header to find the next page URL
                links = link_header.split(',')
                next_url = None
                for link in links:
                    if 'rel="next"' in link:
                        next_url = link[link.find('<') + 1:link.find('>')]
                        break
                url = next_url
            else:
                url = None
        except requests.exceptions.RequestException as e:
            frappe.log_error(f"Error fetching Shopify data: {e}")
            break
    return update_shipping_carhges({"orders": orders})

def remove_duplicate_items(sales_order):
    items = sales_order.get("items")
    item_codes = []
    for item in items:
        if item.get("item_code") not in item_codes:
            item_codes.append(item.get("item_code"))
        else:
            sales_order.remove(item)
    return sales_order

@frappe.whitelist()
def remove_item():
    # get last 10 orders
    # orders = frappe.get_all("Sales Order", filters={"docstatus": 0}, order_by="creation desc", limit=10)
    orders = frappe.get_all("Sales Order", filters={"docstatus": 0})
    for order in orders:
        sales_order_doc = frappe.get_doc("Sales Order", order.name)
        sales_order = remove_duplicate_items(sales_order_doc)
        sales_order.save()
        frappe.db.commit()
        frappe.msgprint("Items removed successfully")
    return "Items removed successfully"
#create discount
@frappe.whitelist()
def create_discount():
    orders = set_shopify(limit=250)
    discount_codes = []
    for o in orders:
        discount_code = o.get('discount_codes', [])
        if discount_code:
            discount = discount_code[0].get('amount')
            discount_codes.append(discount)
            doc = frappe.get_doc("Sales Order", {"shopify_order_id": o.get("id"), "docstatus": 0})
            doc.apply_discount_on = "Grand Total"
            doc.discount_amount = cint(discount)
            doc.save()
            frappe.db.commit()
    return discount_codes
    
def create_shipping_charges(order):
    doc = frappe.get_doc("Sales Order", {"shopify_order_id": order.get("id")})
    shipping_lines = order.get('shipping_lines', [])
    if  shipping_lines:
        charge = shipping_lines[0].get('price')
        if float(charge) > 0:
            append_item(doc, "SHIPPING CHARGES", "SHIPPING CHARGES", charge, 1, "Finished Goods - DPL", getdate(now()), "Nos")
            doc.save()
            frappe.db.commit()
    
