from django.urls import path
from .views import PredictObesity, plan_WD

urlpatterns = [
    path('predict/', PredictObesity.as_view(), name='predict-obesity'),
    path('plan/<int:user_id>/', plan_WD, name='plan-wd'),
]
