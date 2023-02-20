import sys

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")


from classes.TwitterAccount import TrackedTwitterAccount
from classes.ToFollowAccount import ToFollowAccount
from apscheduler.schedulers.blocking import BlockingScheduler
from helpers.idsToTrack import createToTrackList
import sched, time


def doLogicForOneAccount(account):  # account
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


def runForEveryAccount():
    listAccountsTrackingFollows = createToTrackList()

    for account in listAccountsTrackingFollows:
        doLogicForOneAccount(account)


def schedule():
    # Create a scheduler and schedule the run_main function to run every 15 minutes
    scheduler = BlockingScheduler()
    scheduler.add_job(runForEveryAccount, "interval", seconds=15)

    # Start the scheduler
    scheduler.start()
