"""
WSGI config for python_jobs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_jobs.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
