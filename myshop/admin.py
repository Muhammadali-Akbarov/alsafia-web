from django.contrib import admin


from myshop.models.cart import Cart
from myshop.models.sms import SMSClient
from myshop.models.products import Products
from myshop.models.categories import Categories
from myshop.models.order_history import OrderHistory

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',
                    'image_450_200',)
    exclude = ('slug', 'discount', )


admin.site.register(Categories)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Cart)
admin.site.register(OrderHistory)
admin.site.register(SMSClient)