import requests
import json

app_id = '5cdfec9685174a94bf7d05b401154981'
oxr_url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"

# Open a session and retrieve data
response = requests.get(oxr_url)

if response.status_code == 200:
    oxr_latest = json.loads(response.text)

    base_currency = 'GMD'
    gmd_to_usd_rate = 1 * oxr_latest['rates']['GMD']  # Calculate the GMD to USD rate

    # Define a list of target currencies
    target_currencies = ['USD', 'GBP', 'EUR', 'XOF']  # Add more currencies as needed

    # Print the equivalent of 1 unit of each currency in GMD with 2 decimal places
    for target_currency in target_currencies:
        rate = round(gmd_to_usd_rate / oxr_latest['rates'][target_currency], 2)    
        print(f"1 {target_currency} equals {rate} {base_currency}")
else:
    print(f"Error: {response.status_code} - {response.text}")
