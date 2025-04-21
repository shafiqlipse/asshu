from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from teachers.views import *
from base.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    # venues
    path("",home,name='home'),
    path("about_us",about,name='about'),
   path('post/article/<int:id>/', post, name='post'),
    # path("",home,name='home'),
    path("auth/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("teachers/", include("teachers.urls")),
    path("articles/", include("articles.urls")),
    path("events/", include("events.urls")),
    
    # ckeditor urls

    path('tinymce/', include('tinymce.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
