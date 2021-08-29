from django.contrib import admin
from django.urls import path, include

from . import views_basic

app_name = 'main-urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views_basic.home_view, name='home'),
    path('about-us/', views_basic.about_us_view, name='about-us'),
    path('music/', include('music.urls')),
    path('error-404/', views_basic.error_404_view, name='error-404'),
]
