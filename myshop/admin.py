from django.contrib import admin

from myshop.models.products import Products
from myshop.models.categories import Categories


admin.site.register(Products)
admin.site.register(Categories)