import frappe
# from dinks.config import 

@frappe.whitelist(allow_guest=True)
def change_password():
    try:
        data = frappe.local.form_dict
        email = data.get('email')
        old_password = data.get('old_passwrod')
        new_password = data.get('password')

        user = frappe.get_doc("User", email)
        frappe.db.set_value("User", email, "new_password", new_password)
        frappe.db.commit()
        frappe.local.response.update({
            "http_status_code": 200,
            "data": "Password changed successfully"
        })

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), ("Failed to change password"))
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })


    
@frappe.whitelist( allow_guest=True )
def update_profile():
    try:
        data = frappe.local.form_dict
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        mobile_number = data.get("mobile_number")
        date_of_birth = data.get("birth_date")
        geder = data.get("gender")

        user = frappe.get_doc('User', frappe.session.user)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.mobile_no = mobile_number
        user.birth_date = date_of_birth
        user.save()

        frappe.db.commit()
        frappe.local.response.update({
            "http_status_code": 200,
            "data": "Your profile has been updated successfully"
        })

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), ("Failed to update profile"))
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def get_profile():
    try:
        user = frappe.get_doc('User', frappe.session.user)
        data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "mobile_number": user.mobile_no,
            "date_of_birth": user.birth_date,
            "gender": user.gender
        }
        frappe.local.response.update({
            "http_status_code": 200,
            "data": data
        })
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), ("Failed to get profile"))
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
