class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(1, "Alice")
user2 = User(2, "Bob")
#print(user1.id, user1.name)
#print(user2.id, user2.name)
#print(user1.followers)

user1.follow(user2)
print(user1.following)
print(user2.followers)