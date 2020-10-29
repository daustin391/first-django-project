from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("blogs.urls")),
    path("register", views.register),
    path("login", views.login),
    path("users/new", views.register),
    path("users", views.index),
]
