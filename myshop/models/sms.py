from django.db import models


class SMSClient(models.Model):
    AUTH_TOKEN_LEN = 617
    
    token = models.CharField(max_length=817, blank=False, null=True)