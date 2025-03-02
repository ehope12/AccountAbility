import requests
import json
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()
api_key = os.getenv("API_KEY")

"""
Function to return all merchants in the database.
"""
def get_merchants():
    url = f"http://api.nessieisreal.com/merchants?key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print('ERROR: ', response.json())
        return
    return response.json()

"""
Defines a Merchant class which represents a merchant in the database.
Each merchant has a name, category, and address.
"""
class Merchant:
    def __init__(self, name, category, address):
        self.name = name.upper()  # String :: Name of merchant
        self.category = category.upper()  # String :: Category of merchant
        street_number, street_name, city, state, zip_code = address  # List[String] :: Address of merchant

        # Create a Merchant
        url = f"http://api.nessieisreal.com/merchants?key={api_key}"
        payload = {
            "name": self.name,
            "category": self.category,
            "address": {
                "street_number": street_number,
                "street_name": street_name.upper(),
                "city": city.upper(),
                "state": state.upper(),  # 2-letter state abbreviation
                "zip": zip_code
            },
            "geocode": {  # TODO: Edit this later
                "lat": 0,
                "lng": 0
            }
        }
        response = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'},
            )
        if response.status_code != 201:
            print('ERROR: ', response.json())
            return
        self.merchant_id = response.json()["objectCreated"]["_id"]

    def get_merchant_info(self):
        url = f"http://api.nessieisreal.com/merchants/{self.merchant_id}?key={api_key}"
        response = requests.get(url)
        if response.status_code != 200:
            print('ERROR: ', response.json())
            return
        return response.json()