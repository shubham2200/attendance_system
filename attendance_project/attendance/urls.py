from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_save , name='login_save' ),
    path('' , register, name='register'),
    path('dashboard/',dashbord , name='dashboard'),
    path('logout_user/' , logout_user , name='logout_user'),
    # path('save_register/' , save_register , name='save_register'),
]
