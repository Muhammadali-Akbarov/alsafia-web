import requests

from django.conf import settings


class SMSClient:
    __CONTACT = "contact"
    __AUTH_USER = "auth/user"
    __AUTH_LOGIN = "auth/login"
    __AUTH_REFRESH = "auth/refresh"
    __AUTH_INVALIDATE = "auth/invalidate"
    
        