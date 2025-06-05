from django import forms
from dashboard.models import *
from .models import *


class ConventionRegistrationForm(forms.ModelForm):
    class Meta:
        model = ConventionRegistration
        fields = [
            "title",
            "first_name",
            "surname",
            "badge_name",
            "certificate_name",
            "school_institution",
            "designation",
            "country",
            "city",
            "telephone",
            "mobile",
            "email",
            "photo",
            "passport_number",
            "registering_for",
            "is_icp_member",
            "dietary",
            "dietary_other",
            "attend_cocktail",
            "attend_dinner",
            "bringing_accompanying_person",
            "payment_method",
            "billing_company",
            "billing_contact_person",
            "billing_contact_number",
            "billing_email",
            "billing_address",
            "emergency_contact",
            "additional_info",
            "accept_social_media",
            "popia_acknowledged",
            "share_info_with_delegates",
    
        ]


