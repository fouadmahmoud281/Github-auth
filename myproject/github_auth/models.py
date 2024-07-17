# github_auth/models.py

from django.contrib.auth.models import User
from django.db import models


class GitHubToken(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  access_token = models.CharField(max_length=255)

  def __str__(self):
    return self.user.username
