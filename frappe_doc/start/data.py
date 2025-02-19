import frappe
from frappe_doc import bruno

@frappe.whitelist()
@bruno(method="get")
def book_slot(facility_id, user_id, date, start_time, end_time, used_credits=None):
    """
    Hello khan work hard please
    """
    # Your implementation here
    pass

@frappe.whitelist(allow_guest=True)
@bruno()
def hello_khan(khan: str):
    """
    This is just the beginning of something great
    """
    # Your implementation here
    return "Hello Khan"


