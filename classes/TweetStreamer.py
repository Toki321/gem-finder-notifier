import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")
import tweepy
from tweepy import StreamingClient, StreamRule
import os
from dotenv import load_dotenv
from helpers.tweepyClient import getTweepyClient

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_NARRATIVE_TRADERS_CHAT_ID")
client = getTweepyClient()


class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        url = f"https://twitter.com/{tweet.author_id}/status/{tweet.id}"
        print(url)
        # print(tweet.url)
        # print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        # print("tweet Object: ", tweet)
        # print("-" * 50)

    def on_connect(self):
        print("connected")


class TweetStreamer:
    def __init__(self, list) -> None:
        self.accountsToTrack = list
        self.tweetPrinter = TweetPrinterV2(BEARER_TOKEN)

    # clean rules
    def cleanRules(self):
        ruleIds = []
        rules = self.tweetPrinter.get_rules()
        rulesArr = rules.data
        if rulesArr != None:
            for rule in rulesArr:
                print(f"rule marked to delete: {rule.id} - {rule.value}")
                ruleIds.append(rule.id)

            if len(ruleIds) > 0:
                self.tweetPrinter.delete_rules(ruleIds)
                self.tweetPrinter = TweetPrinterV2(BEARER_TOKEN)
            else:
                print("no rules to delete")

    def ruleString(self):
        index = 0
        ruleString = ""
        for account in self.accountsToTrack:
            ruleString += "from: " + account + " "
            if index != len(self.accountsToTrack) - 1:
                ruleString += "OR "
            index += 1

        print(ruleString)
        return ruleString

    # Start printer
    def startStreaming(self):
        self.cleanRules()
        rules = StreamRule(self.ruleString())
        self.tweetPrinter.add_rules(rules)
        self.tweetPrinter.filter(expansions="author_id", media_fields="url")
