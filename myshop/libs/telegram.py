import requests

from django.conf import settings


class TeleBotClient:
    __sendMessage = "/sendMessage"

    def __init__(self, base_url: str, token: str, chat_id: str) -> None:
        self.__token = token
        self.__chat_id = chat_id
        self.__base_url = base_url
        self.__main_url = f'{self.__base_url}{self.__token}'

    def send_message(self, text: str) -> dict:
        params = {
            'text': text,
            'chat_id': self.__chat_id,
            'parse_mode': 'HTML'
        }
        
        return requests.post(f'{self.__main_url}{self.__sendMessage}', params)


telebot = TeleBotClient(
    **settings.MYSERVICE.get('telebot')
)