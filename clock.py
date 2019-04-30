from apscheduler.schedulers.blocking import BlockingScheduler
import wfutv4re

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
def timed_job():
    wfutv4re.tweet()

if __name__ == "__main__":
    twische.start()
