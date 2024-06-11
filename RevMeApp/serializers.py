from rest_framework import serializers
from RevMeApp.models import User, Goal, Assessment

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
            # age=validated_data['age'],
            phone=validated_data['phone'],
            # height=validated_data['height'],
            # weight=validated_data['weight'],
            # intensity_level=validated_data['intensity_level'],
            # sleep_quality=validated_data['sleep_quality'],
            # gender=validated_data['gender']
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

