import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'starnavi_test_task_social_jwt.settings.prod')

application = get_wsgi_application()
