# Generated by Django 2.1.5 on 2019-01-27 00:11

from django.db import migrations, models
import django.db.models.deletion
import simplemde.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "description",
                    simplemde.fields.SimpleMDEField(
                        blank=True, max_length=2000, null=True
                    ),
                ),
                ("invitee_capacity", models.PositiveIntegerField(default=0)),
                ("event_day", models.DateField()),
                ("initial_hour", models.TimeField()),
                ("end_hour", models.TimeField()),
                ("place_name", models.CharField(max_length=200)),
                ("open_street_map_url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Invitee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("enrolled_at", models.DateTimeField(auto_now_add=True)),
                ("cancelled", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.Event"
                    ),
                ),
            ],
        ),
    ]