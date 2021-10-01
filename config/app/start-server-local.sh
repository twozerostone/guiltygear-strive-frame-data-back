#!/bin/bash
python manage.py collectstatic --no-input
gunicorn --reload core.wsgi:application -b 0.0.0.0:12000 --timeout=60
celery -A core worker -l INFO