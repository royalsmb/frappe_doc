import frappe
from frappe import request, _, throw
import inspect
from frappe.exceptions import ValidationError


@frappe.whitelist(allow_guest=True)
def check_bruno_decorator():
    """
    A before_request hook that checks for the @bruno decorator and HTTP method.
    """
    endpoint = request.path
    
        
    
    # chek if app is install 
    installed_apps = frappe.get_installed_apps()
    if endpoint[len("/api/method/"):].split(".")[0] in installed_apps:
        method_path = endpoint[len("/api/method/"):]
        
        app_name = method_path.split(".")[0]

        if endpoint.startswith(f"/api/method/{app_name}") and app_name in installed_apps:
            module_name, function_name = method_path.rsplit('.', 1)
            # Dynamically import the module
            module = __import__(module_name, fromlist=[function_name])
            func = getattr(module, function_name)
        
            
            if hasattr(func, '_bruno_doc'):
                # It's a Bruno-decorated function
                expected_method = func._bruno_doc.get("method", "get").upper()  # Default to POST

                if str(request.method) != str(expected_method):
                    frappe.local.form_dict.clear()
                    frappe.local.response.update({
                        "http_status_code": 405,
                        "error": f"Method not allowed. Expected {expected_method}."
                    })
                    throw(f"Method not allowed. Expected {expected_method}.")
                    
                    

            
            


