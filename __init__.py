from celery.contrib import rdb
from celery import Celery
import marshal, types

def import_all():
  import os
  from os.path import dirname, join, isfile, isdir
  dir_ = (dirname(__file__))
  sub = os.listdir(dir_)
  EXT='.py'
  fil=[x[:-len(EXT)] for x in sub if isfile(join(dir_,x)) 
                                        and x.endswith(EXT)
                                        and not x.startswith(('_','.'))]
  dirs=[x for x in sub if isdir(join(dir_,x)) and not x.startswith(('.','_'))]
  return fil + dirs

_import_all__code = marshal.dumps(import_all.__code__)

# Lets us import the above function indirectly in context of submodules' dictionaries.
# usage example:
#   from .. import _import_all
#   import_all = _import_all(globals())
#   __all__ = _import_all(globals())()
#   from . import *

def _import_all(dict_):
  return types.FunctionType(marshal.loads(_import_all__code),dict_)

__all__ = import_all()

app = Celery('tasks', broker='redis://', backend='redis://')

from . import *

@app.task
def add(x, y):
    result = x + y
#   rdb.set_trace()  # <- set breakpoint
    return result

plus = add
