from django.urls import path, include
from . import views


# TEMPLATE TAGGING
app_name = 'articles'

urlpatterns = [
    path('' , views.article_list, name='news'),
    path('create' , views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    ]
