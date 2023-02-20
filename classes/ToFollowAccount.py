import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")
from helpers.tweepyClient import getTweepyClient
from helpers.substackCheck import isSubstackContainedInString
from helpers.isUrlContained import isUrlContainedInString
from helpers.nftCheck import isNftContainedInString

client = getTweepyClient()


class ToFollowAccount:
    def __init__(self, username) -> None:
        self.username = username
        self.userObject = client.get_user(
            username=self.username, user_fields="entities,description"
        )
        self.fullName = self.userObject.data["name"]

    # Check everything (url, substack url and nft in name), true if all good false if bad
    def checkConditions(self):
        if self.isSubstackContainedInUrls() == False and self.isNftInName() == False:
            return True
        return False

    # Substack and url check
    def isSubstackContainedInUrls(self):
        # If this function returns true then this acc will be discarded that is why if url isnt present we return True
        if self.isUrlPresent() == False:
            return True

        bio = self.userObject.data.description

        # Check if bio url is substack
        if self.isBioUrlPresent():
            if isSubstackContainedInString(bio) == True:
                return True

        entities = self.userObject.data.entities

        # Check if url in section is substack
        if entities != None:
            print(entities)
            try:
                url = entities["url"]["urls"][0]["expanded_url"]
                print(url)
                if isSubstackContainedInString(url) == True:
                    return True
            except KeyError:
                if self.isBioUrlPresent() == False:
                    return True

        return False

    # Check if links exist in bio
    def isBioUrlPresent(self):
        bio = self.userObject.data.description
        if isUrlContainedInString(bio):
            return True
        else:
            return False

    # Check if url section exists
    def checkEntitiesUrl(self):
        entities = self.userObject.data.entities
        if entities == None:
            return False
        else:
            return True

    # Check if url anywhere exists
    def isUrlPresent(self):
        if self.checkEntitiesUrl() == False or self.isBioUrlPresent() == False:
            return True
        else:
            return False

    # Check if nfts in username
    def isNftInName(
        self,
    ):  # false if no NFT, true if there is NFT word in username / name
        if isNftContainedInString(self.username) or isNftContainedInString(
            self.fullName
        ):
            return True
        else:
            return False
