"""
ASGI config for emun project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from emun.settings import BASE_DIR
from whitenoise import WhiteNoise
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emun.settings')

application = get_asgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static/'))
