from django.db import models
from django.contrib.auth.models import User
from precise_bbcode.fields import BBCodeTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    about = models.CharField(max_length = 20, default='General')
    hook = models.TextField(max_length = 300)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'


    def snippet(self):
        return self.hook + "..."
