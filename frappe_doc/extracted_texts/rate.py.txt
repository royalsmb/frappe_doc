# Copyright (c) 2023, Momodou khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json

class Rate(Document):
    def on_submit(self):
        self.update_rate()
    def update_rate(self):
        app_id = '5cdfec9685174a94bf7d05b401154981'
        oxr_url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
        response = requests.get(oxr_url)

        target_currencies = ['USD', 'GBP', 'EUR', 'XOF']
        for target_currency in target_currencies:
                currency = frappe.get_doc('Currency', target_currency)
                if response.status_code == 200:
                        oxr_latest = json.loads(response.text)
                        base_currency = 'GMD'
                        gmd_to_usd_rate = 1 * oxr_latest['rates']['GMD']  # Calculate the GMD to USD rate
                        rate = round(gmd_to_usd_rate / oxr_latest['rates'][target_currency], 2)
                        currency.rate = rate
                        currency.save()
                         
				


