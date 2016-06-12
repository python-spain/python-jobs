web: gunicorn python_jobs.wsgi
worker: python manage.py rqworker default --settings=python_jobs.settings --configuration=Prod
