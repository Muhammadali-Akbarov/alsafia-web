from requests import request
from requests.structures import CaseInsensitiveDict

from django.conf import settings

from myshop.libs.telegram import telebot
from myshop.models.sms import SMSClient as sms_model


class SMSClient:
    __GET = 'get'
    __POST = "post"
    __PATCH = "patch"
    __DELETE = "delete"
    __CONTACT = "contact"
    
    __AUTH_USER = "auth/user"
    __AUTH_LOGIN = "auth/login"
    __AUTH_REFRESH = "auth/refresh"
    __AUTH_INVALIDATE = "auth/invalidate"
    __AUTH_TOKEN_ERROR = "⚠️ Error creating sms client token\n"

    def __init__(self, base_url: str, email: str, password: str, group: str) -> None:
        self.email = email
        self.password = password
        self.base_url = base_url
        self.group = group
        
        self.headers: CaseInsensitiveDict = CaseInsensitiveDict()
    
    def __request(self, api_path: str, data: dict = None, **kwargs) -> dict:
        """Custom request method"""
        context: dict = {
            "data": data,
            "method": kwargs.pop("method", None),
            "headers": kwargs.pop("headers", None),
            "url": self.base_url + api_path,
        }
        resp = request(**context).json()
        print(resp)
        return resp

    def _auth(self) -> dict:
        """Для авторизации используйте этот API, возвращает токен"""
        data: dict = {
            "email": self.email,
            "password": self.password,
        }
        context: dict = {
            "data": data,
            "method": self.__POST,
            "api_path": self.__AUTH_LOGIN
        }
        token: str = self.__request(**context).get('data').get('token')
        if len(token) <= sms_model.AUTH_TOKEN_LEN:
            try:
                sms_model.objects.get_or_create(token=token)
                
            except Exception as e:
                context: dict = {
                    "text": f"{self.__AUTH_TOKEN_ERROR}\n{e}",
                    "_type": telebot.TYPE_WARNINGS
                }
                
                telebot.send_message(**context)
            
        return self.__request(**context)

    def __refresh_token(self) -> dict:
        """Обновляет текущий токен"""
        self.headers["Authorization"] = f"Bearer {self.get_sms_client_token()}"
        
        context: dict = {
            "headers": self.headers,
            "method": self.__PATCH,
            "api_path": self.__AUTH_REFRESH
        }

        return self.__request(**context)

    def __invalidate_token(self) -> dict:
        """Удаляет текущий токен"""
        self.headers["Authorization"] = f"Bearer {self.get_sms_client_token()}"
        
        context: dict = {
            "headers": self.headers,
            "method": self.__DELETE,
            "api_path": self.__AUTH_INVALIDATE
        }

        return self.__request(**context)
    
    def _get_my_user_info(self) -> dict:
        """Возвращает все данные о пользователе"""
        self.headers["Authorization"] = f"Bearer {self.get_sms_client_token()}"
        
        context: dict = {
            "method": self.__GET,
            "headers": self.headers,
            "api_path": self.__AUTH_USER
        }
        
        return self.__request(**context)

    def _add_sms_contact(self, name: str, phone_number: str) -> dict:
        """Добавляет контакт в базу данных"""
        self.headers["Authorization"] = f"Bearer {self.get_sms_client_token()}"
        
        data: dict = {
            'name': name,
            'email': self.email,
            'group': self.group,
            'mobile_phone': phone_number,
        }
        context: dict = {
            "data": data,
            "method": self.__POST,
            "headers": self.headers,
            "api_path": self.__CONTACT
        }
        return self.__request(**context)
    
    @staticmethod
    def get_sms_client_token() -> str:
        """This method returns token from database"""
        return sms_model.objects.only('token').last().token
    
        

sms = SMSClient(
    **settings.MYSERVICE.get('sms_service')
)
