from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

from .views import *


urlpatterns = [
    # venues
    path("addstudent/", studenta, name="addstudent"),
    # path("teccred/", teccreditation, name="teccred"),
    path('export-scsv/', export_scsv, name='export_scsv'),
    path("students/", students, name="students"),
    path("student/<int:id>", student_details, name="student"),
    path("delete_student/<int:id>", student_delete, name="delete_student"),
    path("update_student/<int:id>", student_update, name="update_student"),
    path("activate_student/<int:id>", activate_student, name="activate_student"),
    # path("process-payment/", process_payment, name="process_payment"),  # Add this line
    # Add more URLs as ne
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
