from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name = 'login'),
    path('logout', views.LogoutUser, name = 'logout'),
    path('register', views.RegisterPage, name = 'register'),

    path('userprofile/<int:id>', views.UserProfile, name='userprofile'),
    path('updateuser/<int:id>', views.UpdatUser, name = 'updateuser'),

    path('createroom', views.CreateRoom, name = 'createroom'),
    path('room/<int:id>', views.RoomPage, name = 'room'),
    path('updateroom/<int:id>', views.UpdateRoom, name = 'updateroom'),
    path('delete-room/<int:pk>', views.DeleteRoom, name = 'delete-room'),

    path('topics', views.TopicsPage, name = 'topics'),
    path('activity', views.ActivitiesPage, name = 'activity'),
    path('delete-message/<int:pk>', views.DeleteMessage, name = 'delete-message'),


    path('', views.home, name = 'home'),
]