from django.urls import path
from .views import FootballerListAPIView, FootballDetailAPIView, BannerListAPIView, StoriesAPIView


urlpatterns = [
    path('footballers', FootballerListAPIView.as_view(), name='footballer-list'),
    path('footballer/<str:slug>', FootballDetailAPIView.as_view(), name='footballer-detail'),
    path('banners', BannerListAPIView.as_view(), name='banner-list'),
    path('stories', StoriesAPIView.as_view(), name='stories-list'),
]