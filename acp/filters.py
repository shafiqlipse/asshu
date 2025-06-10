import django_filters
from .models import ConventionRegistration
from django import forms

class ConventionRegistrationFilter(django_filters.FilterSet):

    # Add more fields as needed
        
    designation = django_filters.ChoiceFilter(
        choices=[     ('Principal', 'Principal'),
        ('Acting Principal', 'Acting Principal'),
        ('Deputy Principal', 'Deputy Principal'),
        ('Acting deputy principal', 'Acting deputy principal'),
        ('Retired principal', 'Retired principal'),
        ('Head of Department', 'Head of Department'),
        ('other', 'Other')],
        label="Designation",
        widget=forms.Select(attrs={"class": "form-select"})
    )     
    registering_for = django_filters.ChoiceFilter(
        choices=[       ('council', 'ICP Council | August 25 - 28, 2025'),
        ('convention', 'ICP Convention | August 25 - 28, 2025'),
        ('combined', 'Combined ICP Council & ICP World Convention')],
        label="Registering For",
        widget=forms.Select(attrs={"class": "form-select"})
    )     
    is_icp_member = django_filters.ChoiceFilter(
        choices=[("Yes", "Yes"), ("No", "No")],
        label="ACP Member",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    country = django_filters.CharFilter(
        field_name="country",
        lookup_expr="icontains",
        label="Country",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter country"})
    )

    class Meta:
        model = ConventionRegistration
        fields = [
            "country",
            "designation",
            "registering_for","is_icp_member",
        ]  # Add all fields you want to filter on
        
