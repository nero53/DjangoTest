from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Hello')


def dataPage(request):
    students=[
        {'name': 'Nero', 'age' : 21},
        {'name': 'Hoshi', 'age' : 22},
        {'name': 'Ashe', 'age' : 20},
        {'name': 'Yuki', 'age' : 21}
        
    ]
    return render(request, 'displayData.html', context= {'students' : students})

def learningTemplates(request):
    return render(request, 'index.html')