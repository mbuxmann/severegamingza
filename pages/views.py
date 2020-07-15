
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def media(request):
    return render(request, 'pages/media.html')

def sponsors(request):
    return render(request, 'pages/sponsors.html')

def login_portal(request):
    return redirect('accounts:login')

def register_portal(request):
    return redirect('accounts:signup')

def view_400(request, exception):
    return render (request, 'pages/400.html')

def view_403(request, exception):
    return render (request, 'pages/403.html')

def view_404(request, exception):
    return render (request, 'pages/404.html')

def view_500(request):
    return render (request, 'pages/500.html')
