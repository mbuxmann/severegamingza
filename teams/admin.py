from django.contrib import admin
from .models import Dota2Player, CounterStrikePlayer
# Register your models here.

class Dota2PlayerAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID', 'dotabuff']

    search_fields = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID', 'dotabuff']

    list_filter = ['name', 'surname', 'username']

    list_display = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID']

#   list_editable = ['match_result']

class CounterStrikePlayerAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID', 'counterstrikestats']

    search_fields = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID', 'counterstrikestats']

    list_filter = ['name', 'surname', 'username']

    list_display = ['name', 'surname', 'username', 'position', 'bio', 'picture', 'steamID']

admin.site.register(Dota2Player, Dota2PlayerAdmin)
admin.site.register(CounterStrikePlayer, CounterStrikePlayerAdmin)

