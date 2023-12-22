from django.shortcuts import render
from .models import Catalog


def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, 'catalog_list.html', {'catalogs': catalogs})

