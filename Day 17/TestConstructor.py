class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user1 = User("001", "Abhay")
user2 = User("002", "Verma")

print(user1.id )
print(user1.username )
print(user1.followers    )