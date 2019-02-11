# COS 333 Project

## N.B. we will be using python3 (as Python 2.7 is soon to be deprecated). Currently using MapBox, Django, MongoDB


RESOURCES:
- [Django Official Tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
- [Adding Mapbox to Django](https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html)
- [Markdown cheatsheet for README.md](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
- [Mapbox](https://www.mapbox.com/)
- [User and Login tutorial](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)



SETUP: 
- setup ```virtualenv``` (linux: sudo apt-get install virtualenv)
- Once you've setup virtualenv and are running a virtual environment, run ```pip3 install -r requirements.txt``` 
- If you're adding requirements, then make sure to do ```pip3 freeze > requirements.txt```

RUNNING:
- **```333/mysite$```** ```python3 manage.py runserver```. Then go to ```http://127.0.0.1:8000/accounts/login``` to view the webapp.
- **username**: ollie, **password**: ollie

MIGRATING:
- **```333/mysite$```** ```python3 manage.py migrate```

EDITING THE README:
- Install ```grip``` with ```sudo apt-get install grip```. Then, run ```grip README.md```

MAKING MODEL CHANGES:
- change your models (in ```models.py```)
- run ```python3 manage.py makemigrations``` to create migrations for those changes
- run ```python3 manage.py migrate``` to apply changes to database
