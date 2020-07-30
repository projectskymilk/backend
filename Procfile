web: gunicorn skymilk.wsgi --log-level debug
release: python manage.py migrate
release: python manage.py collectstatic --noinput