#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
    
    try:
        from django.conf import settings
        from django.core.management import execute_from_command_line
        from myshop.libs.telegram import telebot
        if settings.DEBUG == False:
            telebot.send_message("Alsafia has been deployed successfully ✅", telebot.TYPE_WARNINGS)
    
    except ImportError as exc:
        from myshop.libs.telegram import telebot
        if settings.DEBUG == False:
            telebot.send_message("Alsafia has been deployed unsuccessfully ❌", telebot.TYPE_WARNINGS)
        
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    
    main()
    