from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about_me = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to='music_collection/my_media/profile_pic', default='music_collection/static/img/hl-logo.jpg')
    facebook_url = models.CharField(max_length=255, null=True, blank=True, )
    instagram_url = models.CharField(max_length=255, null=True, blank=True, )
    linkedin_url = models.CharField(max_length=255, null=True, blank=True, )

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
