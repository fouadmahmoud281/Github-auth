from django.contrib import admin
from django.urls import path, include
from github_auth import views as github_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('github/callback/',
         github_views.github_callback,
         name='github_callback'),
    path('', github_views.home, name='home'),
]
