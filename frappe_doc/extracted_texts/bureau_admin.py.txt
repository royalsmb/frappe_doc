# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class BureauAdmin(Document):
    def validate(self):
        self.validate_user()
    def validate_user(self):
            """Create a System user for Agent creation if not already exists"""
            if not frappe.db.exists("User", self.email):
                agent_user = frappe.get_doc({
					"doctype": "User",
					"first_name": self.first_name,
					"last_name": self.last_name,
                    "username": self.username,
					"email": self.email,
					"gender": self.gender,
					"send_welcome_email": 0,
					"user_type": "System User",
				})
                agent_user.add_roles("Bureau Admin", "HR Manager", "Analytics", "Accounts Manager", "Sales Manager", "Purchase Manager")
                agent_user.save(ignore_permissions=True)
    def on_update(self):
           user_doc = frappe.get_doc("User", self.email)
           user_doc.first_name =  self.first_name
           user_doc.last_name = self.last_name
           user_doc.gender = self.gender
           
           user_doc.save(ignore_permissions=True)
                
    def on_trash(self):
                frappe.delete_doc("User", self.email)
        # def on_update(self):
        #       full_name = self.first_name + " " + self.last_name
        #       self.db_set("full_name", full_name)
        
                
        
