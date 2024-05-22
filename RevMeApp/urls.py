from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userApi),
    path('register/', views.register),
    path('login/', views.login),
]