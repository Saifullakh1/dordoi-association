from rest_framework.generics import ListAPIView
from .models import History, Image
from .serializers import HistorySerializer, ImageSerializer


class HistoryListAPIView(ListAPIView):
    queryset = History.objects.filter(is_active=True)
    serializer_class = HistorySerializer


class ImageBannerListAPIView(ListAPIView):
    queryset = Image.objects.filter(type='banner')[:3]
    serializer_class = ImageSerializer
