import frappe

@frappe.whitelist(allow_guest=True)
def create_user():
    try:
        data = frappe.local.form_dict
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        gender = data.get("gender")
        date_of_birth = data.get("date_of_birth")
        mobile_number = data.get("mobile_number")
        


        customer_mobile = frappe.db.get_value("Customer Employees", {"mobile": mobile_number}, "mobile")
        if frappe.db.exists("Customer Employees", {"email": email}):
            return {
                "success_key": 0,
                "error": "User email already registered, please login"
            }

        elif customer_mobile:
            return {
                "success_key": 0,
                "error": "Mobile number already registered, please login"
            }

        else:
            employee = frappe.new_doc("Customer Employees")
            employee.full_name = full_name
            employee.email = email
            employee.password = password
            employee.occupation = occupation
            employee.designation = designation
            employee.date_of_birth = date_of_birth
            employee.vehicle_number = vehicle_number
            
            if cid:
                employee.customer = cid
            else:
                # create customer
                customer = frappe.new_doc("Customer")
                customer.customer_name = full_name
                customer.customer_type = "Individual"
                customer.custom_space = space_id
                customer.custom_credit_balance = 10
                customer.save(ignore_permissions=True)

                frappe.db.commit()
                employee.customer = customer.name
                employee.is_admin = 1
                employee.status = "Active"

            employee.mobile = mobile
            employee.save(ignore_permissions=True)
            frappe.db.commit()
            

            return {
                "message": "Your account has been created successfully",
                "success_key": 1
            }

    except Exception as e:
        # Rollback in case of error to avoid partial creation
        frappe.log_error(frappe.get_traceback(), ("Failed to create user"))
        return {
            "success_key": 0,
            "error": str(e)
        }

        # return user.name


@frappe.whitelist( allow_guest=True )
def register_company():
    try:
        data = frappe.local.form_dict
        company_name = data.get("company_name")
        gst_number = data.get("gst_number")
        company_type = data.get("company_type")
        user_name = data.get("user_name")
        email = data.get("email")
        mobile = data.get("mobile")
        password = data.get("password")
        gst_category = data.get("gst_category")
        designation = data.get("designation")
        occupation = data.get("occupation")
        space_id = data.get("space_id")
        date_of_birth = data.get("date_of_birth")
        vehicle_number = data.get("vehicle_number")
        about  = data.get("about")



        if frappe.db.exists("Customer", {"gstn": gst_number}):
            return {
                "success_key": 0,
                "error": "Company with GST number already registered"
            }
        if frappe.db.exists("Customer Employees", {"email": email}):
            return {
                "success_key": 0,
                "error": "User email already registered, please login"
            }
        if frappe.db.exists("Customer Employees", {"mobile": mobile}):
            return {
                "success_key": 0,
                "error": "Mobile number already registered, please login"
            }
        # create customer
        customer = frappe.new_doc("Customer")
        customer.customer_name = company_name
        customer.gstin = gst_number
        customer.gst_category = gst_category
        customer.customer_type = company_type
        customer.custom_space = space_id
        customer.custom_credit_balance = 10
        customer.customer_details = about
        customer.save(ignore_permissions=True)
        frappe.db.commit()
        
        # create user
        employee = frappe.new_doc("Customer Employees")
        employee.full_name = user_name
        employee.email = email
        employee.password = password
        employee.customer = customer.name
        employee.mobile = mobile
        employee.status = "Active"
        employee.occupation = occupation
        employee.designation = designation
        employee.date_of_birth = date_of_birth
        employee.vehicle_number = vehicle_number
        employee.save(ignore_permissions=True)
        frappe.db.commit()


        # set user as admin
        frappe.db.set_value("Customer Employees", {"email": email}, "is_admin", 1)
        frappe.db.commit()

        return {
            "message": "Company registered successfully",
            "success_key": 1
        }
    except Exception as e:
        # Rollback in case of error to avoid partial creation
        frappe.log_error(frappe.get_traceback(), ("Failed to register company"))
        return {
            "success_key": 0,
            "error": str(e)
        }
