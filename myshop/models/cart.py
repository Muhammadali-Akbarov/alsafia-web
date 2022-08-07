from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model

from myshop.models.products import Products

User = get_user_model()


class Cart(models.Model):
    user     = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Products,blank=True, related_name='products')
    
    @property
    def getTotalCost(self):
        return self.products.all().aggregate(Sum('price'))