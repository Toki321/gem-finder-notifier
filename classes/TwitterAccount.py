import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

import requests
from helpers.tweepyClient import getTweepyClient
import os
from classes.ToFollowAccount import ToFollowAccount

client = getTweepyClient()


class TrackedTwitterAccount:
    def __init__(self, id):
        self.id = id
        self.userObject = client.get_user(id=id)

    # Function for getting following list here
    def getListFollowingIds(self):
        return client.get_users_following(self.id)

    # Function to return what is not in list1 but is in list2, input is list2 and list1 we read from file
    def getNewFollows(self, nameListOld, nameListNew):
        return list(set(nameListNew) - set(nameListOld))

    # Function to get usernames of follows
    def getListUsernameFollows(self):
        index = 0
        nameList = []
        followingList = self.getListFollowingIds()
        if followingList.data != None:
            for x in followingList.data:
                nameList.append(str(followingList.data[index]))
                index += 1

        return nameList

    # Function to  write a list to a txt file
    def writeToFile(self, followingListIds):
        fileName = "./text-files/" + self.id + ".txt"

        with open(fileName, "w") as f:
            for id in followingListIds:
                f.write(id + "\n")
        f.close()

    # Function to read a file and extract ids to a list
    def extractIdsFromFile(self):
        fileName = "./text-files/" + self.id + ".txt"

        with open(fileName, "r") as f:
            lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]

        numbers = [line for line in lines]
        return numbers

    def getCheckedNewFollows(newFollows):
        checkedNewFollows = []
        for username in newFollows:
            toFollowAccount = ToFollowAccount(username)
            if toFollowAccount.checkConditions() == True:
                checkedNewFollows.append(toFollowAccount)

        return checkedNewFollows

    # Function to send telegram message
    def sendTelegramMessage(self, newFollows):
        TOKEN = os.getenv("TELEGRAM_TOKEN")
        CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        usernameOfTrackedAccount = self.userObject.data["username"]
        nameOfTrackedAccount = self.userObject.data["name"]
        print("\n")
        for account in newFollows:
            print(f"to follow for {usernameOfTrackedAccount}:", account.username)
            MESSAGE = (
                f"https://twitter.com/{usernameOfTrackedAccount} ({nameOfTrackedAccount})"
                + " has followed "
                + f"https://twitter.com/{account.username} ({newFollows.fullName})"
            )
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
            requests.get(url).json()

    # Function for getting number of $TIKS mentioned for 2 dates input (timeframe)
