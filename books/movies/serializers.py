from rest_framework import serializers
from .models import Movie_list

class MovieLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_list
        fields = ('__all__')

