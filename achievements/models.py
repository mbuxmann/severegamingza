from django.db import models

# Create your models here.
class DotaAchievement(models.Model):
    class Meta:
        verbose_name_plural = "Dota Achievements"

    LEAGUES = (
        ('VS Gaming', 'VS Gaming'),
    )

    DIVISIONS = (
        ('Premier', 'Premier'),
        ('First', 'First'),
        ('Second', 'Second'),
        ('Ladder', 'Ladder'),
    )

    LEGS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
    )

    year        = models.CharField(max_length=10)
    league      = models.CharField(max_length=20, choices=LEAGUES, null=True)
    division    = models.CharField(max_length=10, choices=DIVISIONS)
    leg         = models.CharField(max_length=1,  choices=LEGS)
    placed      = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.year} | {self.league} | {self.division} | {self.leg} | {self.placed}'