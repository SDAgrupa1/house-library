from django.contrib import admin
from django.urls import path
from music import views
app_name = 'main-urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cds/', views.CdTemplateView.as_view(), name='list-of-cds'),
    path('cds/<id>', views.cds_dynamic_lookup_view, name='cd-bio'),
    path('add-rate/', views.rate_music, name='rate-music')
]
