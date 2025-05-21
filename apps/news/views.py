from rest_framework.generics import ListAPIView
from .models import News
from .serializers import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsSerializer
