from rest_framework import serializers
from .models import Image, History


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image")


class HistorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = ("id", "title", "description", "images")
