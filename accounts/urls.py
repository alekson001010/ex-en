from django.contrib.auth import login, authenticate
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', registerUser, name='register'),
    path('login/', loginUser, name='login'),
    path('success/', success, name='success'),
    path('set_data/', set_data, name='set_data'),
    path('set_weight/', set_weight, name='set_weight'),
    path('logout/', logoutUser, name="logout"),
    path('password-change/', passwordChange, name="password")
]