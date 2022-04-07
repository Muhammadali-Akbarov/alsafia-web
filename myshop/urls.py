from django.urls import path

<<<<<<< HEAD
from .views import homeView,aboutView,shopView, loginView, myWishlistView, myCardView
=======
from .views import homeView,aboutView,shopView
>>>>>>> 886dc647164e88759490565a3df5da18f34d72d4

urlpatterns = [
    path('', homeView, name='home'),
    path('about-us/', aboutView, name='about-us'),
    path('online-shop/', shopView, name='shop'),
<<<<<<< HEAD
    path('wishlist/', myWishlistView, name='wishlist'),
    path('my-cart', myCardView, name='cart'),
    
    #my-account
    path('my-account/', loginView, name='my-account')
=======
>>>>>>> 886dc647164e88759490565a3df5da18f34d72d4
]
