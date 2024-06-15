from rest_framework import serializers
from RevMeApp.models import User, Goal, Assessment, Plan, WorkoutPlan, MealPlan, Exercise, Meal, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}, 
            'phone': {'required': False},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

        
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
                
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
        
class ProgressSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = Progress
        fields = '__all__'
        
class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
        
class MealPlanSerializer(serializers.ModelSerializer):
    meal = MealSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = MealPlan
        fields = '__all__'