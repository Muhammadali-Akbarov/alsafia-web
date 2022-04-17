from django.shortcuts import render

from myshop.models.products import Products
from myshop.models.categories import Categories

def loginView(request):    
    return render(request, 'myshop/my-account.html')

def homeView(request):
    day_recommends = Products.objects.filter(category=Categories.KUN_TAKLIFLARI) #kunning eng yaxhi takliflari
    best_seller    = Products.objects.filter(category=Categories.ENG_KOP_SOTILADIGAN) # eng ko'p sotiladigan
    
    context ={
        "day_recommends": day_recommends,
        "best_seller": best_seller
    }
    
    return render(request, 'myshop/index.html',context)

def aboutView(request):
    return render(request, 'myshop/about.html')


def shopView(request):     
    return render(request, 'myshop/shop.html')


def shopViewDetail(request, id):
    return render(request, 'myshop/shop-detail.html')


def myWishlistView(request):
    return render(request, 'myshop/wishlist.html')


def myCardView(request):
    return render(request, 'myshop/cart.html')
