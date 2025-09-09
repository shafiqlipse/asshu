import django_filters
from .models import Member


class MemberFilter(django_filters.FilterSet):
    id_range = django_filters.RangeFilter(field_name='id')
    # Add more fields as needed

    class Meta:
        model = Member
        fields = [
            "district",
            "designation","status",
            "gender","id_range",
        ]  # Add all fields you want to filter on
