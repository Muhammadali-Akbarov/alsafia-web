from re import T
from django.db import models
from django.contrib.auth import get_user_model

from myshop.models.products import Products

User = get_user_model()

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    liked = models.BooleanField(default=False, null=True, blank=True)
    
    def isTrue(self):
        self.liked = True
        self.save()
    
    def isFalse(self):
        self.liked = False
        self.save()