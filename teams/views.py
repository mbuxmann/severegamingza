from django.shortcuts import render
from .models import Dota2Player, CounterStrikePlayer
from achievements.models import DotaAchievement

# Create your views here.

def teams(request):
    return render(request, 'teams/teams.html')

def dota(request):
    Dota2Players = Dota2Player.objects.all()
    DotaAchievements = DotaAchievement.objects.all().order_by('-year', '-leg')
    return render(request, 'teams/dota.html', {'Dota2Players':Dota2Players, 'DotaAchievements':DotaAchievements})

def csgo(request):
    CounterStrikePlayers = CounterStrikePlayer.objects.all()
    return render(request, 'teams/csgo.html', {'CounterStrikePlayers':CounterStrikePlayers})

def hearthstone(request):
    return render(request, 'teams/hearthstone.html')

def leagueoflegends(request):
    return render(request, 'teams/leagueoflegends.html')

def rocketleague(request):
    return render(request, 'teams/rocketleague.html') 