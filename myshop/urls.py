from django.urls import path

from .views import homeView,aboutView,shopView, loginView, myWishlistView, myCardView

urlpatterns = [
    path('', homeView, name='home'),
    path('about-us/', aboutView, name='about-us'),
    path('online-shop/', shopView, name='shop'),
    path('wishlist/', myWishlistView, name='wishlist'),
    path('my-cart', myCardView, name='cart'),
    
    #my-account
    path('my-account/', loginView, name='my-account')
]
