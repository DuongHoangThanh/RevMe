from django.urls import path
from .views import PredictObesity, AssessmentsList, AssessmentsDetail, GeneratePlanAPIView, HomePageView, WorkoutPlanView, DetailWorkoutView, MealPlanView, DetailMealView

urlpatterns = [
    path('assessment/', AssessmentsList.as_view(), name='assessment-list'),
    path('assessment/<int:pk>/', AssessmentsDetail.as_view(), name='assessment-detail'),
    path('predict/', PredictObesity.as_view(), name='predict-obesity'),
    path('generate_plan/', GeneratePlanAPIView.as_view(), name='plan'),
    path('home/<int:goal_id>/', HomePageView.as_view(), name='home'),
    path('workout/<int:goal_id>&<str:day>/', WorkoutPlanView.as_view(), name='workout'),
    path('workout/<int:pk>/', DetailWorkoutView.as_view(), name='workout-detail'),
    path('meal/<int:goal_id>&<str:day>/', MealPlanView.as_view(), name='meal'),
    path('meal/<int:pk>/', DetailMealView.as_view(), name='meal-detail')
]
