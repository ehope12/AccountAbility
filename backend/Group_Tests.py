# Group_Tests.py

from Users import User
from Group import Group
from Merchants import Merchant, get_merchants

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
url = f"http://api.nessieisreal.com/data?type=Purchases&key={api_key}"
response = requests.delete(
    url,
    headers={'Content-Type': 'application/json'}
)

user1 = User("emhopeh", "Emily", "Hsieh", "test", ["1212", "N Marion St", "Oak Park", "IL", "60302"], 1000000)
user2 = User('asitabk', 'Adam', 'Sitabkhan', 'test', ('4820','Oakwood Ave','Downers Grove','IL','60515'), 1000)
user3 = User('abadde', 'Aditi', 'Badde', 'test', ('Somewhere','In','Thailand','IL','90210'), 15000000)
user4 = User('dwuert', 'David', 'Wuertzer', 'test', ('501','E Healey St','Champaign','IL','61820'), 360)

m1 = Merchant('Starbucks', 'cafe', ('snum', 'sname', 'town', 'IL', '60000'))
m2 = Merchant('Denny\'s', 'restaurant', ('snum', 'sname', 'town', 'IL', '60000'))
m3 = Merchant('TikTok Shop', 'brainrot', ('snum', 'sname', 'town', 'IL', '60000'))
m6 = Merchant('Mr. Peanut', 'peanuts', ('snum', 'sname', 'town', 'IL', '60000'))
m7 = Merchant('Yummy Future', 'coffee', ('snum', 'sname', 'town', 'IL', '60000'))
m8 = Merchant('Chipotle', 'restaurant', ('snum', 'sname', 'town', 'IL', '60000'))
m9 = Merchant('Bao Central', 'chinese', ('snum', 'sname', 'town', 'IL', '60000'))

group = Group('squad')
group.addUser(user1)
group.addUser(user2)
group.addUser(user3)
group.addUser(user4)

group.updateCommitmentInfo('emhopeh', pot_share=20, spend_limit=50, merchants=['Starbucks', 'Yummy Future'], categories=['cafe'])
group.updateCommitmentInfo('asitabk', pot_share=30, spend_limit=100, categories=['restaurant'])
group.updateCommitmentInfo('abadde', pot_share=100, spend_limit=1500, merchants=['TikTok Shop'], categories=['online'])
group.updateCommitmentInfo('dwuert', pot_share=10, spend_limit=200, merchants=['Mr. Peanut'], categories=['Mexican'])

print(group.hasValidCommitments())

# print(m1.get_merchant_id())
user1.make_purchase(999990, m1.get_merchant_id())
print(user1.get_accounts())
# print(user1.get_purchases())





