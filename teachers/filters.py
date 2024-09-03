import django_filters
from .models import Teacher


class TeacherFilter(django_filters.FilterSet):
    id_range = django_filters.RangeFilter(field_name='id')
    # Add more fields as needed

    class Meta:
        model = Teacher
        fields = [
            "district",
            "designation",
            "gender","id_range",
        ]  # Add all fields you want to filter on
