from django.contrib import admin

from .models import Music, Category, Availability, Rating, Performer, Profile #profie should go to accounts app


admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Availability)
admin.site.register(Rating)
admin.site.register(Performer)
admin.site.register(Profile)
