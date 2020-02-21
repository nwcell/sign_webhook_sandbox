import uuid
from django.db import models

# Create your models here.
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name