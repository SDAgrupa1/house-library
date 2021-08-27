from django.contrib import admin
from .models import Music, Category, Availability


admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Availability)
