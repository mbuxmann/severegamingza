from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Match

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def news(request):
    return render(request, 'pages/news.html')

def teams(request):
    return render(request, 'pages/teams.html')

def matches(request):
    matches = Match.objects.all().defer(
        "id", "league", "division", "leg", "match_date"
    )
    return render(request, 'pages/matches.html', {'matches' : matches})

def media(request):
    return render(request, 'pages/media.html')

def sponsors(request):
    return render(request, 'pages/sponsors.html')

def contact(request):
    return render(request, 'pages/contact.html')
