from django.urls import path
from .views import MatchListAPIView


urlpatterns = [
    path('matches', MatchListAPIView.as_view(), name="match-list")
]