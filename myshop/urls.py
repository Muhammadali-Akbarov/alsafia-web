from django.urls import path

from .views import homeView,aboutView,shopView

urlpatterns = [
    path('', homeView, name='home'),
    path('about-us/', aboutView, name='about-us'),
    path('online-shop/', shopView, name='shop'),
]
