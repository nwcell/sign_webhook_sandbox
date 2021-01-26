"""Sign Webhook Sandbox URL Configuration"""
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Sign Toolbox"
admin.site.site_title = "Sign Toolbox by Adobe"
admin.site.index_title = "Sign Toolbox"

urlpatterns = [
    path("", admin.site.urls),
    path("api/listener/", include("listener.urls")),
]
