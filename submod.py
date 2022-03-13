from celery.contrib import rdb
#from celery.task import task
from celery import Celery
from . import app
@app.task
def mul(x, y):
    result = x * y
#   rdb.set_trace()  # <- set breakpoint
    return result
times=mul
