from helpers.tweepyClient import getTweepyClient

client = getTweepyClient()


class TrackedTwitterAccount:
    def __init__(self, id):
        self.id = id

    # Function for getting following list here
    def getListFollowingIds(self):
        return client.get_users_following(self.id)

    # Function to return what is not in list1 but is in list2, input is list2 and list1 we read from file
    def getNewFollows(self, oldFollowingList, newFollowingList):
        nameListOld = self.getListUsername(oldFollowingList)
        nameListNew = self.getListUsername(newFollowingList)

        return list(set(nameListNew) - set(nameListOld))

    # Function to get usernames of follows
    def getListUsername(self):
        index = 0
        nameList = []
        followingList = self.getListFollowingIds()
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

    # Function to read a file and extract ids to a list
    def extractIdsFromFile(self):
        fileName = "./text-files/" + self.id + ".txt"

        with open(fileName, "r") as f:
            lines = f.readlines()

        lines = [line.strip() for line in lines]

        numbers = [line for line in lines]
        return numbers

    # Function to send telegram message

    # Function for getting number of $TIKS mentioned for 2 dates input (timeframe)


class FollowerAccount:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
