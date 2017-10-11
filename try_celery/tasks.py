import celery
import os
from datetime import datetime


app = celery.Celery('celery_app')

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


@app.task
def task_one(start_time, source=None):
    print(f"This is task one, started at {start_time}, source {source}")



@app.task
def task_two():
    print("This is task two, now starting task one.")
    util()
    # task_one.delay(start_time=datetime.now(), source="task two")
    celery.current_app.send_task('try_celery.tasks.task_one', args=[datetime.now(), 'task two'])

def util():
    print("Hey!")