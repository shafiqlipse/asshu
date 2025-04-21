from django import forms
from .models import Event
from tinymce.widgets import TinyMCE

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'card_image', 'cover_image', 'date', 'time', 'event_category', 'venue', 'is_active', 'address', 'city']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'card_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'event_category': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags (comma separated)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags (comma separated)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags (comma separated)'}),# ✅ Correct widgets for date and time
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Event date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'placeholder': 'Event time'
            }),
        }