"""Urls for the Listener app."""
from django.urls import path

from . import views

urlpatterns = [
    path("<uuid:listener_id>", views.listener, name="listener"),
]
