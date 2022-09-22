from redis import StrictRedis

from django.conf import settings

from myshop.libs.telegram import telebot

class Redis:
    __EXPIRE_TIME = 100
    
    def __init__(self) -> None:
        self.__redis = StrictRedis(**(settings.MYSERVICE.get('redis')))

    def _set_verify_code(self, session_id: str, phone_number: str = None, verify_code: str = None) -> str:
        """This method is helps to set the verification code for a given phone number"""
        cache_date: dict = {
            'name': session_id,
            'time': self.__EXPIRE_TIME,
            'value': phone_number,
        }
        self.__redis.setex(**cache_date)

    def _is_already_sent(self, phone_number: str) -> bool:
        """This method is checks if the sms verify code already sent or not"""
        return bool(self.__redis.exists(phone_number))

    def _get_phone_number(self, session_id: str) -> str:
        """This method uses to get the phone number with session id"""
        return self.__redis.get(session_id)
    
    
    def _check_code_in_redis(self, session_id: str, code: int) -> bool:
        """This method checks if the code is already in the redis with session id"""
        code_in_redis: str = self.__redis.get(session_id)
        telebot.send_message(
            f"New code {code_in_redis}",
            _type=telebot.TYPE_WARNINGS
        )
        if code_in_redis.decode("utf-8") == code:
            return True
        
        return False


redis = Redis()
