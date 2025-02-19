# Copyright (c) 2024, Erpera and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CourtSchedule(Document):
	def validate(self):
		pass
		# Check if the court schedule is already booked
		# if self.is_new():
		# 	booked = frappe.db.exists("Court Schedules", {
		# 		"court_number": self.court_number,
		# 		"date": self.date,
		# 		"time": self.time
		# 	})
		# 	if booked:
		# 		frappe.throw("Court is already booked for the selected date and time")