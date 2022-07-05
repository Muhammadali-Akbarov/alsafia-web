import re
import requests

from myshop.libs.sms import sms
from myshop.libs.telegram import telebot

from myshop.models.products import Products
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
        product = Products.objects.only("name").get(id=mydict.get('product_id'))
        
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
    p: str = re.compile("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:\.)?([^:\/?\n]+)")
    r: str = requests.get(link)
    domain: str = p.match(r.url).group(1)
    
    return domain
