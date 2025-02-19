import frappe
from frappe.utils import cint
from dinks.v1.config import create_customer, create_invoice

@frappe.whitelist(allow_guest=True)
def get_products(category_id=None):
    try:
        if not category_id:
            items = frappe.get_all("Website Item", "name")
        else:
            items = frappe.get_all("Website Item", {"item_group": category_id}, ["name"])
        products = []
        for item in items:
            product = frappe.get_doc("Website Item", item.name)
            price = cint(frappe.get_value("Item Price", {"item_code": product.item_code, "price_list": "Standard Selling"}, "price_list_rate"))
            images = []
            if item.slideshow:
                slideshow = frappe.get_doc("Website Slideshow", item.slideshow)
                for slide in slideshow.slideshow_items:
                    images.append(frappe.utils.get_url(slide.image)) or ""
            specifications = frappe.get_all("Item Website Specification", {"parent": product.name}, ["label", "description"])
            # get the raw text of the description not the html
            spwcs_data = []
            for spec in specifications:
                spwcs_data.append({
                    "label": spec.label,
                    "description": frappe.utils.strip_html_tags(spec.description)
                })
            products.append({
                "product_id": product.name,
                "product_name": product.item_name,
                "product_thumbnail": frappe.utils.get_url(product.website_image) or "",
                "product_price": price,
                "category_id": product.item_group,
                "category_name": frappe.get_doc("Item Group", product.item_group).item_group_name,
                "is_featured": product.is_featured,
                "best_seller": product.best_seller,
                "product_details": product.description,
                "product_images": images,
                "Product_specifications": spwcs_data

            })
        frappe.local.response.update({
            "http_status_code": 200,
            "data": products,
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e),
        })

@frappe.whitelist(allow_guest=True)
def get_product_categories():
    try:
        categories = frappe.get_all("Item Group", ["name"])
        data = []
        for category in categories:
            if not frappe.db.exists("Website Item", {"item_group": category.name}):
                continue
            doc = frappe.get_doc("Item Group", category.name)
            data.append({
                "category_id": doc.name,
                "category_name": doc.item_group_name,
                "category_thumbnail": frappe.utils.get_url(doc.image) or "",
                "total_products": frappe.db.count("Item", {"item_group": doc.name})

            })
        frappe.local.response.update({
            "http_status_code": 200,
            "data": data,
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e),
        })