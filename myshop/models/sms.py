from django.db import models


class SMSClient(models.Model):
    AUTH_TOKEN_LEN = 10000
    
    token = models.CharField(max_length=10000, blank=False, null=True)