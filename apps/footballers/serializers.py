from rest_framework import serializers
from .models import Footballer


class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = (
            "id", "full_name", "image", "position",
            "slug"
            )


class FootballerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = (
            "id", "full_name", "image", "birthday", "number",
            "height", "weight", "citizenship", "position"
            )