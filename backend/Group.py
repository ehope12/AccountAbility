# Group.py


# temporary for testing
class User():
    def __init__(self, username, password, account_id):
        self.username = username
        self.password = password
        self.account_id = account_id
        

class Commitment():
    def __init__(self, pot_share=0, spend_limit=0, merchants=[], categories=[]):
        self.pot_share = pot_share # Contribution to pot
        self.spend_limit = spend_limit # Spending limit
        self.merchants = set(merchants) # Merchants to track
        self.categories = set(categories) # Categories to track
        self.status = True
        
    # def __str__(self):
    #     return f"Commitment(pot_share={self.pot_share}, spend_limit={self.spend_limit}, merchants={self.merchants}, categories={self.categories})"
    
    def update(self, pot_share=None, spend_limit=None, merchants=None, categories=None):
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
    
    def updateCommitment(self, username, pot_share=None, spend_limit=None, merchants=None, categories=None):
        self.commitments[username].update(pot_share, spend_limit, merchants, categories)
        if pot_share:
            self.updatePot()
    
    def updatePot(self):
        self.pot = sum([c.pot_share for c in self.commitments.values()])
        
    def updateCommitmentStatus(self, username):
        # This should check User object for conflicts with commitment
        return
        
    def areCommitmentsValid(self) -> bool:
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
    group1.updateCommitment('Aditi', pot_share=100, spend_limit=1500, merchants=['TikTok Shop'])
    group1.updateCommitment('David', pot_share=10, spend_limit=200)

    print(f'Group ID: {group1.id}')
    print(f'Pot: {group1.pot}')
    print(f'Are commitments valid? {group1.areCommitmentsValid()}')
    
    group1.updateCommitment('David', merchants=['Mr. Peanut'])
    print(f'Are commitments valid? {group1.areCommitmentsValid()}')


if __name__ == "__main__":
    main()
        
        
    