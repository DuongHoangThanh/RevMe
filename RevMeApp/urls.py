from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.userApi, name='user-list'),
    path('api/register/', views.register, name='register'),
    path('api/login/', views.login, name='login'),
    path('api/user/<int:user_id>/', views.get_user, name='get-user'),
    path('api/user/update/<int:user_id>/', views.update_user, name='update-user'),
    path('api/user/delete/<int:user_id>/', views.delete_user, name='delete-user'),
    path('api/user/goal/', views.predict_bmi, name='predict-bmi'),
]