# Generated by Django 4.2.16 on 2024-10-08 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0002_case_court_jurisdiction_case_date_of_occurrence_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='location_Area',
            new_name='location_area',
        ),
        migrations.RemoveField(
            model_name='case',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='case',
            name='assigned_official',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_official_cases', to=settings.AUTH_USER_MODEL),
        ),
    ]