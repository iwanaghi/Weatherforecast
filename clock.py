from apscheduler.schedulers.blocking import BlockingScheduler
import wfutv4re

twische = BlockingScheduler()

@twische.scheduled_job('interval',hours=24)
def timed_job():
    wfutv4re.tweet()

if __name__ == "__main__":
    twische.start()
