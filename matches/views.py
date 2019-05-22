from django.shortcuts import render
from . models import Match
# Create your views here.

def matches(request):
    matches = Match.objects.all().order_by('-match_date')
    return render(request, 'matches/matches.html', {'matches':matches})