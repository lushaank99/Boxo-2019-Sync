from rest_framework import serializers
from .models import comments_list

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments_list
        fields = ('__all__')