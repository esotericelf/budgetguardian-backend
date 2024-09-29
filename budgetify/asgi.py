"""
ASGI config for budgetify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import sys

# Add the project directory to the sys.path
project_home = '/home/esotericelf/budgetguardian-backend'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'budgetify.settings'

# Import Django's WSGI handler to serve the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()