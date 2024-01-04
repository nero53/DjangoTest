from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Hello')


def sucessPage(request):
    return HttpResponse("This is the Sucess page")

def learningTemplates(request):
    return render(request, 'index.html')