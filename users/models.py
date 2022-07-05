from django.db import models

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

from users.managers import UserManager


class User(AbstractUser):
    """User model."""
    username = None
    phone_regex = RegexValidator(regex=r'^998[0-9]{2}[0-9]{7}$', message="Faqat o'zbek raqamlarigina tasdiqlanadi")
    phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    objects = UserManager()