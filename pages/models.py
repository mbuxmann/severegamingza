from django.db import models
import django_tables2

class Match(models.Model):
    class Meta:
        verbose_name_plural = "Matches"

    SEVERE_TEAMS = (
        ('DOTA 2', 'DOTA 2'),
    )

    LEAGUES = (
        ('VS Gaming', 'VS Gaming'),
    )

    DIVISIONS = (
        ('Premier', 'Premier'),
        ('First', 'First'),
        ('Second', 'Second'),
    )

    MATCH_RESULTS = (
        ('W', 'Won'),
        ('L', 'Lost'),
    )

    LEGS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
    )


    severe_team  = models.CharField(max_length=10, choices=SEVERE_TEAMS)
    opponent     = models.CharField(max_length=50)
    league       = models.CharField(max_length=20, choices=LEAGUES, null=True)
    division     = models.CharField(max_length=10, choices=DIVISIONS)
    score        = models.CharField(max_length=10)
    match_result = models.CharField(max_length=1,  choices=MATCH_RESULTS)
    leg          = models.CharField(max_length=1,  choices=LEGS)
    match_date   = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.severe_team} vs {self.opponent} at {self.match_date}'

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')
