# github_auth/views.py

from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from github_auth.models import GitHubToken
from django.contrib.auth.decorators import login_required


@login_required
def github_callback(request):
  social_account = SocialAccount.objects.get(user=request.user,
                                             provider='github')
  token = social_account.socialtoken_set.first().token

  # Store or update the token in the database
  github_token, created = GitHubToken.objects.get_or_create(user=request.user)
  github_token.access_token = token
  github_token.save()

  return redirect('home')


def home(request):
  return render(request, 'github_auth/home.html')
