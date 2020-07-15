from django.urls import path, include
from . import views


# TEMPLATE TAGGING
app_name = 'contact'

urlpatterns = [
    path('' , views.contact, name='contact'),
    ]
