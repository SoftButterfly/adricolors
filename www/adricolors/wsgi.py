# -*- encoding: utf-8 -*-
import os
import dotenv

from django.core.wsgi import get_wsgi_application

DOTENV=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "setup", ".env")
dotenv.read_dotenv(DOTENV)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adricolors.settings")

application = get_wsgi_application()
