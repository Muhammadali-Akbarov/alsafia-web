from myshop.libs.telegram import telebot
from myshop.models.customer import CustomerModel

from myshop.models.products import Products

def getCategoryid(mystr: str) -> int:
    id = ""
    for item in mystr:
        if item.isdigit():
            id += item
    
    return id

def send_message(mydict: dict) -> None:
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
        telebot.send_message(text)