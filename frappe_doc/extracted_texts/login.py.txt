import frappe
from frappe import auth
# 1. User Login API

# This API will authenticate the user based on the provided email and password.

# Endpoint: /auth/login
# Method: POST

# Request body:

# {
#   "usr": "rbspl8@reformiqo.com",
#   "pwd": "rbspl8"
# }

# Response:

# {
#   "message": {
#     "success_key": 1,
#     "message": "Authentication success",
#     "sid": "4193a7f39c9e3b7cbca6ca5bd2f5e95948b9b4cec2dafbd278f04fcd",
#     "api_key": "ac91b19a3607e90",
#     "api_secret": "915557441408656",
#     "username": "RBSPL",
#     "email": "rbspl8@reformiqo.com",
#   }
# }




@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        # Initialize and authenticate the login manager
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key": 0,
            "message": "Invalid login credentials"
        }
        return
    # Generate API key and secret

    api_secret = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)
    employee = frappe.get_doc('Customer Employees', {'email': user.email})
    data = {

    
        "success_key": 1,
        "message": "Authentication success",
        "sid": frappe.session.sid,
        "api_key": user.api_key,
        "api_secret": api_secret,
        "username": user.username,
        
    }
    
    frappe.response["message"] = data
def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    
    # Generate a new API secret
    api_secret = frappe.generate_hash(length=15)

    # If API key doesn't exist, generate it
    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    # Set the API secret
    user_details.api_secret = api_secret
    
    # Save the user details to update the document
    user_details.save(ignore_permissions=True)
    frappe.db.commit()

    return api_secret


@frappe.whitelist(allow_guest=True)
def reset_password(email):
    try:
        user = frappe.get_doc('User', email)
        return {
            "success_key": 1,
            "message": user.reset_password(send_email=True, password_expired=True)
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), ("Failed to reset password"))
        return {
            "success_key": 0,
            "error": str(e)
        }
@frappe.whitelist(allow_guest=True)
def change_password(email, old_password, new_password):
    pass