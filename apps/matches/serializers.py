from rest_framework import serializers
from .models import Club, Match


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ("id", "title", "description", "image")


class MatchSerializer(serializers.ModelSerializer):
    first_club = serializers.SerializerMethodField()
    second_club = serializers.SerializerMethodField()
    first_club_logo = serializers.SerializerMethodField()
    second_club_logo = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ("id", "first_club", "first_club_logo",
                  "second_club", "second_club_logo", "result",
                  "date_at", "time_at", "description", "location",
                  "championship"
                  )

    def get_first_club(self, obj):
        return obj.first_club.title

    def get_second_club(self, obj):
        return obj.second_club.title

    def get_first_club_logo(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.first_club.image.url)

    def get_second_club_logo(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.second_club.image.url)