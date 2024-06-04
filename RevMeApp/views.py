from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from RevMeApp.models import User
from RevMeApp.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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


# assessment
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import AssessmentSerializer

@api_view(['POST'])
def create_assessment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AssessmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)