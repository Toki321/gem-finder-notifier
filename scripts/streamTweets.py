import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

from classes.TweetStreamer import TweetStreamer

listAccounts = ["1449328468227932163", "2966287497"]

streamer = TweetStreamer(listAccounts)

streamer.startStreaming()
