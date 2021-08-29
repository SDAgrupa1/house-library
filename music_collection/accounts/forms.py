from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileView(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), max_length=50)
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), max_length=50)
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), max_length=50)
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff',
                  'is_active', 'date_joined']

class EditForm():
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=255)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
