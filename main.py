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


def run_scheduler(account):
    s = sched.scheduler(time.time, time.sleep)

    def run_main():
        toTrackAccounts = createToTrackList()
        main(account)
        s.enter(900, 1, run_main)  # 900 seconds = 15 minutes

    s.enter(0, 1, run_main)
    s.run()


# call the scheduler function with your Twitter account ID
run_scheduler("1449328468227932163")
