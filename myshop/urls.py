from django.urls import path

from .views import faqView
from .views import homeView
from .views import shopView
from .views import orderView
from .views import aboutView
from .views import searchView
from .views import myCartView
from .views import thanksView
from .views import addCartView
from .views import contactView
from .views import categoryView
from .views import myWishlistView
from .views import removeCartView
from .views import shopDetailView
from .views import sendMessageView
from .views import removeOrderHistoryView


urlpatterns = [
    
    path('', homeView, name='home'),
    path('faq/', faqView, name='faq'),
     path('order/', orderView, name='order'),
    path('my-cart/', myCartView, name='cart'),
    path('thanks/', thanksView, name='thanks'),
    path('search/', searchView, name='search'),
    path('online-shop/', shopView, name='shop'),
    path('about-us/', aboutView, name='about-us'),
    path('wishlist/', myWishlistView, name='wishlist'),
    path('contact-us/', contactView, name='contact-us'),
    path('send-message/<str:id>/', sendMessageView, name='send-message'),
    
    # details
    path('add-cart/<str:id>/', addCartView, name='add-cart'),
    path('myshop/<str:id>/', shopDetailView, name='shop-detail'),
    path('by-category/<int:id>/', categoryView, name='category'),
    path('remove-cart/<int:id>/', removeCartView, name='remove-cart'),
    path('remove-order-history/<int:id>/', removeOrderHistoryView, name='remove-order-history'),
    # my-account
    
   
]
