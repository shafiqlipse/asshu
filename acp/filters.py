import django_filters
from .models import ConventionRegistration


class ConventionRegistrationFilter(django_filters.FilterSet):

    # Add more fields as needed

    class Meta:
        model = ConventionRegistration
        fields = [
            "country",
            "designation",
            "registering_for","is_icp_member",
        ]  # Add all fields you want to filter on
