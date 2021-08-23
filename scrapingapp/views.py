from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

# create home views


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    frontend_stuff = {'search': search}
    return render(request, 'scrapingapp/new_search.html', frontend_stuff)
