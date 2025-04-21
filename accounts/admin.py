from django.contrib import admin
from accounts.models import *
from dashboard.models import *
from events.models import *
from articles.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(EventCategory)
admin.site.register(Event)
