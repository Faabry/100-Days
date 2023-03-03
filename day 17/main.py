class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0


    def follow(self, user):
        # The user whose is gonna be followed will increase the number of
        # followers in 1
        user.followers += 1

        # The self user is gonna be increased the number of 
        # following accounts in 1
        self.following += 1


# Creating the users
user1 = User("001", "Josias")
user2 = User("002", "Cabrunquito")


user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)