from django.db import models
from django.contrib.auth import get_user_model

from myshop.models.products import Products

User = get_user_model()


class Cart(models.Model):
    user     = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    products = models.ManyToManyField(Products,blank=True, related_name='products')

