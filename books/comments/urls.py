from . import views
from django.conf.urls import include,url
from django.urls import path

app_name = 'comments'

urlpatterns = [
    url('search/', views.CommListAPI, name='search'),
    url('', views.home, name='home'),
    #path('<str:type>/<str:name>', views.search, name='search'),
    #url('(?P<Name>(\d+))/$', views.search, name='search'),
    #path('<str:Type>/<str:Name>', views.search, name='search')

]