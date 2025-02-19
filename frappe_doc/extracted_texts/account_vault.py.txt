# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AccountVault(Document):
	def validate(self):
		self.set_bureau()
	#set the auto name
	def autoname(self):
		self.name = self.account_vault_name + " - " + self.branch or ''
		
	#get user
	def set_bureau(self):
		user = frappe.session.user
		user_email = frappe.db.get_value("User", user, "email")
		bureau = frappe.get_list("Bureau", filters={'email': user_email}, fields=['name'])
		self.bureau = bureau[0].name
	
	@frappe.whitelist()
	def get_account_vaults_for_bureau_admin(user):
		#check if user is a bureau admin or agent
		user = frappe.get_doc("User", user)
		user_email = frappe.db.get_value("User", user, "email")
		bureau = frappe.get_list("Bureau", filters={'email': user_email}, fields=['name'])
		return frappe.get_list("AccountVault", filters={'bureau': bureau[0].name}, fields=['name', 'account_vault_name', 'branch', 'account_vault_type', 'account_vault_balance'])

	@frappe.whitelist()
	def get_account_vaults_for_branch_admin(user):
		#check if user is a branch admin or agent
		user = frappe.get_doc("User", user)
		agent  = frappe.get_doc("Agent", user)
		return frappe.get_list("AccountVault", filters={'branch': branch[0].name}, fields=['name', 'account_vault_name', 'branch', 'account_vault_type', 'account_vault_balance'])