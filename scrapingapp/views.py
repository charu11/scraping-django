from django.shortcuts import render

# Create your views here.

# create home views


def home(request):
    return render(request, 'base.html')
