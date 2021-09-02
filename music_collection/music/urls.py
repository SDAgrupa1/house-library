from django.urls import path

from . import views
from .views import all_music_albums, new_music_album, edit_music_album, delete_music_album

app_name = 'music-urls'
urlpatterns = [
    path('cds/', views.CdTemplateView.as_view(), name='list-of-cds'),
    path('cds/<id>/', views.cds_dynamic_lookup_view, name='cd-bio'),
    path('rate/', views.rate_music, name='rate'),
    path('all_music_albums/', all_music_albums, name='all_music_albums'),
    path('new/', views.new_music_album, name='new'),
    path('edit/<int:id>/', views.edit_music_album, name='edit'),
    path('delete/<int:id>/', views.delete_music_album, name='delete'),
]
