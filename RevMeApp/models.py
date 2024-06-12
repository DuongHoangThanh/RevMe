from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return f"{self.username}, {self.email}, {self.phone}"

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ass") # nó tự thêm _id vào sau user
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES,null=True, blank=True)
    height = models.FloatField(default=0.0,null=True, blank=True)
    weight = models.FloatField(default=0.0,null=True, blank=True)
    CALC = models.CharField(max_length=50,null=True, blank=True)
    FAVC = models.CharField(max_length=50,null=True, blank=True)
    FCVC = models.IntegerField(null=True, blank=True)
    NCP = models.IntegerField(null=True, blank=True)
    SCC = models.CharField(max_length=50,null=True, blank=True)
    SMOKE = models.CharField(max_length=50,null=True, blank=True)
    CH2O = models.FloatField(default=0.0,null=True, blank=True)
    family_history_with_overweight = models.CharField(max_length=50,null=True, blank=True)
    FAF = models.IntegerField(null=True, blank=True)
    TUE = models.FloatField(null=True, blank=True)
    CAEC = models.CharField(max_length=50,null=True, blank=True)
    MTRANS = models.CharField(max_length=100,null=True, blank=True)
    NObeyesdad = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return f"{self.gender}, {self.age}, {self.height}, {self.weight}, {self.NObeyesdad}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_goal") # nó tự thêm _id vào sau user
    goal_type = models.CharField(max_length=255,null=True, blank=True)
    target_weight_kg = models.FloatField(null=True, blank=True)
    duration_weeks = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal_type}, {self.target_weight_kg}, {self.duration_weeks}"
    
    
    





