from rest_framework import serializers

from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    """list of films"""

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")

class MovieDetailSerializer(serializers.ModelSerializer):
    """Full films"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ("draft",)