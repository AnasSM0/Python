class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0 
        


user1 = User(1, "Alice")
user2 = User(2, "Bob")
print(user1.id, user1.name)
print(user2.id, user2.name)
print(user1.followers)