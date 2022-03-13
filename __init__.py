from celery.contrib import rdb
from celery import Celery
import os

def import_all():
  from os.path import dirname,join,isfile,isdir
  dir_ = (dirname(__file__))
  sub = os.listdir(dir_)
  EXT='.py'
  fil=[x[:-len(EXT)] for x in sub if isfile(join(dir_,x)) 
                                        and x.endswith(EXT)]
  dirs=[x for x in sub if isdir(join(dir_,x))]
  return fil+dirs

__all__ = import_all()

app = Celery('tasks', broker='redis://')

from . import *

@app.task
def add(x, y):
    result = x + y
#   rdb.set_trace()  # <- set breakpoint
    return result

plus = add