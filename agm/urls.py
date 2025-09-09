from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

from .views import *


urlpatterns = [
    # venues
    path("addmember/", Membera, name="addmember"),
    # path("teccred/", teccreditation, name="teccred"),
    path('export-csv/', export_csv, name='export_csv'),
    path("members/", Members, name="members"),
    path("member/<int:id>", member_details, name="member"),
    path("delete_member/<int:id>", member_delete, name="delete_member"),
    path("update_member/<int:id>", member_update, name="update_member"),
    path("activate_member/<int:id>", activate_member, name="activate_member"),
    # path("process-payment/", process_payment, name="process_payment"),  # Add this line
    # Add more URLs as ne
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
