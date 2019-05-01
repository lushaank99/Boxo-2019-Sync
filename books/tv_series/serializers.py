from rest_framework import serializers
from .models import tv_series_list

class TVLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = tv_series_list
        fields = ('__all__')