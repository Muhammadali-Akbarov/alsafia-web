from django.contrib import admin

from myshop.models.products import Products
from myshop.models.categories import Categories


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'category',
                    'image_450_200', 'image_330x330')
    exclude = ('slug',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)
