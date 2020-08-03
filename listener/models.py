import uuid
from django.db import models

# Create your models here.
class ListenerLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        timestamp = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return f'{timestamp} | {self.id}'