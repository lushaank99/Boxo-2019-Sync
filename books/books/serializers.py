from rest_framework import serializers
from .models import Books

class BookLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('__all__')
