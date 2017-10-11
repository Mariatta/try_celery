import celery
import os
from datetime import datetime


app = celery.Celery('celery_app')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


@app.task(rate_limit="1/m")
def task_one(start_time, source=None):
    print(f"This is task one, started at {start_time}, source {source}")



@app.task(rate_limit="1/m")
def task_two():
    print("This is task two, now starting task one.")
    util()
    task_one.delay(start_time=datetime.now(), source="task two")

def util():
    print("Hey!")