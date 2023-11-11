# Generated by Django 4.2.7 on 2023-11-11 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("email", models.EmailField(blank=True, max_length=500, null=True)),
                (
                    "short_intro",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="profiles/user-default.png",
                        null=True,
                        upload_to="profiles/",
                    ),
                ),
                (
                    "social_github",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("social_x", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "social_linkedin",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "social_website",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
