import itertools
import os.path
from TwitterAccount import TrackedTwitterAccount


# Read first 15 ids
def readIds():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../idsToTrack.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()
        toTrackIdList = [line.split()[-1] for line in itertools.islice(lines, 15)]
        return toTrackIdList


def createToTrackList():
    list = []
    idsToTrack = readIds()
    for id in idsToTrack:
        account = TrackedTwitterAccount(id)
        list.append(account)
    return list
