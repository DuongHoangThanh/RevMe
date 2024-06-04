from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # GENDER_CHOICES = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other'),
    # ]

    # age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    # height = models.FloatField()
    # weight = models.FloatField()
    # intensity_level = models.IntegerField()
    # sleep_quality = models.IntegerField()
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # avatar = models.CharField
    def __str__(self):
        return f"{self.get_gender_display()} - Age: {self.age}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_goal") # nó tự thêm _id vào sau user
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True, blank=True)
    occupation = models.CharField(max_length=255,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    daily_steps = models.IntegerField(null=True, blank=True)
    sleep_duration = models.FloatField(null=True, blank=True)
    quality_of_sleep = models.FloatField(default=0.0,null=True, blank=True)
    physical_activity_level = models.FloatField(null=True, blank=True)
    stress_level = models.FloatField(default=0.0,null=True, blank=True)
    bmi_category = models.CharField(max_length=255, blank=True, null=True)  # Initially blank until predicted
    SLEEP_DISORDER_CHOICES = (
        ('None', 'None'),
        ('Insomnia', 'Insomnia'),
        ('Sleep Apnea', 'Sleep Apnea'),
    )
    sleep_disorder = models.CharField(max_length=255, choices=SLEEP_DISORDER_CHOICES, blank=True, null=True)  # Allow blank value
    heart_rate = models.IntegerField(blank=True, null=True)
    systolic = models.IntegerField(blank=True, null=True)
    diastolic = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.occupation}"




