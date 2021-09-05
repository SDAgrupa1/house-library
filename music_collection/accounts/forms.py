from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    about_me = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    linkedin_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'about_me', 'facebook_url',
                   'instagram_url', 'linkedin_url']


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    about_me = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    linkedin_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    profile_pic = forms.ImageField(label=('Avatar'), required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'about_me', 'facebook_url', 'instagram_url',
                  'linkedin_url', 'profile_pic']



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']