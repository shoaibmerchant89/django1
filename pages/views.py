from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from pages import views

def index(request):
    return render(request, 'pages/index.html', status=200)

def about(request):
    return render(request, 'pages/about.html')