from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from RevMeApp.models import User,Goal   
from RevMeApp.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Handle POST requests without CSRF token
from .models import Goal
import pickle
import joblib
# Create your views here.

@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def userApi(request):
    if request.method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def register(request):
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=201)
        return JsonResponse(user_serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"message": "success",'token': token.key}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405) 
@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data, safe=False)


@csrf_exempt
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    data = JSONParser().parse(request)
    user_serializer = UserSerializer(user, data=data, partial=True)  # partial=True để cho phép cập nhật từng phần
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=200)
    return JsonResponse(user_serializer.errors, status=400)

@csrf_exempt
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    user.is_active = False
    user.save()
    return JsonResponse({'message': 'User deactivated'}, status=200)



@csrf_exempt
def predict_bmi(request):
    if request.method == 'POST':
        # Extract data from the request body (assuming JSON format)
        data = JSONParser().parse(request)
        # Create a Goal object from the received data
        goal = Goal(
            user_id=data['user_id'],
            gender=data['gender'],
            age=data['age'],
            occupation=data['occupation'],
            sleep_duration=data['sleep_duration'],
            quality_of_sleep=data['quality_of_sleep'],
            physical_activity_level=data['physical_activity_level'],
            stress_level=data['stress_level'],
            heart_rate=data['heart_rate'],
            daily_steps=data['daily_steps'],
            sleep_disorder=data['sleep_disorder'],
            systolic=data['systolic'],
            diastolic=data['diastolic'],
        )

        model = pickle.load(open("/Users/thanhduonghoang/Desktop/RevMe/RevMeApp/DTC.pkl", "rb"))

        if goal.gender == "Male" :
            goal.gender = 1
        elif goal.gender == "Female": 
            goal.gender = 0
            
        if goal.occupation == "Accountant" :
            goal.occupation = 0
        elif goal.occupation == "Doctor": 
            goal.occupation = 1
        elif goal.occupation == "Engineer":
            goal.occupation = 2
        elif goal.occupation == "Lawyer":
            goal.occupation = 3
        elif goal.occupation == "Manager":
            goal.occupation = 4
        elif goal.occupation == "Nurse":
            goal.occupation = 5
        elif goal.occupation == "Sales Representative":
            goal.occupation = 6
        elif goal.occupation == "Salesperson":
            goal.occupation = 7
        elif goal.occupation == "Scientist":
            goal.occupation = 8
        elif goal.occupation == "Software Engineer":
            goal.occupation = 9
        elif goal.occupation == "Teacher":
            goal.occupation = 10
        else:
            goal.occupation = 10
        
        
        if goal.sleep_disorder == "Insomnia" :
            goal.sleep_disorder = 0
        elif goal.sleep_disorder == "NoInfo": 
            goal.sleep_disorder = 1
        elif goal.sleep_disorder == "Sleep Apnea":
            goal.sleep_disorder = 2
            
        # Extract features from the Goal object
        features = [goal.gender, goal.age, goal.occupation, goal.sleep_duration, goal.quality_of_sleep, goal.physical_activity_level, goal.stress_level, goal.heart_rate, goal.daily_steps, goal.sleep_disorder, goal.systolic, goal.diastolic]

        # Use the model to predict BMI
        predicted_bmi = model.predict([features])[0]

        # Save the prediction to the database (if needed)
        goal.bmi_category = predicted_bmi
        
        if goal.bmi_category == 0 :
            goal.bmi_category = "Normal"
        elif goal.bmi_category == 1 : 
            goal.bmi_category = "Normal Weight"
        elif goal.bmi_category == 2 :
            goal.bmi_category = "Obese"
        elif goal.bmi_category == 3 :
            goal.bmi_category = "Overweight"
            
        goal.save()

        # Return the prediction to the Android app
        return JsonResponse({'predicted_bmi': goal.bmi_category}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)