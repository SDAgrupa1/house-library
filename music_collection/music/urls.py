from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import views

app_name = 'music-urls'
urlpatterns = [
    path('cds/', views.CdListView.as_view(), name='list-of-cds'),
    path('cds/<id>/', views.cds_dynamic_lookup_view, name='cd-bio'),
    path('rate/', views.rate_music, name='rate'),
    path('all_music_albums/', views.all_music_albums, name='all_music_albums'),
    path('new/', views.new_music_album, name='new'),
    path('edit/<int:id>/', views.edit_music_album, name='edit'),
    path('delete/<int:id>/', views.delete_music_album, name='delete'),
    path('performer/new/', views.new_performer, name='new_performer'),
    # path('performer/list/', views.PerformerTemplateView.as_view(), name='list_performer'),
    path('performer/list/', views.PerformerListView.as_view(), name='list_performer'),
    path('performer/edit/<int:id>/', views.edit_performer, name='edit_performer'),
    path('performer/delete/<int:id>/', views.delete_performer, name='delete_performer'),
    path('performer/list/<int:id>/', views.performer_dynamic_lookup_view, name='performer-bio')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
