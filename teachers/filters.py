import django_filters
from .models import Teacher


class TeacherFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = Teacher
        fields = [
            "district",
            "designation",
            "gender",
        ]  # Add all fields you want to filter on
