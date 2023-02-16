from TwitterAccount import TrackedTwitterAccount

# create a TwitterAccount object
account = TrackedTwitterAccount("1449328468227932163")

# call the getListFollowingIds() function and store the result in a variable

userNameList = account.getListUsername()

account.writeToFile(userNameList)

oldList = account.extractIdsFromFile()
