import os
import sys

sys.path.append('usr/lib/python2.6/site-packages/ermis')
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

