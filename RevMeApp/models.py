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

    def __str__(self):
        return f"{self.get_gender_display()} - Age: {self.age}"
    
    

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_goal")
    target_weight = models.FloatField()
    target_body_fat_percentage = models.FloatField()
    target_muscle_mass = models.FloatField()
    target_duration_day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    

