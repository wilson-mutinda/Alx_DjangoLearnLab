from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.FileField(upload_to='profiles', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=True, related_name='following', blank=True)

    def __str__(self):
        return self.username