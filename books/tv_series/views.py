import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import tv_series_list
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TVLogSerializer

# Create your views here.

list=[]
sup_list=[]
val = tv_series_list.objects.all()
for j in range(len(val)):
    list = []
    x=val[j]
    x=str(x)
    y=x.split(' /// ')
    #print(y)
    for i in range(8):
        list.append(y[i])

    sup_list.append(list)
#list.append(val)
#print(sup_list)
def csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tv_series.csv"'

    writer = csv.writer(response)
    writer.writerow(['tv_series', 'genre','year', 'released date', 'imdb rating', 'poster .........................', 'seasons','trailer.....'])
    for k in range(len(sup_list)):
        writer.writerow(sup_list[k])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def home(request):
    if request.method == 'POST':
        s = request.POST['search_name']
        search=str(s)
        #x='guardians of the galaxy vol. 2'
        search.replace(" ", "%20")

        response = requests.get('http://www.omdbapi.com/?t={}&apikey=769fee09'.format(search))
        geodata = response.json()
        tv_series = geodata['Title']
        genre = geodata['Genre']
        year = geodata['Year']
        released = geodata['Released']
        imdb_rating = geodata['imdbRating']
        poster = geodata['Poster']
        seasons = geodata['totalSeasons']


        if tv_series_list.objects.filter(tv_series = s):
            print(s)
        else:
            tv_series_list.objects.create(tv_series=tv_series,genre=genre,year=year,released=released,imdb_rating=imdb_rating,poster=poster,seasons=seasons)

        return render(request,'tv_series/home.html', {
            'ip': geodata['Title'],
            'year':geodata['Year'],
            'genre' : geodata['Genre'],
            'released' : geodata['Released'],
            'imdbrating' : geodata['imdbRating'],
            'seasons': geodata['totalSeasons']

        })
    return render(request, 'tv_series/home.html')

@api_view()
def TVAPI(request):
    name=request.GET.get('name',"")
    print(name)
    #query = "SELECT * FROM games_Games_list WHERE movie = '%s'" % name
    #print(query)
    eqlogs = tv_series_list.objects.filter(tv_series=name).values()
    print(eqlogs[0])
    #serializers = MovieLogSerializer(eqlogs, many=False)
    #print(serializers.data)
    return Response(eqlogs[0])

@api_view()
def TV5ListAPI(request):
    eqlogs = tv_series_list.objects.raw("SELECT * FROM tv_series_tv_series_list ORDER BY imdb_rating DESC LIMIT 5")
    serializers = TVLogSerializer(eqlogs, many=True)
    return Response(serializers.data)

@api_view()
def TV10ListAPI(request):
    eqlogs = tv_series_list.objects.raw("SELECT * FROM tv_series_tv_series_list ORDER BY imdb_rating DESC LIMIT 10")
    serializers = TVLogSerializer(eqlogs, many=True)
    return Response(serializers.data)