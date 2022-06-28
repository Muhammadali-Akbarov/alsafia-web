from django.db import models 


class CustomerModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=14, blank=False)
    