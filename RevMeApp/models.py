from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    height = models.FloatField()
    weight = models.FloatField()
    intensity_level = models.IntegerField()
    sleep_quality = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # avatar = models.CharField
    def __str__(self):
        return f"{self.get_gender_display()} - Age: {self.age}"
    
    

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_goal")
    target_weight = models.FloatField()
    target_body_fat_percentage = models.FloatField()
    target_muscle_mass = models.FloatField()
    target_duration_day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class Assessment(models.Model):
    user_id = models.IntegerField()
    target = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    weight = models.IntegerField()
    age = models.IntegerField()
    experienced = models.BooleanField()
    level = models.IntegerField()
    limitations = models.CharField(max_length=255, blank=True, null=True)
    diet_preference = models.CharField(max_length=255, blank=True, null=True)
    day_commit = models.IntegerField()
    exercise_preference = models.JSONField(blank=True, null=True)
    any_supplement = models.BooleanField()
    specify_supplement = models.JSONField(blank=True, null=True)
    calo_per_day = models.IntegerField()
    quality_sleep = models.CharField(max_length=255, blank=True, null=True)


