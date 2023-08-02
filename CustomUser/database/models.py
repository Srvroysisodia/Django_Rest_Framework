from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from database.manager import UserManager
from django.core.validators import RegexValidator
import uuid
import os
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Meta class to store timezone info


class Timezone(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
# Meta Class for soft delete manage -----------------------------------------


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_del=False)

# Meta Class to Soft-Delete the records in Every Table


class SoftDeleteModel(models.Model):

    is_del = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_del = True
        self.save()

    def restore(self):
        self.is_del = False
        self.save()

    class Meta:
        abstract = True

# User model Class for creating a user ans


class User(AbstractBaseUser, PermissionsMixin, Timezone):

    user_type = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin'),
        ('Others', 'Others')
    ]

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    subject = models.CharField(
        max_length=255, blank=True, null=True)
    mobile_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Wrong Contact number!")
    contact_no = models.CharField(
        validators=[mobile_regex], max_length=14, blank=True, null=True)
    user_profile = models.CharField(
        max_length=255, choices=user_type, default=user_type[0][0], null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_approve = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

class EnquiryEmail(Timezone):
    e_id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def _str_(self):
        return self.sender_name


class EmailOTP(models.Model):
    otp = models.IntegerField()
    email = models.EmailField()