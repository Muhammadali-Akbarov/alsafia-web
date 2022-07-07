from random import choice
from cryptography.fernet import Fernet


def generate_code() -> str:
    """Generates random verify code"""
    password: str = ''
    numbers: tuple = ('1234567890')
    
    for _ in range(4):
        password+=choice(choice(numbers))
        
    return password


def cryptography_fearnet_endcoder(password: str) -> str:
    """This function to encrypt password"""
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encMessage = fernet.encrypt(password.encode())
    
    return encMessage, key


def cryptography_fearnet_decoder(password: str, key: str) -> str:
    """This function to decrypt password"""
    fernet = Fernet(key)
    
    return fernet.decrypt(password).decode()


