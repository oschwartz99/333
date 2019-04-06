#!/bin/bash

rm db.sqlite3
rm maps/migrations/00*
rm users/migrations/00*
python3 manage.py makemigrations
python manage.py migrate --run-syncdb
python3 manage.py createsuperuser
python3 manage.py runserver