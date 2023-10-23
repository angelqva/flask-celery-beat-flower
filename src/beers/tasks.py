import time
from datetime import datetime
from celery import shared_task
from celery.contrib.abortable import AbortableTask
# from flask_caching import Cache
from .repository import BEER_REPOSITORY

# cache = Cache(config={'CACHE_TYPE': 'simple'})
# TEN_MINUTES = 10 * 60 * 1000


@shared_task(name="sync_task", bind=True, base=AbortableTask)
def sync_task(self):
    time.sleep(10)
    response = BEER_REPOSITORY.counts()
    if self.is_aborted():
        return 'TASK STOPPED!'
    return {"beers length": response}


@shared_task(name="periodic")
def periodic():
    current_timestamp = int(time.mktime(datetime.now().timetuple()))
    return f"Periodic task, timestamp: {current_timestamp}"
