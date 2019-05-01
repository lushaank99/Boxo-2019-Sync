import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import comments_list
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer

def home(request):
    return render(request, 'comments/home.html')

@api_view()
def CommListAPI(request):
    type = request.GET['type']
    name = request.GET['name']
    eqlogs = comments_list.objects.filter(type=type, name=name).values()
    print(eqlogs)
    serializers = CommentSerializer(eqlogs, many=True)
    return Response(serializers.data)
