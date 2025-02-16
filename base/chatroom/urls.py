from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name = 'login'),
    path('logout', views.LogoutUser, name = 'logout'),
    path('register', views.RegisterPage, name = 'register'),
    path('updateuser/<int:id>', views.UpdatUser, name = 'updateuser'),

    path('', views.home, name = 'home'),
    path('header', views.Header, name = 'header')
]