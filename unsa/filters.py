import django_filters
from .models import Student
from accounts.models import Region
from django import forms


class StudentFilter(django_filters.FilterSet):
    id_range = django_filters.RangeFilter(field_name='id')
    # Add more fields as needed

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
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=Student.objects.all(),
        label="Name",
        method="filter_by_full_name",
        widget=forms.SelectMultiple(
            attrs={"class": "form-control js-example-basic-multiple-name"}
        )
    )

    class Meta:
        model = Student
        fields = [
            "region","name",
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