# A brief script for when models have been modified 
# and the database needs to be deleted and recreated
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
