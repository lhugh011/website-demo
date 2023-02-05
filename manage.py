#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# This is a comment to test if git will display a modification message.
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# Another commit to see other changes.
# Yet another step back...
# and yet another step back (bass thump)
x = 21
y = 13


if __name__ == '__main__':
    main()
