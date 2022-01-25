###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
import os
from django.core.asgi import get_asgi_application

###############################################################################

"""
ASGI config for django_pp4_ci_wqcs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pp4_ci_wqcs.settings')

application = get_asgi_application()
