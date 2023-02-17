import tweepy
from tweepy import StreamingClient, StreamRule
import os
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
chat_id = os.getenv("TELEGRAM_NARRATIVE_TRADERS_CHAT_ID")


class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)

    def on_connect(self):
        print("connected")


printer = TweetPrinterV2(bearer_token)

# clean-up pre-existing rules
rule_ids = []
result = printer.get_rules()
print(result)
if result.data != None:
    for rule in result.data:
        print(f"rule marked to delete: {rule.id} - {rule.value}")
        rule_ids.append(rule.id)

    if len(rule_ids) > 0:
        printer.delete_rules(rule_ids)
        printer = TweetPrinterV2(bearer_token)
    else:
        print("no rules to delete")

# 1449328468227932163

# add new rules
rule = StreamRule(value="from: 1449328468227932163")
printer.add_rules(rule)

printer.filter(
    expansions="author_id",
)
