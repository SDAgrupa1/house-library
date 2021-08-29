from django.contrib import admin
from .models import Music, Category, Availability, Rating


admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Availability)
admin.site.register(Rating)
