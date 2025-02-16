# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import *
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserCreateForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['name', 'username', 'email', 'password1', 'password2']

# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'
#         exclude = ['host', 'members']

# class UserFrom(ModelForm):
#     class Meta:
#         model = User
#         fields = ['avator', 'name', 'username', 'email', 'bio']