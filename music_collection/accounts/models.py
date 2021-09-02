from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about_me = models.TextField()
    profile_pic = models.ImageField(upload_to="music_collection/my_media/profile_pic", null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True, )
    instagram_url = models.CharField(max_length=255, null=True, blank=True, )
    linkedin_url = models.CharField(max_length=255, null=True, blank=True, )

    def __str__(self):
        return str(self.user)

