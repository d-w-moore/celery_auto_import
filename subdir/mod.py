from celery.contrib import rdb
from celery import Celery

from .. import app

@app.task
def div(x, y):
    result = x / y
#   rdb.set_trace()  # <- set breakpoint
    return result
