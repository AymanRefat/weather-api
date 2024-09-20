from django.urls import path
from .views import WeatherAPIView

urlpatterns = [
    path('<str:city>/', WeatherAPIView.as_view(), name='weather'),
]
