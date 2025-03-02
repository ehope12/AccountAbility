# Group_Tests.py

from Users import User
from Group import Group
from Merchants import Merchant

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

user1 = User("emhopeh", "Emily", "Hsieh", "test", ["1212", "N Marion St", "Oak Park", "IL", "60302"], 1000000)
user2 = User('asitabk', 'Adam', 'Sitabkhan', 'test', ('4820','Oakwood Ave','Downers Grove','IL','60515'), 1000)
user3 = User('abadde', 'Aditi', 'Badde', 'test', ('Somewhere','In','Thailand','IL','90210'), 15000000)
user4 = User('dwuert', 'David', 'Wuertzer', 'test', ('501','E Healey St','Champaign','IL','61820'), 360)

Merchant('Starbucks', ['coffee', 'cafe', 'latte'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('Denny\'s', ['restaurant'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('TikTok Shop', ['online', 'brainrot'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('Mr. Peanut', ['peanuts', 'nuts'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('Yummy Future', ['coffee', 'cafe', 'robots'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('Chipotle', ['restaurant', 'mexican'], ('snum', 'sname', 'town', 'state', 'zip'))
Merchant('Bao Central', ['chinese', 'super yummy'], ('snum', 'sname', 'town', 'state', 'zip'))

group = Group('squad')
group.updateCommitmentInfo('emhopeh', pot_share=20, spend_limit=50, merchants=['Starbucks', 'Yummy Future'])
group.updateCommitmentInfo('asitabk', pot_share=30, spend_limit=100, categories=['restaurant'])
group.updateCommitmentInfo('abadde', pot_share=100, spend_limit=1500, merchants=['TikTok Shop'])
group.updateCommitmentInfo('dwuert', pot_share=10, spend_limit=200, merchants=['Mr. Peanut'], categories=['Mexican'])





