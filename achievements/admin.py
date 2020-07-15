from django.contrib import admin
from achievements.models import DotaAchievement

# Register your models here.
class AchievementAdmin(admin.ModelAdmin):
    fields = ['year', 'league', 'division', 'leg', 'placed']
    search_fields = ['year', 'league', 'division', 'leg', 'placed']
    list_filter = ['year', 'league', 'division', 'leg', 'placed']
    list_display = ['year', 'league', 'division', 'leg', 'placed']
    

admin.site.register(DotaAchievement, AchievementAdmin)
