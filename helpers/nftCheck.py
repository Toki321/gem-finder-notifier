from helpers.tweepyClient import getTweepyClient

client = getTweepyClient()


def checkStringForNft(string):  # true if there is nft word, false if not
    str1 = "nfts"
    str2 = "nft"
    str3 = "NFT"
    str4 = "NFTs"

    if str1 in string or str2 in string or str3 in string or str4 in string:
        return True
    else:
        return False


def checkNftUsernames(
    oneAccount,
):  # false if no NFT, true if there is NFT word in username / name
    user = client.get_user(username=oneAccount)
    usName = oneAccount
    fullName = user.data["name"]

    if checkStringForNft(usName) or checkStringForNft(fullName):
        return True
    else:
        return False
