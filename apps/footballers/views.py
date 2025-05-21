from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import Footballer, Banner, Stories
from .serializers import FootballSerializer, FootballerDetailSerializer, BannerSerializer, StoriesSerializer


class FootballerListAPIView(ListAPIView):
    queryset = Footballer.objects.filter(is_active=True)
    serializer_class = FootballSerializer


class FootballDetailAPIView(RetrieveAPIView):
    queryset = Footballer.objects.filter(is_active=True)
    serializer_class = FootballerDetailSerializer
    lookup_field = "slug"


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class StoriesAPIView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer



