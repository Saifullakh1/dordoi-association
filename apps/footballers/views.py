from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Footballer
from .serializers import FootballSerializer, FootballerDetailSerializer


class FootballerListAPIView(ListAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballSerializer


class FootballDetailAPIView(RetrieveAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerDetailSerializer
    lookup_field = "slug"




