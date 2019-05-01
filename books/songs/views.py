import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Songs_List
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongLogSerializer

list=[]
sup_list=[]
val = Songs_List.objects.all()
for j in range(len(val)):
    list = []
    x=val[j]
    x=str(x)
    y=x.split(' /// ')
    #print(y)
    for i in range(7):
        list.append(y[i])

    sup_list.append(list)
#list.append(val)
#print(sup_list)
def csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="songs.csv"'

    writer = csv.writer(response)
    writer.writerow(['song', 'type', 'artist/albums','released', 'imdb rating', 'poster .........................', 'runtime'])
    for k in range(len(sup_list)):
        writer.writerow(sup_list[k])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

@api_view()
def Songs10ListAPI(request):
    eqlogs = Songs_List.objects.raw("SELECT * FROM songs_Song_List ORDER BY rating DESC LIMIT 10")
    serializers = SongLogSerializer(eqlogs, many=True)
    return Response(serializers.data)

@api_view()
def Songs20ListAPI(request):
    eqlogs = Songs_List.objects.raw("SELECT * FROM songs_Song_List ORDER BY rating DESC LIMIT 20")
    serializers = SongLogSerializer(eqlogs, many=True)
    return Response(serializers.data)