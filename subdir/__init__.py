from celery.contrib import rdb
from celery import Celery

from .. import app
from .. import _import_all

__all__ = _import_all(globals())()
from . import *

@app.task
def minus(x, y):
    result = x - y
#   rdb.set_trace()  # <- set breakpoint
    return result
