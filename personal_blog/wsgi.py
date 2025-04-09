"""
WSGI config for personal_blog project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_blog.settings')

application = get_wsgi_application() 