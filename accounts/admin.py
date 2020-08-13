from django.contrib import admin

# Register your models here.
from .models import profile,city

admin.site.register(profile)
admin.site.register(city)