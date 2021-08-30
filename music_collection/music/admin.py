from django.contrib import admin
from .models import MusicAlbum, Category, Availability, Rating


admin.site.register(MusicAlbum)
admin.site.register(Category)
admin.site.register(Availability)
admin.site.register(Rating)
