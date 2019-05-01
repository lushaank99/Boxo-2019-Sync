from rest_framework import serializers
from .models import Songs_List

class SongLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs_List
        fields = ('__all__')