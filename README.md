# COS 333 Project

## N.B. we will be using python3 (as Python 2.7 is soon to be deprecated). Currently using MapBox, Django, MongoDB

SETUP: setup ```virtualenv``` (linux: sudo apt-get install virtualenv)
Once you've setup virtualenv and are running a virtual environment, run ```pip3 install -r requirements.txt``` If you're adding requirements, then make sure to do ```pip3 freeze > requirements.txt```

RUNNING:
```333/mysite$ python3 manage.py runserver```

MIGRATING:
```333/mysite$ python3 manage.py migrate```

EDITING THE README:
Install ```grip``` with ```sudo apt-get install grip```
Then, run ```grip README.md```
