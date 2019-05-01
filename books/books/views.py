import csv
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookLogSerializer


from .models import Books
# Create your views here.

list=[]
sup_list=[]
val = Books.objects.all()
for j in range(len(val)):
    list = []
    x=val[j]
    x=str(x)
    y=x.split(' /// ')
    #print(y)
    for i in range(5):
        list.append(y[i])

    sup_list.append(list)
#list.append(val)
#print(sup_list)
def csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['book', 'genre', 'published', 'poster .........................','author'])
    for k in range(len(sup_list)):
        writer.writerow(sup_list[k])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

@api_view()
def BookAPI(request):
    name=request.GET.get('name',"")
    print(name)
    query = "SELECT * FROM books_Books WHERE book = '%s'" % name
    print(query)
    eqlogs = Books.objects.filter(book=name).values()
    print(eqlogs[0])
    #serializers = MovieLogSerializer(eqlogs, many=False)
    #print(serializers.data)
    return Response(eqlogs[0])

@api_view()
def Books10ListAPI(request):
    eqlogs = Books.objects.raw("SELECT * FROM books_Books ORDER BY book DESC LIMIT 10")
    serializers = BookLogSerializer(eqlogs, many=True)
    return Response(serializers.data)

@api_view()
def Books20ListAPI(request):
    eqlogs = Books.objects.raw("SELECT * FROM books_Books ORDER BY book DESC LIMIT 20")
    serializers = BookLogSerializer(eqlogs, many=True)
    return Response(serializers.data)