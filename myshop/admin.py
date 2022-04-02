from django.contrib import admin

from .models import (Product, Categories, 
                    Reviews, SliderImage
                    )


admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Reviews)
admin.site.register(SliderImage)