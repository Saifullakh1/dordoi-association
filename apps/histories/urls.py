from django.urls import path
from .views import HistoryListAPIView


urlpatterns = [
    path('histories', HistoryListAPIView.as_view(), name='histories-list')
]