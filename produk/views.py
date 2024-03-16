from django.shortcuts import render
from .models import Buku, Stationery

# Create your views here.
def index(request):
    buku = Buku.objects.all()
    stationery = Stationery.objects.all()
    context = {
        'books': buku,
        'halaman': 'Produk',
        'stationery': stationery,
        'website': 'OnlineBookStore',
    }

    return render(request, 'produk/index.html', context)

def detail(request, inputSlug):
    buku = Buku.objects.get(slug=inputSlug)
    context = {
        'books': buku,
        'halaman': 'Detail Buku',
        'website': 'OnlineBookStore'
    }
    return render(request, 'produk/detail.html', context)
