import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")


from classes.TwitterAccount import TrackedTwitterAccount
from helpers.idsToTrack import readIds

idsToTrack = readIds()

accountsToTrack = []

for id in idsToTrack:
    account = TrackedTwitterAccount(id)
    accountsToTrack.append(account)

    usernameList = account.getListUsernameFollows()
    account.writeToFile(usernameList)
