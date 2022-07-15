from django.urls import path

from .views import CartAPIView


urlpatterns = [
    path('cart-check/', CartAPIView.as_view())
]

