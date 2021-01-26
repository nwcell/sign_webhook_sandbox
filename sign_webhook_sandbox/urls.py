"""Sign Webhook Sandbox URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


admin.site.site_header = "Sign Toolbox"
admin.site.site_title = "Sign Toolbox by Adobe"
admin.site.index_title = "Sign Toolbox"

urlpatterns = [
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("", admin.site.urls),
    # path("admin_password_reset")
    path("api/listener/", include("listener.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
]
