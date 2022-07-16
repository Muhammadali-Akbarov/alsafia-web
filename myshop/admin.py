from django.contrib import admin

from myshop.models.products import Products
from myshop.models.categories import Categories


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',
                    'image_450_200',)
    exclude = ('slug', 'discount', )


admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)

