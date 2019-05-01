import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Games_List
# Create your views here.
#ad97dd8cecd4480bb8332b5cff0d2c4b

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GameLogSerializer

list=[]
sup_list=[]
val = Games_List.objects.all()
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
    response['Content-Disposition'] = 'attachment; filename="games.csv"'

    writer = csv.writer(response)
    writer.writerow(['game', 'genre', 'released date', 'imdb rating', 'poster .........................', 'developer','youtube link . ...'])
    for k in range(len(sup_list)):
        writer.writerow(sup_list[k])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

@api_view()
def GameAPI(request):
    name=request.GET.get('name',"")
    print(name)
    query = "SELECT * FROM games_Games_list WHERE movie = '%s'" % name
    print(query)
    eqlogs = Games_List.objects.filter(game=name).values()
    print(eqlogs[0])
    #serializers = MovieLogSerializer(eqlogs, many=False)
    #print(serializers.data)
    return Response(eqlogs[0])

@api_view()
def Games10ListAPI(request):
    eqlogs = Games_List.objects.raw("SELECT * FROM games_Games_List ORDER BY rating DESC LIMIT 10")
    serializers = GameLogSerializer(eqlogs, many=True)
    return Response(serializers.data)

@api_view()
def Games20ListAPI(request):
    eqlogs = Games_List.objects.raw("SELECT * FROM games_Games_List ORDER BY rating DESC LIMIT 20")
    serializers = GameLogSerializer(eqlogs, many=True)
    return Response(serializers.data)