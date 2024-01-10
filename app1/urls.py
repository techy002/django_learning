"""
URL configuration for P1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("hellow-world/", views.HelloWorld.as_view()),
    path("create-profile/", views.ProfileCreateApi.as_view()),
    path("view-all-profile/", views.AllProfileViewApi.as_view()),
    path("view-profile/<int:pk>/", views.ProfileViewApi.as_view()),
    path("update-profile/<int:pk>/", views.ProfileUpdateApi.as_view()),
    path("delete-profile/<int:pk>/", views.ProfileDeleteApi.as_view()),
    path("retrive-profile/<int:pk>/", views.ProfileApi.as_view()),
]
