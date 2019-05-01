from django.contrib import admin
from .models import Movie_list

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie','genre','released','imdb_rating','poster','runtime')
admin.site.register(Movie_list,MovieAdmin)
