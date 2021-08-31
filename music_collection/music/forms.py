from django.forms import ModelForm
from .models import Rating, MusicAlbum

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review','stars','music']


class MusicForm(ModelForm):
    class Meta:
        model = MusicAlbum
        fields = ['performer', 'name_cd', 'publisher', 'year', 'info', 'category_models', 'cover', 'availability']
