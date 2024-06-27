#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # if len(sys.argv) == 1 or sys.argv[1] == 'runserver':
    #     sys.argv.append('192.168.0.18:8000')
    # python manage.py runserver 192.168.0.18:8000
    # 여러분들이 서버가 될 경우엔 자신의 IP를 직접 넣어야함

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()