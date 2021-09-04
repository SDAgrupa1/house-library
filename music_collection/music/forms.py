from django.forms import ModelForm, TextInput, Select, Textarea, FileInput, NumberInput
from .models import Rating, MusicAlbum, Performer


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['stars','music']
        
        widgets = {
            'stars': NumberInput(attrs={'class': 'form-control'}),
            'music': Select(attrs={'class': 'form-control'}),
        }


class MusicForm(ModelForm):
    class Meta:
        model = MusicAlbum
        fields = ['name_cd', 'publisher', 'year', 'info', 'category_models', 'cover', 'availability']

        widgets = {
            'name_cd': TextInput(attrs={'class': 'form-control'}),
            'publisher': TextInput(attrs={'class': 'form-control'}),
            'year': TextInput(attrs={'class': 'form-control'}),
            'info': Textarea(attrs={'class': 'form-control'}),
            'category_models': Select(attrs={'class': 'form-control'}),
            'cover': FileInput(attrs={'class': 'form-control'}),
            'availability': Select(attrs={'class': 'form-control'}),
        }

        
class PerformerForm(ModelForm):
    class Meta:
        model = Performer
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }
