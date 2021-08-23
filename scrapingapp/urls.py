from django.urls import path
from . import views

app_name = 'scraping'
urlpatterns = [
    path('new_search/', views.new_search, name='new_search'),
    path('', views.home, name='home')

]

