class User:
    def __init__(self, fname, lname, email, age):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_user_infos(self):
        print("==============")
        print(f"Full name: {self.fname} {self.lname} \nEmail: {self.email} \nAge: {self.age} \nMembeership tatus: {self.is_rewards_member} \nRewards card points: {self.gold_card_points}")
        print("--------------")
        return self
    
    def enroll(self):
        if self.is_rewards_member:
            print(f"User already a member.")
            return self
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            return self
        print(f"Not enough points to spend at this time!")
        


user_1 = User("Rassim", "Benmhamed", "rassimb@ninja.com", 35)
user_2 = User("Sadie", "Flick", "sadief32@ninja.com", 32)
user_1.display_user_infos().enroll().display_user_infos().spend_points(50).display_user_infos()
user_2.display_user_infos().enroll().display_user_infos().spend_points(80).display_user_infos()

