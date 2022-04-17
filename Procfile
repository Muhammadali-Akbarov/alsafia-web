release: python manage.py migrate
release: python manage.py loaddata db.json
web: gunicorn configs.wsgi --log-file -