from django.contrib import models 
from django.contrib.auth import get_user_model

from myshop.models.products import Products

User = get_user_model()

class Likes(models.Model):
    user = models.ForeignKey(Products, on_delete=models.CASCADE)