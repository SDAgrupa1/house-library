from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'),
         name='change_password'),
    path('password_success', views.password_success, name='password_success'),
]