import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import quote_plus
from . import models

# Create your views here.

# create home views

BASE_URL = 'https://kerala.craigslist.org/d/events-classes/search/hhh?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_600x450.jpg'
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listing = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listing:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='gallery').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url))


    frontend_stuff = {
        'search': search,
        'final_postings': final_postings
    }
    return render(request, 'scrapingapp/new_search.html', frontend_stuff)
