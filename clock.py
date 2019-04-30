from apscheduler.schedulers.blocking import BlockingScheduler
import words

twische = BlockingScheduler()

@twische.scheduled_job('interval',hours=24)
def timed_job():
    words.puttweet()

if __name__ == "__main__":
    twische.start()
