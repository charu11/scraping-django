from django.urls import path
from . import views

app_name = 'scraping'
urlpatterns = [
    path('', views.home, name='home')
]

