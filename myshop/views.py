from django.db.models import Sum

from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from myshop.utils import send_message

from myshop.models.cart import Cart
from myshop.models.products import Likes
from myshop.models.products import Products
from myshop.models.categories import Categories



def loginView(request) -> None:
    return render(request, 'myshop/my-account.html')


def homeView(request) -> object:
    likes: Likes = Likes.objects.filter(
        user=request.user, liked=True).select_related("products")
    
    categories = Categories.objects.all()
    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    the_most_popular = Products.objects.filter(
        category=Categories.ENG_MASHHUR_MAHSULOTLAR)[:4]  # eng mashhur mahsulotlar
    _all_products = Products.objects.all()  # all products

    context = {
        "best_seller": best_seller,
        "day_recommends": day_recommends,
        "the_most_popular": the_most_popular,
        "categories": categories,
        "likes": likes,
        "all_products": _all_products
    }

    return render(request, 'myshop/index.html', context)


def aboutView(request):
    return render(request, 'myshop/about.html')


def shopView(request):
    return render(request, 'myshop/shop.html')


def shopDetailView(request, id) -> Products:
    items: Products = Products.objects.get(id=id)
    context: dict = {
        "items": items
    }

    return render(request, 'myshop/shop-detail.html', context)


def myWishlistView(request) -> Likes:
    likes: Likes = Likes.objects.filter(user=request.user).select_related("products").filter(liked=True)
    
    context: dict = {
        'likes': likes
        }

    return render(request, 'myshop/wishlist.html', context)


def myCartView(request):
    cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
    
    context: dict = {
        "items": cartProducts.products.all(),
        "sum": cartProducts.products.aggregate(Sum('price')).get('price__sum')
    }
    
    return render(request, 'myshop/cart.html', context)


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


def sendMessageView(request) -> None:
    if request.method == 'POST':
        mydict: dict = {}
        product_id = request.META['HTTP_REFERER'][29:-1]
        mydict.update({
            "name": request.POST.get('name'),
            "phone": request.POST.get('phone'),
            "product_id": product_id
        })
        send_message(mydict)
        return redirect('shop-detail', product_id)


def likeView(request, id: int) -> None:
    item, _ = Likes.objects.only('liked').get_or_create(products_id=id, user=request.user)
    
    if item.liked:
        item.delete()
    
    if not item.liked:
        item.isTrue()
    
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect('home')
    
    return redirect('category', request.META['HTTP_REFERER'][34:-1])


def addCartView(request, id: int) -> None:
    product: Products = Products.objects.get(id=id)
    cart,_ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect('home')
    
    return redirect('shop-detail', product.id)
