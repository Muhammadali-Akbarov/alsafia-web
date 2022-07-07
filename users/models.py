from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractUser):
    _USER_ERROR_MESSAGE = "Bunday foydalanuvchi topilmadi"
    
    """User model."""
    username = None
    phone_regex = RegexValidator(regex=r'^998[0-9]{2}[0-9]{7}$', message="Faqat o'zbek raqamlarigina tasdiqlanadi")
    phone = models.CharField(_('Telefon raqam'), validators=[phone_regex], max_length=17, unique=True)
    eskiz_id = models.CharField(max_length=20, null=True, blank=True)
    key = models.CharField(max_length=40, null=True, blank=False)
    eskiz_code = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False, blank=True)
    is_deleted = models.BooleanField(default=False, blank=True)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    @property
    def isVerified(self):
        return self.is_verified