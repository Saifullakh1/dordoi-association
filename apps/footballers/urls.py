from django.urls import path
from .views import FootballerListAPIView, FootballDetailAPIView


urlpatterns = [
    path('footballers', FootballerListAPIView.as_view(), name='footballer-list'),
    path('footballer/<str:slug>', FootballDetailAPIView.as_view(), name='footballer-detail')
]