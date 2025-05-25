from django.urls import path
from .views import HistoryListAPIView, ImageBannerListAPIView


urlpatterns = [
    path('histories', HistoryListAPIView.as_view(), name='histories-list'),
    path('banners', ImageBannerListAPIView.as_view(), name='banners-list')
]