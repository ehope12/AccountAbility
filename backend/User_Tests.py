import Users
import Merchants
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("API_KEY")

# Clear the environment
url = f"http://api.nessieisreal.com/data?type=Customers&key={api_key}"
response = requests.delete(
    url,
    headers={'Content-Type': 'application/json'}
)
url = f"http://api.nessieisreal.com/data?type=Merchants&key={api_key}"
response = requests.delete(
    url,
    headers={'Content-Type': 'application/json'}
)

emily = Users.User("emhopeh", "Emily", "Hsieh", "test", ["1212", "N Marion St", "Oak Park", "IL", "60302"], 1000000)
# print(emily.get_accounts())
# print(Merchants.get_merchants())
emily.make_purchase(10, "67c3a9d09683f20dd518c690")
# print(emily.get_purchases())
print(emily.get_num_purchases())