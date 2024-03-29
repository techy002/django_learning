# Generated by Django 4.2.9 on 2024-01-10 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=150, null=True)),
                ("addres", models.TextField(blank=True, max_length=500, null=True)),
                ("mobile", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="BusinessProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("addres", models.TextField(blank=True, max_length=500, null=True)),
                ("mobile", models.IntegerField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.userprofile",
                    ),
                ),
            ],
        ),
    ]
