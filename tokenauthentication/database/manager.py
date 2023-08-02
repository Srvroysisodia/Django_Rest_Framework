# Importing required libraries
#Signals For Auto Token Gen As User Created
from django.conf import settings 
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
#BaseUserManager
from django.contrib.auth.models import BaseUserManager

#Token Creation Using Signals,As User created Token Also created Simoultaneously
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


# Creating a User Manager Class for creating a user or Superuser
class UserManager(BaseUserManager):
    
    #Overriding the deafult create_user class
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')
        user = self.create_user(email,password,**extra_fields)
        return user 