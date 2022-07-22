import re
from unicodedata import category
import requests

from django.db.models import Q

from myshop.libs.sms import sms
from myshop.libs.telegram import telebot

from myshop.models.products import Products
from myshop.models.categories import Categories
from myshop.models.customer import CustomerModel


def getCategoryid(mystr: str) -> int:
    """
        This function returns the category identifier id
    """
    id = ""
    for item in mystr:
        if item.isdigit():
            id += item
    
    return id


def send_message(mydict: dict, _type: str= telebot.TYPE_ORDERS) -> None:
    """
        This function sends a message to telegram channel
    """
    if mydict is not None:
        text: str = ""
        product = Products.objects.only("name").get(id=mydict.get('product_id'))  #Select name ...
        
        obj = CustomerModel.objects.create(
            name=mydict.get('name'),
            phone=mydict.get('phone'),
        )
        text += f"<b>Order ID: {obj.id}</b>\n\n"
        text += f"<b>Customer Name: {obj.name}</b>\n"
        text += f"<b>Customer Phone: {obj.phone}</b>\n"
        text += f"<b>Product Name: {product.name}</b>\n"
        
        context: dict = {
            "text": text,
            "_type": _type
        }
        
        telebot.send_message(**context)


def getHostName(link) -> str:
    """Returns the host name"""
    p: str = re.compile("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:\.)?([^:\/?\n]+)")
    r: str = requests.get(link)
    domain: str = p.match(r.url).group(1)
    
    return domain


def searchHelper(request) -> dict:
    """Returns a list of products"""
    search_query: str = ""
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    category: str = Categories.objects.filter(
        name__icontains=search_query
    )
    
    products: list = Products.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(price__icontains=search_query)|
        Q(category__in=category)
    )
    
    return products, search_query

