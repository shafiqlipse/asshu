from django.db import models
from tinymce.models import HTMLField
from accounts.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    featured_image = models.ImageField(
        upload_to="featured_images/",
    )
    category = models.ForeignKey(
        Category,
        related_name="articles",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    tags = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, verbose_name="author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title