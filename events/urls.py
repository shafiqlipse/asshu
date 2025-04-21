from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [

    path('events/', event_list, name='event-list'),
    path('event/<int:id>/', event_detail, name='event-detail'),
    path('event/create/', event_create, name='event-create'),
    path('event/<int:id>/edit/', event_edit, name='event-edit'),
    path('event/<int:id>/delete/', event_delete, name='event-delete'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
