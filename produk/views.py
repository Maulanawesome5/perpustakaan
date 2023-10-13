from django.shortcuts import render
from .models import Buku

# Create your views here.
def index(request):
    buku = Buku.objects.all()
    context = {
        'books': buku,
        'halaman': 'Produk',
        'website': 'Perpustakaan'
    }
    return render(request, 'produk/index.html', context)