from django.db import models


class SMSClient(models.Model):
    token = models.CharField(max_length=617, blank=False, null=True)