import django_filters
from .models import Member
from accounts.models import Region
from django import forms


class MemberFilter(django_filters.FilterSet):
    id_range = django_filters.RangeFilter(field_name='id')
    # Add more fields as needed
    designation = django_filters.ChoiceFilter(
        choices=[
  ("Principal", "Principal"),
            ("Headteacher", "Headteacher"),
            ("Deputy Headteacher", "Deputy Headteacher")
        ],
        label="Designation",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )
    region = django_filters.ModelChoiceFilter(
        queryset=Region.objects.all(),
        label="Region",
        widget=forms.Select(attrs={"class": "form-control js-example-basic-single"})
    )
    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    status = django_filters.ChoiceFilter(
        choices=[("Pending", "Pending"), ("Verified", "Verified"), ("Unverified", "Unverified")],
        label="Status",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Member.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )

    class Meta:
        model = Member
        fields = [
            "region",
            "designation","status","name",
            "gender","id_range",
        ]  # Add all fields you want to filter on
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show "First Last" in the dropdown
        self.filters['name'].field.label_from_instance = (
            lambda obj: f"{obj.first_name} {obj.last_name}"
        )

    def filter_by_full_name(self, queryset, name, value):
        """Filter by selected member IDs, while keeping other filters."""
        if value:
            queryset = queryset.filter(id__in=[v.id for v in value])
        return queryset