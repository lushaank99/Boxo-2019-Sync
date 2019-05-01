"""torrenthub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path

from movies import views as movViews
from songs import views as songViews
from books import views as bookViews
from games import views as gameViews
from tv_series import views as tv_seriesViews
from comments import views as commViews


urlpatterns = [
    url('admin/', admin.site.urls),
    url('moviepage/',include('movies.urls')),
    url('tvseriespage/', include('tv_series.urls')),
    url('books/', include('books.urls')),
    url('games/', include('games.urls')),
    url('songs/', include('songs.urls')),
    url('printing/', include('print.urls')),
    url('movieapi10/', movViews.Movies10ListAPI),
    url('movieapi20/', movViews.Movies20ListAPI),
    url('songapi10/', songViews.Songs10ListAPI),
    url('songapi20/', songViews.Songs20ListAPI),
    #url('bookapi10/', bookViews)
    url('gameapi10/', gameViews.Games10ListAPI),
    url('gameapi20/', gameViews.Games20ListAPI),
    url('seriesapi5/', tv_seriesViews.TV5ListAPI),
    url('seriesapi20/', tv_seriesViews.TV10ListAPI),
    url('comments/', include('comments.urls')),
    url('movie/', movViews.MovieAPI),
    url('game/', gameViews.GameAPI),
    url('series/', tv_seriesViews.TVAPI),
    url('books/', bookViews.BookAPI),
    url('bookapi20/', bookViews.Books20ListAPI),
]
