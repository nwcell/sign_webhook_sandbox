"""Admin for webhook listener app."""
from django.contrib import admin

from .models import Listener, ListenerLog


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that prevents modifications through the admin.
    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    Source: https://gist.github.com/aaugustin/1388243
    """

    actions = None

    # We cannot call super().get_fields(request, obj) because that method calls
    # get_readonly_fields(request, obj), causing infinite recursion. Ditto for
    # super().get_form(request, obj). So we  assume the default ModelForm.
    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them.
    def has_change_permission(self, request, obj=None):
        return request.method in ["GET", "HEAD"] and super().has_change_permission(
            request, obj
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Listener)
class ListenerAdmin(ReadOnlyModelAdmin):
    """View valid listeners"""

    fields = ("url", "id", "user")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superuser or user.has_perm("listener.view_all_listeners"):
            return qs
        return qs.filter(user=user)


@admin.register(ListenerLog)
class ListenerLogAdmin(ReadOnlyModelAdmin):
    """View logs for a user's listener."""

    fields = ("id", "created_at", "headers_prettified", "data_prettified")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.has_perm("listener.view_all_logs"):
            return qs
        return qs.filter(listener__user=request.user)
