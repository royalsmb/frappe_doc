import frappe
from frappe import auth

@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        if frappe.request.method != "POST":
            frappe.local.response.update({
            "http_status_code": 405,
            "error": "Method not allowed"
            })
            return
        # Initialize and authenticate the login manager
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

        
        

    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response.update({
            "http_status_code": 403,
            "error": "Invalid login credentials"
        })
        return
    # Generate API key and secret

    api_secret = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)
    data = {

    
        "success_key": 1,
        "message": "Authentication success",
        "sid": frappe.session.sid,
        "api_key": user.api_key,
        "api_secret": api_secret,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": user.gender,
        "date_of_birth": user.birth_date
        
    }
    frappe.clear_messages()
    frappe.local.response.update({
            "http_status_code": 200,
            "data": data
    })
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
def signup():
    try:
        data = frappe.local.form_dict
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        gender = data.get("gender")
        date_of_birth = data.get("date_of_birth")
        mobile_number = data.get("mobile_number")
        


        if frappe.db.exists("User", email):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "User email already registered, please login"
            })

        elif frappe.db.exists("User", {"mobile_no": mobile_number}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Mobile number already registered, please login"
            })

        else:
            user = frappe.new_doc("User")
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.new_password = password
            user.send_welcome_email = 0
            user.gender = gender
            user.birth_date = date_of_birth
            user.insert(ignore_permissions=True)
            frappe.db.commit()

            frappe.clear_messages()
            frappe.local.response.update({
                "http_status_code": 200,
                "data": "Your account has been created successfully",
            })

    except Exception as e:
        # Rollback in case of error to avoid partial creation
        frappe.log_error(frappe.get_traceback(), ("Failed to create user"))
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })


@frappe.whitelist(allow_guest=True)
def forget_password():
    try:
        data = frappe.local.form_dict
        email = data.get("email")
        user = frappe.get_doc("User", email)
        if not user:
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "User not found"
            })
        else:
            user.reset_password()
            frappe.local.response.update({
                "http_status_code": 200,
                "data": "Password reset link has been sent to your email"
            })

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), ("Failed to reset password"))
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })


