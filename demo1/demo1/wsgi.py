"""
WSGI config for demo1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

# 项目想要发布运行 需要遵循WSGI协议
# web service gateway interface

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo1.settings')

application = get_wsgi_application()
