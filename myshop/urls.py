from django.urls import path

from .views import faqView
from .views import likeView
from .views import homeView
from .views import shopView
from .views import loginView
from .views import aboutView
from .views import addCartView
from .views import myCartView
from .views import contactView
from .views import categoryView
from .views import myWishlistView
from .views import shopDetailView
from .views import sendMessageView
from .views import check_cart_list

urlpatterns = [
    
    path('', homeView, name='home'),
    path('faq/', faqView, name='faq'),
    path('my-cart', myCartView, name='cart'),
    path('online-shop/', shopView, name='shop'),
    path('about-us/', aboutView, name='about-us'),
    path('wishlist/', myWishlistView, name='wishlist'),
    path('contact-us/', contactView, name='contact-us'),
    path('by-category/<int:id>/', categoryView, name='category'),
    
    # details
    path('myshop/<str:id>/', shopDetailView, name='shop-detail'),
    path('likes/<int:id>/', likeView, name='likes'),
    path('send-message', sendMessageView, name='send-message'),
    path('add-cart/<str:id>/', addCartView, name='add-cart'),
    
    # my-account
    path('my-account/', loginView, name='my-account'),
    path("check_cart_list", check_cart_list, name="check_cart_list")
]
