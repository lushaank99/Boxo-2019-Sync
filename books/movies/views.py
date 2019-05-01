import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie_list
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieLogSerializer


#69dfb02d97db8238985dd9d57f656946

list=[]
sup_list=[]
val = Movie_list.objects.all()
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
    response['Content-Disposition'] = 'attachment; filename="movies.csv"'

    writer = csv.writer(response)
    writer.writerow(['movie', 'genre', 'released date', 'imdb rating', 'poster .........................', 'runtime','youtube link . ...'])
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
        movie = geodata['Title']
        genre = geodata['Genre']
        released = geodata['Released']
        imdb_rating = geodata['imdbRating']
        poster = geodata['Poster']
        runtime = geodata['Runtime']
        if Movie_list.objects.filter(movie = s):
            print(s)
        else:
            Movie_list.objects.create(movie=movie,genre=genre,released=released,imdb_rating=imdb_rating,poster=poster,runtime=runtime)

        return render(request,'movies/home.html', {
            'ip': geodata['Title'],
            'year':geodata['Year'],
            'genre' : geodata['Genre'],
            'released' : geodata['Released'],
            'imdbrating' : geodata['imdbRating'],
            'runtime': geodata['Runtime']

        })
    return render(request, 'movies/home.html')

@api_view()
def MovieAPI(request):
    name=request.GET.get('name',"")
    print(name)
    query = "SELECT * FROM movies_Movie_list WHERE movie = '%s'" % name
    print(query)
    eqlogs = Movie_list.objects.filter(movie=name).values()
    print(eqlogs[0])
    #serializers = MovieLogSerializer(eqlogs, many=False)
    #print(serializers.data)
    return Response(eqlogs[0])

@api_view()
def Movies10ListAPI(request):
    eqlogs = Movie_list.objects.raw("SELECT * FROM movies_Movie_list ORDER BY imdb_rating DESC LIMIT 10")
    serializers = MovieLogSerializer(eqlogs, many=True)
    return Response(serializers.data)

@api_view()
def Movies20ListAPI(request):
    eqlogs = Movie_list.objects.raw("SELECT * FROM movies_Movie_list ORDER BY imdb_rating DESC LIMIT 20")
    serializers = MovieLogSerializer(eqlogs, many=True)
    return Response(serializers.data)
