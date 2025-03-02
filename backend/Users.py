import requests
import json
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()
api_key = os.getenv("API_KEY")

"""
Defines a User class which represents a user of the application.
A user has a unique username and a password.
Upon initialization, a user is given a checkings account with a balance that they choose.
    This is their AccountAbility account to encourage good spending habits.
A user is allowed to add additional accounts if they so choose.
A user can make purchases at any of the available merchants.
A user is also able to view all of their purchases.
"""
class User:
    def __init__(self, username, firstname, lastname, password, address, balance):
        self.username = username
        self.firstname = firstname.upper()  # String :: First name of user
        self.lastname = lastname.upper()  # String :: Last name of user
        self.password = password  # String :: Password of user
        street_number, street_name, city, state, zip_code = address  # List[String] :: Address of user
        self.group_ids = set()
        self.balance = balance
        self.num_purchases = 0
        
        # Create a Customer
        url = f"http://api.nessieisreal.com/customers?key={api_key}"
        payload = {
            "first_name": self.firstname,
            "last_name": self.lastname,
            "address": {
                "street_number": street_number,
                "street_name": street_name.upper(),
                "city": city.upper(),
                "state": state.upper(),  # 2-letter state abbreviation
                "zip": zip_code
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
        self.customer_id = response.json()["objectCreated"]["_id"]
        
        # Create a Checking Account
        url = f'http://api.nessieisreal.com/customers/{self.customer_id}/accounts?key={api_key}'
        payload = {
            "type": "Checking",
            "nickname": self.firstname + self.lastname + "AccountAbility",
            "rewards": 0,
            "balance": balance,  # Float :: Initial balance of account
        }
        response = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'},
            )
        if response.status_code != 201:
            print('ERROR: ', response.json())
            return
        self.primary_account_id = response.json()["objectCreated"]["_id"]
    
    def make_purchase(self, amount, merchant_id, account_id=None):
        # Make a purchase of "amount" at the provided merchant_id
        if account_id is None:
            account_id = self.primary_account_id
            
        # POST purchase data
        url = f'http://api.nessieisreal.com/accounts/{account_id}/purchases?key={api_key}'
        payload = {
            "merchant_id": merchant_id,
            "medium": "balance",
            "purchase_date": "2025-03-02",
            "amount": amount,
            "status": "completed",
            "description": "string"
        }
        response1 = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'},
            )
        if response1.status_code != 201:
            print('ERROR1: ', response1.json())
            return response1.status_code
        
        # # GET account data
        # url = f'http://api.nessieisreal.com/accounts/{account_id}?key={api_key}'
        # response2 = requests.get( 
        #     url,
        #     headers={'content-type':'application/json'},
        #     )
        # if response2.status_code != 200:
        #     print('ERROR2: ', response2.json())
        #     return response2.status_code
        
        # # PUT account data
        # payload = response2.json()
        # payload['balance'] -= amount
        # print(payload)
        # response3 = requests.put( 
        #     url, 
        #     data=json.dumps(payload),
        #     headers={'content-type':'application/json'},
        #     )
        # if response3.status_code != 202:
        #     print('ERROR3: ', response3.json())
        #     return response3.status_code
        
        self.balance -= amount
        self.num_purchases += 1
        return
    
    def get_purchases(self, account_id=None):
        # Get all purchases made by the user
        if account_id is None:
            account_id = self.primary_account_id
        url = f'http://api.nessieisreal.com/accounts/{account_id}/purchases?key={api_key}'
        response = requests.get( 
            url, 
            headers={'content-type':'application/json'},
            )
        if response.status_code != 200:
            print('ERROR: ', response.json())
            return
        return response.json()
    
    def make_account(self, account_type, nickname, rewards, balance):
        # Make a new account of "account_type" with the provided nickname, rewards, and balance
        url = f'http://api.nessieisreal.com/customers/{self.customer_id}/accounts?key={api_key}'
        payload = {
            "type": account_type,  # String :: Type of account (Checking, Savings, Credit Card, etc.)
            "nickname": nickname,  # String :: Nickname of account
            "rewards": rewards,  # Float :: Rewards of account
            "balance": balance,  # Float :: Initial balance of account
        }
        response = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'},
            )
        if response.status_code != 201:
            print('ERROR: ', response.json())
            return response.status_code
        return response.status_code

    def get_accounts(self):
        # Get all accounts associated with the user
        url = f'http://api.nessieisreal.com/customers/{self.customer_id}/accounts?key={api_key}'
        response = requests.get( 
            url, 
            headers={'content-type':'application/json'},
            )
        if response.status_code != 200:
            print('ERROR: ', response.json())
            return
        return response.json()
    
    def delete_account(self, account_id):
        # Delete the account with the provided account_id
        url = f'http://api.nessieisreal.com/accounts/{account_id}?key={api_key}'
        response = requests.delete( 
            url, 
            headers={'content-type':'application/json'},
            )
        if response.status_code != 204:
            print('ERROR: ', response.json())
            return response.status_code
        return response.status_code
    
    def add_group_id(self, group_id):
        # Add a group_id to the user's set of group_ids
        self.group_ids.add(group_id)
    
    def remove_group_id(self, group_id):
        # Remove a group_id from the user's set of group_ids
        self.group_ids.remove(group_id)
    
    def get_group_ids(self):
        # Return the user's set of group_ids
        return self.group_ids
    
    def get_num_purchases(self):
        # Return the number of purchases made by a user
        return self.num_purchases