class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Abhay")
user2 = User("002", "Ansh")


user1.follow(user2)

print(f"{user1.id} {user1.username} follower : {user1.followers} & following : {user1.following}")
print(f"{user2.id} {user2.username} follower : {user2.followers} & following : {user2.following}")