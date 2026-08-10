from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context = {'name' : 'Kaveh Aliani', 'age': '23 Years', 'email': 'Kaveh.aj17@gmail.com', 'city': 'Tehran', 'country': 'Iran',
               'number': '09909083082'}
    return render(request, 'website\index.html', context)

