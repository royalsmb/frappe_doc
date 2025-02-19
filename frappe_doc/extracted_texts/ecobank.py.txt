import requests
import json
import frappe

base_url = "https://developer.ecobank.com"
@frappe.whitelist()
def get_access_token():
    url = f"{base_url}/corporateapi/user/token"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "origin": "developer.ecobank.com"

    }
    body = {
        "userId": get_site_config().get("userid"),
        "password": get_site_config().get("password"),
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    token = response.json()
    return token

@frappe.whitelist()
def get_site_config():
    userid = frappe.local.conf.ecobank.get('user_id')
    password = frappe.local.conf.ecobank.get('password')
    return {
        "userid": userid,
        "password": password
    }
@frappe.whitelist()
def get_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "origin": "developer.ecobank.com",
        "Authorization": f"Bearer {get_access_token().get('token')}"
    }
@frappe.whitelist()
def get_account_balance():
    url = f"{base_url}/corporateapi/merchant/accountbalance"
    headers = get_headers()
    data = {
        "requestId": "14232436312",
        "affiliateCode": "EGH",
        "accountNo": "6500184371",
        "clientId": "ECO00184371123",
        "companyName": "ECOBANK TEST CO",
        "secureHash": "7cf1b1f6e1cce663de5cac528fa1f69ccf06b8cbe5263a412b341caa2a787198185921ca71cb1fa1ef04731726068202588955195f313b022a7d25b095fdc28f"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    #return status code
    return response.json()