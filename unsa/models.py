from django.db import models
from accounts.models import District,Region

# Create your models here.




class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to="student_photos/",
    )

    district = models.ForeignKey(
        District,
        related_name="unsa_district",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    contact = models.CharField(max_length=15)
    school = models.CharField(max_length=125)

    gender = models.CharField(
        max_length=14,
        choices=[("Male", "Male"), ("Female", "Female")],
    )


    def __str__(self):
        return self.first_name

