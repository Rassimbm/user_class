class User:
    def __init__(self, fname, lname, email, age):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

user_1 = User("Rassim", "Benmhamed", "rassimb@ninja.com", 35)
print(user_1)