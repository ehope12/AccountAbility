# Group.py

from Users import User    
from Merchants import Merchant


class Commitment():
    def __init__(self, pot_share=0, spend_limit=0, merchants=[], categories=[]):
        self.pot_share = pot_share # Contribution to pot
        self.spend_limit = spend_limit # Spending limit
        self.merchants = set(merchants) # Merchants to track
        self.categories = set(categories) # Categories to track
        
        self.num_purchases = 0
        self.status = True
        
    def updateInfo(self, pot_share=None, spend_limit=None, merchants=None, categories=None):
        # Update commitment info
        if pot_share:
            self.pot_share = pot_share
        if spend_limit:
            self.spend_limit = spend_limit
        if merchants:
            self.merchants = set(merchants)
        if categories:
            self.categories = set(categories)
   

class Group():
    curr_name_ids = {}
    
    def __init__(self, name : str):
        self.name = name # Group name
        self.users = {}
        self.commitments = {}
        self.pot = 0
        
        if name not in Group.curr_name_ids.keys():
            Group.curr_name_ids[name] = 0
        self.id = f"{name}-{Group.curr_name_ids[name]:04}"
        Group.curr_name_ids[name] += 1
    
    def addUser(self, user : User):
        if user.username in self.users.keys():
            print(f"User {user.username} is already in group {self.name}.")
            return
        self.users[user.username] = user
        self.commitments[user.username] = Commitment()
        
    def removeUser(self, username):
        return 
    
    def updateCommitmentInfo(self, username, pot_share=None, spend_limit=None, merchants=None, categories=None):
        self.commitments[username].update(pot_share, spend_limit, merchants, categories)
        if pot_share:
            self.pot = sum([c.pot_share for c in self.commitments.values()])
        
    def updateCommitmentStatus(self, username):
        purchases = self.users[username].get_purchases()
        self.commitments[username].num_purchases = len(purchases)
        
        for p in purchases:
            merchant_id = p['merchant_id']
            merchant = Merchant()
            
            amount = p['amount']
            
            
            
        
        return
        
    def hasValidCommitments(self) -> bool:
        for u, cmt in self.commitments.items():
            if cmt.pot_share <= 0 or cmt.spend_limit <= 0 or (len(cmt.merchants) == 0 and len(cmt.categories) == 0):
                return False
        return True


def main():
    user1 = User('Emily', 'helloo', 'a')
    user2 = User('Adam', 'hiiii', 'b')
    user3 = User('Aditi', 'haiiii', 'c')
    user4 = User('David', 'hey.', 'd')
    
    group1 = Group('squad')
    group1.addUser(user1)
    group1.addUser(user2)
    group1.addUser(user3)
    group1.addUser(user4)
    
    group1.updateCommitment('Emily', pot_share=20, spend_limit=50, merchants=['Starbucks', 'Yummy Future'])
    group1.updateCommitment('Adam', pot_share=30, spend_limit=100, categories=['Restaurants'])
    group1.updateCommitment('Aditi', pot_share=100, merchants=['TikTok Shop'])
    group1.updateCommitment('David', pot_share=10, spend_limit=200)

    group2 = Group('squad')
    print(f'Group ID: {group2.id}')

    print(f'Group ID: {group1.id}')
    print(f'Pot: {group1.pot}')
    print(f'Are commitments valid? {group1.hasValidCommitments()}')
    
    group1.updateCommitment('David', merchants=['Mr. Peanut'])
    group1.updateCommitment('Aditi', spend_limit=1500)
    print(f'Are commitments valid? {group1.hasValidCommitments()}')


if __name__ == "__main__":
    main()
        
        
    