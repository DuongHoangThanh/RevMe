# Generated by Django 5.0.6 on 2024-06-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RevMeApp', '0003_delete_assessment_remove_goal_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='blood_pressure',
        ),
    ]
