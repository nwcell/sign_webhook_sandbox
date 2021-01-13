# Generated by Django 3.1.4 on 2021-01-06 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('listener', '0001_initial'), ('listener', '0002_auto_20210106_2306'), ('listener', '0003_auto_20210106_2307'), ('listener', '0004_auto_20210106_2309'), ('listener', '0005_auto_20210106_2317'), ('listener', '0006_auto_20210106_2324')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
                'permissions': (('view_all_listeners', 'Can view all webhook listeners'),),
            },
        ),
        migrations.CreateModel(
            name='ListenerLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('listener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listener.listener')),
            ],
            options={
                'ordering': ['-created_at'],
                'permissions': (('view_all_logs', 'Can view all webhook listener logs'),),
            },
        ),
    ]
