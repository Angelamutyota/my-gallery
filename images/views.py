from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    images = Image.all_images()
    return render(request, 'index.html', {'images': images})

def search_image_results(request):
     
     if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"image": searched_image})

     else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
   try:
      image = Image.objects.get(id = image_id)
   except ObjectDoesNotExist:
      raise Http404()
   return render(request,"image.html", {"image":image})

