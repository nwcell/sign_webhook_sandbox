from django.contrib import admin
from .models import ListenerLog


@admin.register(ListenerLog)
class ListenerLogAdmin(admin.ModelAdmin):
    readonly_fields=('id', 'data', 'created_at')
