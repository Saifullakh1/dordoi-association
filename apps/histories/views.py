from rest_framework.generics import ListAPIView
from .models import History
from .serializers import HistorySerializer


class HistoryListAPIView(ListAPIView):
    queryset = History.objects.filter(is_active=True)
    serializer_class = HistorySerializer
