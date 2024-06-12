from django.urls import path
from .views import PredictObesity, plan_WD, AssessmentsList, AssessmentsDetail

urlpatterns = [
    path('assessment/', AssessmentsList.as_view(), name='assessment-list'),
    path('assessment/<int:pk>/', AssessmentsDetail.as_view(), name='assessment-detail'),
    path('predict/', PredictObesity.as_view(), name='predict-obesity'),
    path('plan/<int:user_id>/', plan_WD, name='plan-wd'),
]
