"""Listener models"""
# pylint: disable=unused-argument,no-name-in-module

import uuid
import json

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.urls import reverse

from pygments import highlight
from pygments.lexers.data import JsonLexer
from pygments.formatters import HtmlFormatter


class Listener(models.Model):
    """
    Registered listeners.

    There is one for every :model:`auth.User` in the system.

    Each listener will post a record to :model:`listener.ListenerLog`
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} - {self.url}"

    class Meta:
        ordering = ["user"]
        permissions = (("view_all_listeners", "Can view all webhook listeners"),)

    @property
    def url(self):
        """Target url for new webhooks."""
        return reverse("listener", args=(self.pk,))


class ListenerLog(models.Model):
    """Log of every :model:`listener.Listener` event that hits the system."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listener = models.ForeignKey(Listener, on_delete=models.CASCADE)
    headers = models.JSONField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        permissions = (("view_all_logs", "Can view all webhook listener logs"),)

    def __str__(self):
        timestamp = self.created_at.strftime("%m/%d/%y %H:%M:%S")
        if self.webhook_name:
            return f"{self.listener.user} | {timestamp} | {self.webhook_name}"
        return f"{self.listener.user} | {timestamp} | <Non Conforming>"

    @property
    def webhook_name(self):
        """Name assigned to the webhook."""
        return self.data.get("webhookName")

    def json_prettify(self, data):
        """Function to display pretty version of our data"""
        response = json.dumps(data, sort_keys=True, indent=2)
        formatter = HtmlFormatter(style="colorful")
        response = highlight(response, JsonLexer(), formatter)
        style = f"<style>{formatter.get_style_defs()}</style><br>"
        return mark_safe(style + response)

    @property
    def data_prettified(self):
        """Function to display pretty version of our data"""
        return self.json_prettify(self.data)

    @property
    def headers_prettified(self):
        """Function to display pretty version of our data"""
        return self.json_prettify(self.headers)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_listener(sender, instance, created, **kwargs):
    """Create listener, when users are created."""
    if created:
        Listener.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_listener(sender, instance, **kwargs):
    """Update listener, when the user is updated."""
    instance.listener.save()
