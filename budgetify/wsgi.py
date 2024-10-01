"""
WSGI config for budgetify project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables from the .env file
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Add your project directory to the sys.path
project_home = '/home/esotericelf/budgetguardian-backend'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the settings module for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budgetguardian.settings')

# Get the WSGI application for the project
application = get_wsgi_application()
