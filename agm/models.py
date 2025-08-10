from django.db import models
from accounts.models import District,Region

# Create your models here.




class Member(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to="member_photos/",
    )

    district = models.ForeignKey(
        District,
        related_name="agm_district",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        Region,
        related_name="agm_region",
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
    designation = models.CharField(
        max_length=40,
        choices=[
            ("Principal", "Principal"),
            ("HeadMember", "HeadMember"),
            ("Deputy HeadMember", "Deputy HeadMember"),
        ],
    )

    def __str__(self):
        return self.first_name

