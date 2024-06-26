# Generated by Django 5.0.6 on 2024-06-11 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RevMeApp', '0005_goal_diastolic_goal_systolic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='age',
            new_name='duration_weeks',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='bmi_category',
            new_name='goal_type',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='physical_activity_level',
            new_name='target_weight_kg',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='daily_steps',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='diastolic',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='heart_rate',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='quality_of_sleep',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='sleep_disorder',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='sleep_duration',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='stress_level',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='systolic',
        ),
        migrations.AddField(
            model_name='goal',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50, null=True)),
                ('height', models.FloatField(blank=True, default=0.0, null=True)),
                ('weight', models.FloatField(blank=True, default=0.0, null=True)),
                ('CALC', models.CharField(blank=True, max_length=50, null=True)),
                ('FAVC', models.CharField(blank=True, max_length=50, null=True)),
                ('FCVC', models.IntegerField(blank=True, null=True)),
                ('NCP', models.IntegerField(blank=True, null=True)),
                ('SCC', models.CharField(blank=True, max_length=50, null=True)),
                ('SMOKE', models.CharField(blank=True, max_length=50, null=True)),
                ('CH2O', models.FloatField(blank=True, default=0.0, null=True)),
                ('family_history_w_overweight', models.CharField(blank=True, max_length=50, null=True)),
                ('FAF', models.IntegerField(blank=True, null=True)),
                ('TUE', models.FloatField(blank=True, null=True)),
                ('CAEC', models.CharField(blank=True, max_length=50, null=True)),
                ('MTRANS', models.CharField(blank=True, max_length=100, null=True)),
                ('NObeyesdad', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ass', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
