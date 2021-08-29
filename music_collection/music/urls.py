from django.urls import path
from . import views


urlpatterns = [
    path('cds/', views.CdTemplateView.as_view(), name='list-of-cds'),
    path('cds/<id>', views.cds_dynamic_lookup_view, name='cd-bio'),

]