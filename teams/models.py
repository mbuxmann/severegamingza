from django.db import models

# Create your models here.
class Dota2Player(models.Model):
    class Meta:
        verbose_name_plural = "Dota 2"

    name = models.CharField(max_length = 100, default='Name')
    surname = models.CharField(max_length = 100, default='Surname')
    username = models.CharField(max_length = 100, default='In Game Name')
    position = models.CharField(max_length = 20, default='Position')
    bio = models.TextField(max_length = 300)
    picture = models.ImageField(max_length = 100, default='PPdefault.jpg', blank=True)
    steamID = models.CharField(max_length = 300, default='Steam ID')
    dotabuff = models.CharField(max_length = 400,default='DOTABUFF')
    
    def __str__(self):
        return f'{self.name}'


class CounterStrikePlayer(models.Model):
    class Meta:
        verbose_name_plural = "Counter-Strike: Global Offensive"


    name = models.CharField(max_length = 100, default='Name')
    surname = models.CharField(max_length = 100, default='Surname')
    username = models.CharField(max_length = 100, default='In Game Name')
    position = models.CharField(max_length = 20, default='Position')
    bio = models.TextField(max_length = 300)
    picture = models.ImageField(max_length = 100, default='PPdefault.jpg', blank=True)
    steamID = models.CharField(max_length = 300, default='Steam ID')
    counterstrikestats = models.CharField(max_length = 400, default='CSGO STATS')


    def __str__(self):
        return f'{self.name}'
