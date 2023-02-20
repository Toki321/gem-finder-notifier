import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

import os.path
from classes.TwitterAccount import TrackedTwitterAccount


def readIds():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../accountsForTracking1.txt")

    with open(file_path, "r") as f:
        lines = f.readlines()
        toTrackIdList = []
        for line in lines:
            try:
                toTrackIdList.append(line.split(" ")[1])
            except IndexError:
                print(line)

        return toTrackIdList


def createToTrackList():
    list = []
    idsToTrack = readIds()
    for id in idsToTrack:
        account = TrackedTwitterAccount(id)
        list.append(account)
    return list
