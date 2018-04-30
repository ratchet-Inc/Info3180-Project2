release: python flask-migrate.py db upgrade --directory migration
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app