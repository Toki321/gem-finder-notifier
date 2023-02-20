import sys
import multiprocessing

sys.path.append("D:\\Coding Projects\\gem-finder-notifier")

from notifyFollows import schedule
from streamTweets import streamTweets

if __name__ == "__main__":
    # Create two processes, one for each script
    p1 = multiprocessing.Process(target=schedule)
    p2 = multiprocessing.Process(target=streamTweets)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
