# Generated by Django 4.1.3 on 2023-01-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_location_events_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.CharField(default=None, max_length=1000, blank=True, null=True),
        ),
    ]
