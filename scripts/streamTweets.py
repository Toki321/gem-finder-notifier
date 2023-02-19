import threading
import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

from classes.TweetStreamer import TweetStreamer
from helpers.idsToTrack import readIds

listAllAccounts = readIds()
listAccountsOne = []
listAccountsTwo = []
listAccountsThree = []

i = 0
for id in listAllAccounts:
    if i <= 14:
        listAccountsOne.append(id)
    if i >= 14 and i < 30:
        listAccountsTwo.append(id)
    if i > 30:
        listAccountsThree.append(id)
    i += 1

print(len(listAccountsOne))
print(len(listAccountsTwo))
print(len(listAccountsThree))


# listAccountsOne.append("2966287497")
listAccountsTwo.append("2966287497")

streamerOne = TweetStreamer(listAccountsOne, listAccountsTwo, listAccountsThree)

streamerOne.startStreaming()
# streamerTwo = TweetStreamer(listAccountsTwo)
