release: python manage.py migrate --run-syncdb
web: $(gunicorn pickup.wsgi --log-file -; python manage.py rebuild_index)