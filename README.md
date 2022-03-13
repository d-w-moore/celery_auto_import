# celery_auto_import
Recursive import straegy to import **/modules for celery

## Use
```
$ pip3 install celery'>=5'[redis]
$ git clone http://github.com/d-w-moore/celery_auto_import tasks
$ python -ic import 
$ tmux
(in window 1: )$ celery -A tasks worker
(in window 2: )$ find -type f|grep -vE '(git|pyc)'|xargs grep def
python3 >>> import tasks; tasks.subdir.mod.div(3, 2.0)
```
