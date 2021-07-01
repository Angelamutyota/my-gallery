from django.shortcuts import render
from django.http  import HttpResponse
from .models import Location, Category, Image

# Create your views here.
def welcome(request):
    images = Image.all_images()
    return render(request, 'index.html', {'images': images})
