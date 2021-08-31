from os import name
from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import CustomerUserManager
from django.utils.translation import gettext_lazy as _
from .validators import PHONE_NUMBER_REGEX
# Create your models here.

class role (models.Model):
    ROLE_CHOICE = (
        ('cu','customers'),
        ('su','supporter'),
        ('se','sellers')
    )

    name = models.CharField(max_length=2,choices=ROLE_CHOICE)

class customeUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=35,verbose_name="نام")
    phone_number = models.CharField(max_length=12,validators=[PHONE_NUMBER_REGEX],verbose_name="شماره موبایل",unique=True)
    email = models.EmailField(blank=True,null=True ,unique=True,verbose_name="ایمیل")
    is_staff = models.BooleanField(default=False,verbose_name="وضع کارمندی")
    is_active = models.BooleanField(default=True,verbose_name="فعال هست")
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.ManyToManyField(role)

    USERNAME_FIELD = 'phone_number'
    

    objects = CustomerUserManager()

    def __str__(self):
        return self.name

