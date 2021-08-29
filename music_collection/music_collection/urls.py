from django.contrib import admin
from django.urls import path, include


app_name = 'main-urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('music/', include('music.urls')),
]
