import sys
import requests

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")
import tweepy
from tweepy import StreamingClient, StreamRule
import os
from dotenv import load_dotenv
from helpers.tweepyClient import getTweepyClient
from helpers.top100coins import get_top_100_cryptos

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_NARRATIVE_TRADERS_CHAT_ID")

top_100_coins_dict = get_top_100_cryptos()


class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if self.isTick(tweet.text):
            url = f"https://twitter.com/{tweet.author_id}/status/{tweet.id}"
            self.postUrlToTelegram(url)

    def postUrlToTelegram(self, url):
        TOKEN = os.getenv("TELEGRAM_GHOUL_TOKEN")
        CHAT_ID = "-710524915"
        # CHAT_ID = os.getenv("TELEGRAM_NARRATIVE_TRADERS_CHAT_ID")
        print("sending tweet to tg: ", url)
        MESSAGE = url
        call = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
        requests.get(call).json()

    def isInTop100(self, threeLetteres):
        try:
            get = top_100_coins_dict[threeLetteres.upper()]
        except KeyError:
            return False
        return True

    def isCorrect(self, charArr):
        # if 3 letters and space
        if (
            charArr[0].isalpha() == True
            and charArr[1].isalpha() == True
            and charArr[2].isalpha() == True
        ):
            try:
                if charArr[3].isalpha() == False or charArr[4].isalpha() == False:
                    return True
            except:
                return True
        return False

    def isTick(self, text):
        try:
            index = text.index("$")
        except:
            print("no ticker: ", text)
            return
        threeLetters = text[index + 1 : index + 3]
        if self.isInTop100(threeLetters) == True:
            return False
        else:
            substring = text[index + 1 : index + 6]
            return self.isCorrect(substring)

    def on_connect(self):
        print("connected")


class TweetStreamer:
    def __init__(self, list1, list2, list3) -> None:
        self.accountsToTrackOne = list1
        self.accountsToTrackTwo = list2
        self.accountsToTrackThree = list3
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

    def ruleString(self, flag):
        index = 0
        ruleString = ""
        if flag == "one":
            for account in self.accountsToTrackOne:
                ruleString += "from: " + account + " "
                if index != len(self.accountsToTrackOne) - 1:
                    ruleString += "OR "
                index += 1
        elif flag == "two":
            for account in self.accountsToTrackTwo:
                ruleString += "from: " + account + " "
                if index != len(self.accountsToTrackTwo) - 1:
                    ruleString += "OR "
                index += 1
        elif flag == "three":
            for account in self.accountsToTrackThree:
                ruleString += "from: " + account + " "
                if index != len(self.accountsToTrackThree) - 1:
                    ruleString += "OR "
        print(ruleString)
        return ruleString

    # Start printer
    def startStreaming(self):
        self.cleanRules()
        rules = []
        rules.append(StreamRule(self.ruleString("one")))
        rules.append(StreamRule(self.ruleString("two")))
        # rules.append(StreamRule(self.ruleString("three")))
        self.tweetPrinter.add_rules(rules)
        self.tweetPrinter.filter(expansions="author_id", media_fields="url")
