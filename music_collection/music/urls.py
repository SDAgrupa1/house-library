from django.urls import path

from . import views

app_name = 'music-urls'
urlpatterns = [
    path('cds/', views.CdTemplateView.as_view(), name='list-of-cds'),
    path('cds/<id>/', views.cds_dynamic_lookup_view, name='cd-bio'),
    path('rate/',views.rate_music, name='rate')
]
