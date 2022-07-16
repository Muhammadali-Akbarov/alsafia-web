from itertools import product
from uuid import uuid4

from django.db.models import Sum
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from myshop.models.cart import Cart
from myshop.models.products import Products
from myshop.models.categories import Categories

from myshop.utils import send_message
from myshop.utils import searchHelper
from myshop.libs.telegram import telebot


def homeView(request) -> object:
    
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
        "all_products": _all_products,
    }
    context["order_history"] = 0
    context["cartProductsCount"] = 0
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
        

    return render(request, 'myshop/index.html', context)


def aboutView(request):
    categories = Categories.objects.all()
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    context['categories'] = categories
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
        
    return render(request, 'myshop/about.html', context)


def shopView(request):
    categories = Categories.objects.all()
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    context['categories'] = categories
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
            
    return render(request, 'myshop/shop.html', context)


def shopDetailView(request, id) -> Products:
    categories = Categories.objects.all()
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    context['categories'] = categories
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
    
    items: Products = Products.objects.get(id=id)
    context["items"]=items

    return render(request, 'myshop/shop-detail.html', context)


@login_required(login_url='my-account')
def myWishlistView(request):
    categories = Categories.objects.all()
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    context['categories'] = categories
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
        
    return render(request, 'myshop/wishlist.html', context)


@login_required(login_url='my-account')
def myCartView(request):
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        context["cardItems"]=cartProducts.products.all()
        context["cartProductsCount"]=cartProducts.products.count()
        
        if cartProducts:
            context['items'] = cartProducts.products.all()
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
    
    return render(request, 'myshop/cart.html', context)


def contactView(request):
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        context["cardItems"]=cartProducts.products.all()
        context["cartProductsCount"]=cartProducts.products.count()
        
    return render(request, 'myshop/contact.html', context)


def faqView(request):
    context: dict = {}
    
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
        
    return render(request, 'myshop/faq.html', context)


def searchView(request) -> list:
    products, _ = searchHelper(request)
    categories = Categories.objects.all()
    
    context: dict = {}
    context['products'] = None
    context["order_history"] = 0
    context["cartProductsCount"] =  0
    context['categories'] = categories
    
    if len(products) > 0:
        context['products'] = products
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
       
    return render(request, 'myshop/search.html', context)
    


def categoryView(request, id: int) -> list:
    categories = Categories.objects.all()
    
    context: dict = {}
    context["order_history"] = 0
    context["cartProductsCount"] = 0
    context['categories'] = categories
    
    if request.user.is_authenticated:
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        if cartProducts:
            context['sum'] = cartProducts.products.aggregate(Sum('price')).get('price__sum')
            context["cardItems"]=cartProducts.products.all()
            context["cartProductsCount"]=cartProducts.products.count()
    
    if id == 0:
        products = Products.objects.all()
    
    if id > 0:
        products = Products.objects.filter(category_id=id)
    
    context['products'] = products

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



@login_required(login_url='my-account')
def removeCartView(request, id: int) -> None:
    cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
    if cartProducts:
        cartItem = cartProducts.products.get(id=id)
        cartProducts.products.remove(cartItem)
        messages.add_message(request, messages.INFO, 'Savatchadan muofaqqiyatli o\'chirildi ✅')
    
    return redirect('home')


@login_required(login_url='my-account')
def addCartView(request, id: int) -> None:
    messages.add_message(request, messages.INFO, 'Savatchaga muofaqqiyatli qo\'shildi ✅')
    
    product: Products = Products.objects.get(id=id)
    cart,_ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()
    if request.META['SERVER_NAME'] in settings.ALLOWED_HOSTS:
        return redirect('home')
    
    return redirect('shop-detail', product.id)


def orderView(request):
    if request.method == 'POST':
        price: int = 0
        text: str = ""
        text += f"<b>ID</b>: {uuid4()}\n\n"
        text += f"Haridor ismi: {request.user.first_name}\n"
        text += f"Haridor Raqami: {request.user.phone}\n\n"
        
        cartProducts: Cart = Cart.objects.filter(user=request.user).prefetch_related("products").first()
        for product in cartProducts.products.all():
            price += product.price
            text += f"{product.name} - {product.price} UZS\n"
        
        cartProducts.delete()
        text += F"Jami - {price} UZS"
        telebot.send_message(text, telebot.TYPE_ORDERS)
        
    return redirect('thanks')


def thanksView(request):
    return render(request, 'thanks/index.html')

