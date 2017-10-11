import celery
import os
from datetime import datetime


app = celery.Celery('celery_app')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


@app.task
def task_one(start_time):
    print(f"This is task one, started at {start_time}")

@app.task
def task_two():
    print("This is task two.")
    task_one.delay(start_time=datetime.now())

def util():
    print("Hey!")