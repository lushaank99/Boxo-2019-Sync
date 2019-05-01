from django.shortcuts import render
from movies.serializers import MovieLogSerializer
from games.serializers import GameLogSerializer
from songs.serializers import SongLogSerializer
from tv_series.serializers import TVLogSerializer

from movies.models import Movie_list

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        type = request.POST['type']
        print(name, type)


    return render(request, "print/index.html")


@api_view()
def MovieAPI(name):
    query = "SELECT * FROM movies_Movie_list AS movie WHERE movie.name = %s" % name
    eqlogs = Movie_list.objects.raw(query)
    serializers = MovieLogSerializer(eqlogs, many=False)
    return Response(serializers.data)