class User:
    def __init__(self, id="0", username=""):

        print("new user being created....")
        self.id = id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.following += 1
        self.following += 1


user_1 = User("001", "jack")
user_2 = User()
print(user_2.id)
