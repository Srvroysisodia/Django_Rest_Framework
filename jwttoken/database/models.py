from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator
from .manager import UserManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=250,null=False)
    last_name = models.CharField(max_length=250,null=False)
    email = models.EmailField(null=False,unique=True)
    mobile_regex= RegexValidator(regex="^[0-9]{10,15}$",message="Wrong Contact number!")
    contact_no = models.CharField(validators=[mobile_regex],max_length=14,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = "email"