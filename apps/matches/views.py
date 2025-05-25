from rest_framework.generics import ListAPIView
from .models import Match
from .serializers import MatchSerializer


class MatchListAPIView(ListAPIView):
    queryset = Match.objects.filter(is_active=True)
    serializer_class = MatchSerializer