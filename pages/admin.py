from django.contrib import admin
from pages.models import Match, Person

# Register your models here.

class MatchAdmin(admin.ModelAdmin):
    fields = ['severe_team', 'opponent', 'league', 'division', 'score', 'match_result', 'leg', 'match_date']

    search_fields = ['severe_team', 'opponent', 'league', 'division', 'score', 'match_result', 'leg', 'match_date']

    list_filter = ['severe_team', 'opponent', 'league', 'division', 'match_result', 'leg', 'match_date']

    list_display = ['severe_team', 'opponent', 'league', 'division', 'score', 'match_result', 'leg', 'match_date']



admin.site.register(Match, MatchAdmin)
admin.site.register(Person)
