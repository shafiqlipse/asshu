from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from teachers.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    # venues
    path("teachers/", include("teachers.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
