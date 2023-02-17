def isNftContainedInString(string):  # true if there is nft word, false if not
    str1 = "nfts"
    str2 = "nft"
    str3 = "NFT"
    str4 = "NFTs"

    if str1 in string or str2 in string or str3 in string or str4 in string:
        return True
    else:
        return False
