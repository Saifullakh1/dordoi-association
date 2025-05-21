from rest_framework import serializers
from .models import Footballer, Banner, Stories


class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = (
            "id", "full_name", "image", "position","number", "citizenship",
            "slug"
            )


class FootballerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = (
            "id", "full_name", "image", "birthday", "number",
            "height", "weight", "citizenship", "position"
            )
        
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            "id", "image", "title"
            )


# serializers.py

class StoriesSerializer(serializers.ModelSerializer):
    isNew = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Stories
        fields = ['id', 'title', 'subtitle', 'description', 'image', 
                  'thumbnail', 'video', 'isNew', 'date']