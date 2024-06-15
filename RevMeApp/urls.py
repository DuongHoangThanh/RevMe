from django.urls import path
from .views import PredictObesity, AssessmentsList, AssessmentsDetail, GeneratePlanAPIView, HomePageView, WorkoutPlanView, DetailWorkoutView

urlpatterns = [
    path('assessment/', AssessmentsList.as_view(), name='assessment-list'),
    path('assessment/<int:pk>/', AssessmentsDetail.as_view(), name='assessment-detail'),
    path('predict/', PredictObesity.as_view(), name='predict-obesity'),
    path('generate_plan/', GeneratePlanAPIView.as_view(), name='plan'),
    path('home/', HomePageView.as_view(), name='home'),
    path('workout/', WorkoutPlanView.as_view(), name='workout'),
    path('workout/<int:pk>/', DetailWorkoutView.as_view(), name='workout-detail')
]
