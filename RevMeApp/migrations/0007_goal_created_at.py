# Generated by Django 5.0.6 on 2024-06-11 16:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevMeApp', '0006_rename_age_goal_duration_weeks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
