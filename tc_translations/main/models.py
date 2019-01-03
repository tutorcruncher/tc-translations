from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField('Email Address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Version(models.Model):
    language = models.CharField('Language', max_length=255)
    users = models.ManyToManyField(User, blank=True)
    branch_name = models.CharField('Branch name', max_length=255)


class Change(models.Model):
    user = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, related_name='changes')
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='changes')
    msgid = models.TextField('String')
    msgstr = models.TextField('New Translation')
