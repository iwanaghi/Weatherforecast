from apscheduler.schedulers.blocking import BlockingScheduler
import wfutv4re
import wfutv4osaka

twische = BlockingScheduler()

@twische.scheduled_job('interval',hours=23)
def timed_job():
    wfutv4re.tweet()
    wfutv4osaka.tweet()

if __name__ == "__main__":
    twische.start()
