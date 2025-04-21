from django.db import models
from accounts.models import User  # Assuming you have a custom User model in accounts app
# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    date = models.DateField()  # Only the date
    time = models.TimeField()  # Only the time
    
    venue = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    card_image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='events')
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
