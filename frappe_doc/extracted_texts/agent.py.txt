# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Agent(Document):
        def validate(self):
                self.validate_user()
                self.create_employee()
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
                agent_user.add_roles("Agent")
                agent_user.save(ignore_permissions=True)

        def on_update(self):
           user_doc = frappe.get_doc("User", self.email)
           user_doc.first_name =  self.first_name
           user_doc.last_name = self.last_name
           user_doc.gender = self.gender
           
           user_doc.save(ignore_permissions=True)

        def on_trash(self):
                user = frappe.db.set_value("User", self.email, "enabled", 0)
                
        #create an employee for the agent
        def create_employee(self):
            if not frappe.db.exists("Employee", self.email):
                employee = frappe.get_doc({
                    "doctype": "Employee",
                    "employee_name": self.first_name,
                    "user_id": self.email,
                    "status": "Active",
                    "designation": "Agent",
                    "date_of_joining": self.date_of_joining,
                    "date_of_birth": self.date_of_birth
                })
                employee.insert()
                frappe.msgprint("Employee created successfully")
        