import os.path
from TwitterAccount import TrackedTwitterAccount


def readIds():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../idsToTrack.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()
        toTrackIdList = []
        i = 0
        for line in lines:
            toTrackIdList.append(line.split()[-1])
            i += 1
            if i == 14:
                break
        return toTrackIdList


def createToTrackList():
    list = []
    idsToTrack = readIds()
    for id in idsToTrack:
        account = TrackedTwitterAccount(id)
        list.append(account)
    return list
