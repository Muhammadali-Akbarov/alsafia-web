from requests import request
from requests.structures import CaseInsensitiveDict

from django.conf import settings


class SMSClient:
    __POST = "post"
    __PATCH = "patch"
    __DELETE = "delete"

    __CONTACT = "contact"

    __AUTH_USER = "auth/user"
    __AUTH_LOGIN = "auth/login"
    __AUTH_REFRESH = "auth/refresh"
    __AUTH_INVALIDATE = "auth/invalidate"

    def __init__(self, base_url: str, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.base_url = base_url
        
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

    def __auth(self) -> dict:
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

        return self.__request(**context)

    def __refresh_token(self, token: str) -> dict:
        """Обновляет текущий токен"""
        self.headers["Authorization"] = f"Bearer {token}"
        
        context: dict = {
            "headers": self.headers,
            "method": self.__PATCH,
            "api_path": self.__AUTH_REFRESH
        }

        return self.__request(**context)

    def __invalidate_token(self, token: str):
        """Удаляет текущий токен"""
        context: dict = {
            "method": self.__DELETE,
            "api_path": self.__AUTH_INVALIDATE
        }

        return self.__request(**context)

    def _add_sms_contact(self, name: str, email: str, group: str, phone_number: str):
        """Добавляет контакт в базу данных"""
        data: dict = {
            'name': name,
            'email': email,
            'group': group,
            'mobile_phone': phone_number,
        }
        pass
        

sms = SMSClient(
    **settings.MYSERVICE.get('sms_service')
)
