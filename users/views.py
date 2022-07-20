import logging

from uuid import uuid4

from django.db import transaction
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

from myshop.libs.sms import sms
from myshop.libs.redis import redis
from myshop.libs.telegram import telebot

from users import login
from users.models import User
from users.utils import generate_code
from users.utils import cryptography_fearnet_endcoder


logger = logging.getLogger(__name__)


def loginView(request) -> dict:
    """This method is about login/logout"""
    if request.user.is_authenticated and request.user.is_verified:
         return redirect('home')
    
    page: str = 'login'
    code: str = generate_code()
    user: User = None
    
    if request.method == 'POST':
        phone = request.POST.get('phone').replace("+", "")
        
        try:
            with transaction.atomic():
                user = User.objects.get(phone=phone, is_deleted=False)
                if user is not None:
                    user.is_verified = False
                    sms._send_verify_message(user.phone, code)
                    user.save()
                    context: dict = {
                        "request": request,
                        "user": user,
                        "code": code,
                    }
                    login(**context)
                    
                    return redirect('confirm')
                
        except User.DoesNotExist:
            page: str = 'register'
    
    context: dict = {
        "page": page,
    }

    return render(request, 'users/login.html', context)


def registerView(request) -> dict:
    if request.user.is_authenticated and request.user.is_verified:
        return redirect('home')
    
    if request.method == 'POST':
        context: dict = {}
        passowrd, key = cryptography_fearnet_endcoder(str(uuid4()).replace("-","")[:12])
        print(passowrd)
        print(key)

        try:
            context['key'] = key
            context['password'] = passowrd.decode()
            context['first_name'] = request.POST.get('name')
            context['phone'] = request.POST.get('phone_number').replace("+", "")
            
            code: str = generate_code()
            
            try:
                user: User = User.objects.get(phone=context['phone'])
                
                if user.is_authenticated and user.is_verified:
                    return redirect('home')
            
                sms._send_verify_message(user.phone, code)
                context: dict = {
                    "user": user,
                    "code": code,
                    "request": request,
                    }
                if user.is_authenticated and user.is_verified == False:
                    login(**context)
                    return redirect('confirm')
            
            except User.DoesNotExist:
                logger.info("User does not exist")
            
            
            user: User = User.objects.create(**context)
            with transaction.atomic():
                if user is not None:
                    user.is_verified = False
                    sms._send_verify_message(user.phone, code)
                    user.save()
                    context: dict = {
                        "request": request,
                        "user": user,
                        "code": code,
                        }
                    login(**context)
                
                return redirect('confirm')
            
        except Exception as err:
            context: dict = {
                "text": err,
                "_type": telebot.TYPE_WARNINGS
            }
            telebot.send_message(**context)
            logger.error(f"Error during registeration {err}")
            pass

    return render(request, 'users/login.html')


def verifyView(request) -> None:
    """This View verifies users if they have verified code"""
    page: str = 'confirm'
    code = request.POST.get('code')
    session_id: str = request.COOKIES.get('sessionid')
    checked: bool = redis._check_code_in_redis(session_id, code)
    
    try:
        if checked:
            user: User = User.objects.get(id=request.user.id, is_deleted=False)
            if user:
                user.is_verified = True
                user.save()
                return redirect('home')
    except:
        logger.error("User not found")
        pass
    
    if request.user.is_authenticated and request.user.is_verified:
        return redirect('home')
    
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            user: User = User.objects.get(
                id=int(request.user.id),
                phone=str(request.user.phone),
                is_deleted=False,
                eskiz_code=str(code)
            )
            user.is_verified = True
            user.save()
        
        except User.DoesNotExist:
            error: str = "Tasdiqlash kodi xato, qaytadan yuboring"
            logger.error(f"Error during user verification {error}")
            messages.error(request, error)
            return redirect('my-account')
        
        if user is not None and user.is_verified:
            messages.success(request, f"{user.name} web sahifamizga xush kelibsiz!")
            login(request, user)
            return redirect('home')
    
    return render(request, 'users/login.html', {'page': page})


def logoutView(request) -> None:
    """Remove the authenticated user's ID from the request and flush their session data"""
    logout(request)
    
    return redirect('home')
