from unicodedata import category
from django.shortcuts import render

from myshop.models.products import Products
from myshop.models.categories import Categories


def loginView(request) -> None:
    return render(request, 'myshop/my-account.html')


def homeView(request) -> object:
    categories = Categories.objects.all()
    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    the_most_popular = Products.objects.filter(
        category=Categories.ENG_MASHHUR_MAHSULOTLAR)[:4]  # eng mashhur mahsulotlar

    context = {
        "best_seller": best_seller,
        "day_recommends": day_recommends,
        "the_most_popular": the_most_popular,
        "categories": categories
    }

    return render(request, 'myshop/index.html', context)


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


def contactView(request):
    return render(request, 'myshop/contact.html')


def faqView(request):
    return render(request, 'myshop/faq.html')


def categoryView(request, id: int) -> object:    
    if id == 0:
        products = Products.objects.all()
        
    if id > 0:
        products = Products.objects.filter(category_id=id)

    context: dict = {
        "products": products
    }

    return render(request, 'myshop/by_category.html', context)
