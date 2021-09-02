from django.forms import ModelForm
from .models import Rating, MusicAlbum, Performer


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'stars', 'music']


class MusicForm(ModelForm):
    class Meta:
        model = MusicAlbum
        fields = ['performer', 'name_cd', 'publisher', 'year', 'info', 'category_models', 'cover', 'availability']


class PerformerForm(ModelForm):
    class Meta:
        model = Performer
        fields = ['name']
