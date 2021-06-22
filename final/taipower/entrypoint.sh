#!/bin/bash

# Apply database migrations
echo "Apply database migrations - $MIGRATION_APP"
python manage.py makemigrations $MIGRATION_APP
python manage.py migrate $MIGRATION_APP
python manage.py collectstatic --noinput
uwsgi --ini uwsgi.ini  