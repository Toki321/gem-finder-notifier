from TwitterAccount import TrackedTwitterAccount
from ToFollowAccount import ToFollowAccount
from helpers.idsToTrack import createToTrackList
import sched, time


def main(account):
    # Read old data from txt
    oldFollows = account.extractIdsFromFile()

    # Get latest follow list
    latestFollows = account.getListUsernameFollows()

    # Write new data to txt
    account.writeToFile(latestFollows)

    # Get follows that weren't in the old list
    newFollows = account.getNewFollows(oldFollows, latestFollows)

    # Remove follows that don't meet conditions
    checkedNewFollows = account.getCheckedNewFollows(newFollows)

    # Send telegram notification to group
    account.sendTelegramMessage(checkedNewFollows)


def run_scheduler():
    s = sched.scheduler(time.time, time.sleep)

    def run_main():
        try:
            toTrackAccounts = createToTrackList()
            for account in toTrackAccounts:
                main(account)
                s.enter(900, 1, run_main)  # 900 seconds = 15 minutes
        except:
            print("error for ", account)

    s.enter(0, 1, run_main)
    s.run()


run_scheduler()
