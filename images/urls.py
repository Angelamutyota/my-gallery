from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.welcome,name = 'index'),
    url(r'^search/', views.search_image_results, name='search_image_results'),
    url(r'^image/(\d+)',views.image, name ='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)