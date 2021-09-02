from django.forms import ModelForm, TextInput, Select, Textarea
from .models import Rating, MusicAlbum


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'stars', 'music']


class MusicForm(ModelForm):
    class Meta:
        model = MusicAlbum
        fields = ['performer', 'name_cd', 'publisher', 'year', 'info', 'category_models', 'cover', 'availability']

        widgets = {
            'performer': TextInput(attrs={'class': 'form-control'}),
            'name_cd': TextInput(attrs={'class': 'form-control'}),
            'publisher': TextInput(attrs={'class': 'form-control'}),
            'year': TextInput(attrs={'class': 'form-control'}),
            'info': Textarea(attrs={'class': 'form-control'}),
            'category_models': Select(attrs={'class': 'form-control'}),
            'cover': TextInput(attrs={'class': 'form-control'}),
            'availability': Select(attrs={'class': 'form-control'}),
        }
