from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .customusermanager import CustomUserManager
from django.utils import timezone

# models: Used to define database models.
# AbstractBaseUser: Provides basic authentication fields (password, last login).
# PermissionsMixin: Adds permission-related fields and methods.
# timezone: Used to handle timestamps.

# AbstractBaseUser: Provides authentication-related fields (password, last login).
# PermissionsMixin: Adds Django’s permission framework.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=250, blank=True, default='')

    user_profile = models.ImageField(upload_to="userprofile", null=True, default="avatat.svg")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    joined_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]

# email = "john.doe@example.com"
# print(email.split('@'))  # Output: ['john.doe', 'example.com']
# print(email.split('@')[0])  # Output: 'john.doe'
