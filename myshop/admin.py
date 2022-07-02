from django.contrib import admin

from myshop.models.cart import Cart
from myshop.models.products import Likes
from myshop.models.wishlist import Wishlist
from myshop.models.products import Products
from myshop.models.categories import Categories


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'category',
                    'image_450_200',)
    exclude = ('slug',)


admin.site.register(Cart)
admin.site.register(Likes)
admin.site.register(Wishlist)
admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)

