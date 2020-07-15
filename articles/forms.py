from django import forms
from . models import Article

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'hook', 'about', 'body', 'slug', 'thumb']
    
    