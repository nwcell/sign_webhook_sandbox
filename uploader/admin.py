from django.contrib import admin
from .models import File

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(File)