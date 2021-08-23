import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import quote_plus

# Create your views here.

# create home views

BASE_URL = 'https://kerala.craigslist.org/d/events-classes/search/eee?query={}'

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    frontend_stuff = {'search': search}
    return render(request, 'scrapingapp/new_search.html', frontend_stuff)
