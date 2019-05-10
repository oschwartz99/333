# meetup
### N.B. we will be using python3 (3.7.2) (as Python 2.7 is soon to be deprecated). Currently using MapBox, Django (2.1.7), MongoDB

CURRENT PROGRESS:
- Creating user login page/sign up page (see tutorial below)

USEFUL (non-essential) COMMANDS:
- ```tree``` lists directory structure in a tree-layout
- ```python3 manage.py shell``` - can view database structure, view object models, manipulate things in the database
- while in ```shell``` mode, use ```help(Object_name)``` to view the methods and fields of an object

TENTATIVE TO-DO:
- Begin learning Mapbox API to add additional functionality
- Begin fleshing out what we need to add to Mapbox (e.g. pop-up labels for pickup sites)
- Brainstorm other functionality (do we want just a map interface?)

RESOURCES:
- Corey Schafer Django Python Tutorial (YouTube)
- [Django Official Tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
- [Adding Mapbox to Django](https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html)
- [Markdown cheatsheet for README.md](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
- [Mapbox](https://www.mapbox.com/)
- [User and Login tutorial](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
- [Deploying Django to Heroku from Scratch](https://medium.com/@BennettGarner/deploying-django-to-heroku-procfile-static-root-other-pitfalls-e7ab8b2ba33b)

SETUP: 
- Make sure you have Python 3.6.3. Check with: ```python --version```
- Virtual environment creator: ```sudo apt-get install python3/venv```
- create a directory to house venv: ```cd ~/; mkdir envs; mkdir/envs/pickup; python3 -m venv ~/envs/pickup```
- activate venv: ```source ~/envs/pickup/bin/activate```
- Once you've setup virtualenv and are running a virtual environment, run ```pip3 install -r requirementsUbuntu.txt``` 
- If you are using a Mac, run this command instead ```pip3 install -r requirements.txt``` 
- We need to address the discrepancy in requirements between the Mac and Ubuntu version. Some packages are incompatible. 
- The requirements.txt file is used by Heroku to install requirements, so maintain it as the main requirements file until issue is solved.
- If adding requirements to a Mac, then make sure to do ```pip3 freeze > requirements.txt``` 
- If adding requirements to Ubuntu, then make sure to do ```pip3 freeze > requirementsUbuntu.txt``` 

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

HOSTING ON HEROKU:
- make sure that you have the Heroku Command Line Interface (CLI) downloaded. 
- If you are using Mac, then run ```brew install heroku/brew/heroku``` to download the CLI
- If you are using Ubuntu, then run ```sudo snap install heroku --classic``` to download the CLI
- Log in to Heroku with ```heroku login``` if not already logged in. 


DEPLOYING CODE TO HEROKU: 
- Beware, as the following lines will delete any committed changes that have not yet been pushed. Uncommitted changes are okay.
- Initialize another local git repository. ```cd pickup``` then ```git init``` 
- If you have any changes, then add them with then ```git add .``` and commit with ```git commit -m "My first commit"```
- Add the remote to your local repository from Heroku with ```heroku git:remote -a pickup333```
- If you wish to deploy code from your local repository's master branch to the heroku remote, run ```git push heroku-django master```
- If you want to deploy from a non-master branch, then use ```git push heroku-django testbranch:master``` substituting testbranch

OPENING THE APP:
- Run ```python manage.py collectstatic``` to prepare the app locally. 
- You can run the app locally on a Unix system with ```heroku local web```
- You can run the app locally on Windows with ```heroku local web -f Procfile.windows```
- You can run the app on Heroku's web server with ```heroku open```

RUNNING THE SEARCH ENGINE: 
- We are using Haystack with Whoosh as the backend search engine. 
- Whoosh uses its own database that allows more efficient search than database queries
- You must build this database the first time before you ```run server``` to ensure the models are built. It automatically updates afterwards
- Run ```pythony3 manage.py rebuild_index``` to build the search index
- You can change which points of data are searchable with the search_indexes.py in each app (maps, users, etc.) Look at the other fields as examples.
- You can search for items using the SearchQuerySet() api from haystack. Make sure you import the library. Use event search in maps/view.py as an example.

COLORS:
-ED9E00
