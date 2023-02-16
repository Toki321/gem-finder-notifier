from ToFollowAccount import ToFollowAccount

account = ToFollowAccount("0xToki")

user = account.getUserObject()

bio = user.data.description
print(user)

print(bio)
