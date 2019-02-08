"""
WSGI config for referralApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'referralApp.settings')
print("Here is what is happening right before the get wsgi portion of the wsgi file")
application = get_wsgi_application()
