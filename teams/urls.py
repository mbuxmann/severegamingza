from django.urls import path, include
from . import views


# TEMPLATE TAGGING
app_name = 'teams'

urlpatterns = [
    path('' , views.teams, name='teams'),
    path('dota/', views.dota, name='dota'),
    path('csgo/', views.csgo, name='csgo'),
    path('hearthstone/', views.hearthstone, name='hearthstone'),
    path('lol/', views.leagueoflegends, name='leagueoflegends'),
    path('rocketleague/', views.rocketleague, name='rocketleague'),
    ]
