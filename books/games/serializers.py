from rest_framework import serializers
from .models import Games_List

class GameLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games_List
        fields = ('__all__')