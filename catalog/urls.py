from django.conf.urls.static import static
from django.urls import path
from mysite import settings
from .views import catalog_list

urlpatterns = [
    path('catalog/', catalog_list, name='catalog_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)