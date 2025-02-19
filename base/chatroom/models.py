from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanager import CustomUserManager
from django.utils import timezone

# Create your models here.

# models: Used to define database models.
# AbstractBaseUser: Provides basic authentication fields (password, last login).
# PermissionsMixin: Adds permission-related fields and methods.
# timezone: Used to handle timestamps.

# AbstractBaseUser: Provides authentication-related fields (password, last login).
# PermissionsMixin: Adds Django’s permission framework.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=250, blank=True,)
    user_bio = models.TextField(blank=True, null=True)

    user_profile = models.ImageField(upload_to="userprofile", null=True, default="userprofile/avatar.svg")

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



class Topic(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(CustomUser, related_name='username', on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, related_name='topicname',on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user = models.ForeignKey(CustomUser, related_name='usermessage', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='roommessage', on_delete=models.CASCADE)
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.comment[0:50]