from TwitterAccount import TrackedTwitterAccount
from helpers.idsToTrack import readIds

idsToTrack = readIds()

accountsToTrack = []

for id in idsToTrack:
    account = TrackedTwitterAccount(id)
    accountsToTrack.append(account)

    usernameList = account.getListUsernameFollows()
    account.writeToFile(usernameList)
