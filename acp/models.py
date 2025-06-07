from django.db import models
from django.core.validators import FileExtensionValidator


class ConventionRegistration(models.Model):
    ICP_EVENT_CHOICES = [
        ('council', 'ICP Council | August 25 - 28, 2025'),
        ('convention', 'ICP Convention | August 25 - 28, 2025'),
        ('combined', 'Combined ICP Council & ICP World Convention'),
    ]

    MEMBER_STATUS = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]


    DIETARY_CHOICES = [
        ('none', 'None'),
        ('gluten_free', 'Gluten-Free'),
        ('halal', 'Halal'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('other', 'Other'),
    ]


    DESIGNATIONS = [
        ('Principal', 'Principal'),
        ('Acting Principal', 'Acting Principal'),
        ('Deputy Principal', 'Deputy Principal'),
        ('Acting deputy principal', 'Acting deputy principal'),
        ('Retired principal', 'Retired principal'),
        ('Head of Department', 'Head of Department'),
        ('other', 'Other'),
    ]

    PAYMENT_OPTIONS = [
        ('bank', 'Bank Transfer / EFT'),
        ('card', 'Credit Card'),
    ]

    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    badge_name = models.CharField(max_length=100)
    certificate_name = models.CharField(max_length=100)
    school_institution = models.CharField(max_length=255)
    designation = models.CharField(max_length=100,choices=DESIGNATIONS)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    passport_number = models.CharField(max_length=50, blank=True)
    
    registering_for = models.CharField(max_length=20, choices=ICP_EVENT_CHOICES)
    is_icp_member = models.CharField(max_length=3, choices=MEMBER_STATUS)
    dietary = models.CharField(max_length=20, choices=DIETARY_CHOICES,null=True, blank=True)
    dietary_other = models.CharField(max_length=100, blank=True,null=True)

    attend_cocktail = models.CharField(max_length=3, choices=MEMBER_STATUS,null=True, blank=True)
    attend_dinner = models.CharField(max_length=3, choices=MEMBER_STATUS,null=True, blank=True)
    bringing_accompanying_person = models.CharField(max_length=3, choices=MEMBER_STATUS,null=True, blank=True)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_OPTIONS,null=True, blank=True)

    billing_company = models.CharField(max_length=255,null=True, blank=True)
    billing_contact_person = models.CharField(max_length=100,null=True, blank=True)
    billing_contact_number = models.CharField(max_length=20,null=True, blank=True)
    billing_email = models.EmailField(null=True, blank=True)
    billing_address = models.CharField(max_length=100,null=True, blank=True)

    emergency_contact = models.CharField(max_length=100,null=True, blank=True)
    additional_info = models.TextField(blank=True)

    accept_social_media = models.BooleanField(default=False)
    popia_acknowledged = models.BooleanField(default=False)
    share_info_with_delegates = models.CharField(max_length=3, choices=MEMBER_STATUS)
    photo = models.ImageField(
        upload_to="student_photos/",
        validators=[FileExtensionValidator(
            allowed_extensions=["png", "jpg", "jpeg"])],null=True, blank=True       
    )
   

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.registering_for}"
