from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderHistory(models.Model):
    user     = models.OneToOneField(User, related_name='history_order', on_delete=models.DO_NOTHING)
    products = models.ManyToManyField('Products',blank=True, related_name='history_products')