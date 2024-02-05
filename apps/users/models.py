import os
from django.db import models
from utils.image_path import upload_avatar_for_user
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    display_name = models.CharField(
        max_length=50,
        verbose_name='Отображаемое имя',
    )
    avatar = models.ImageField(
        upload_to=upload_avatar_for_user,
        verbose_name='Аватар',
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.avatar.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.username

