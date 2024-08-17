from django import forms
from dashboard.models import *
from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "designation",
            "photo",
            "contact",
            "region",
            "district",
            "gender",
            "school",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "school": forms.TextInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control"}),
            "designation": forms.Select(attrs={"class": "form-control"}),
            "region": forms.Select(attrs={"class": "form-control"}),
            "district": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields["photo"].widget.attrs["onchange"] = "displayImage(this);"
