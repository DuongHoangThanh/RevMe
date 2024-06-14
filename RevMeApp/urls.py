from django.urls import path
from .views import PredictObesity, AssessmentsList, AssessmentsDetail, GeneratePlanAPIView

urlpatterns = [
    path('assessment/', AssessmentsList.as_view(), name='assessment-list'),
    path('assessment/<int:pk>/', AssessmentsDetail.as_view(), name='assessment-detail'),
    path('predict/', PredictObesity.as_view(), name='predict-obesity'),
    path('generate_plan/', GeneratePlanAPIView.as_view(), name='plan'),
]
