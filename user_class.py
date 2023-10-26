class User:
    def __init__(self, fname, lname, email, age):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_user_infos(self):
        user_infos = f'''
        Full name: {user_1.fname} {user_1.lname}
        Email: {user_1.email}
        Age: {user_1.age}
        Membeership tatus: {user_1.is_rewards_member}
        Rewards card points: {user_1.gold_card_points}
        '''
        return user_infos
    
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200


user_1 = User("Rassim", "Benmhamed", "rassimb@ninja.com", 35)
print(user_1.display_user_infos())
user_1.enroll()
print(user_1.is_rewards_member)
