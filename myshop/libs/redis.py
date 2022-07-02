from redis import StrictRedis

from django.conf import settings


class Redis:
    __EXPIRE_TIME = 30

    def __init__(self) -> None:
        self.__redis = StrictRedis(**(settings.MYSERVICE.get('redis')))

    def _set_verify_code(self, phone_number: str, verify_code: str) -> str:
        """This method is helps to set the verification code for a given phone number"""
        cache_date: dict = {
            'name': phone_number,
            'time': self.__EXPIRE_TIME,
            'value': verify_code,
        }
        self.__redis.setex(**cache_date)

    def _is_already_sent(self, phone_number: str) -> bool:
        """This method is checks if the sms verify code already sent or not"""
        return bool(self.__redis.exists(phone_number))


redis = Redis()
