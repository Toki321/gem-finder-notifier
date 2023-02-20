import threading
import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

from classes.TweetStreamer import TweetStreamer
from helpers.idsToTrack import readIds


def streamTweets():
    listAccounts = readIds()

    print(listAccounts)
    listAccounts.append("2966287497")

    streamerOne = TweetStreamer(listAccounts)

    streamerOne.startStreaming()
