from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from RevMeApp.models import User
from RevMeApp.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

# Create your views here.

@csrf_exempt
def userApi(request):
    if request.method == "GET":
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
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
            return JsonResponse({'token': token.key}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
