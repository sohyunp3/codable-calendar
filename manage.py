#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocalendar.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Not able to import Django. Did you install Django and "
            "make it available on your PYTHONPATH environment variable?"
            "Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
