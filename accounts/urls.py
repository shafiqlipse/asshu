from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path("login/",user_login,name='login'),
    path("reset_password/",change_password,name='password_reset'),
    path("register/",school_registration,name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
