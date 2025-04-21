from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [

    path('articles/', article_list, name='article-list'),
    path('article/<int:id>/', article_detail, name='article-detail'),
    path('article/create/', article_create, name='article-create'),
    path('article/<int:id>/edit/', article_edit, name='article-edit'),
    path('article/<int:id>/delete/', article_delete, name='article-delete'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
