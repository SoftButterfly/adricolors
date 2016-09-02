#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys
import dotenv

DOTENV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "setup", ".env")

if __name__ == "__main__":
    dotenv.read_dotenv(DOTENV)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adricolors.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
            execute_from_command_line = django.core.management.execute_from_command_line
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
