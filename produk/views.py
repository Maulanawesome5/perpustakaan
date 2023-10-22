from django.shortcuts import render
from .models import Buku, Penulis_Buku

# Create your views here.
def index(request):
    buku = Buku.objects.all()
    context = {
        'books': buku,
        'halaman': 'Produk',
        'website': 'Perpustakaan'
    }
    return render(request, 'produk/index.html', context)

def detail(request, inputSlug):
    buku = Buku.objects.get(slug=inputSlug)
    context = {
        'books': buku,
        'halaman': 'Detail Buku',
        'website': 'Perpustakaan'
    }
    return render(request, 'produk/detail.html', context)

# def profilPenulis(request, id):
#     penulis = Penulis_Buku.objects.get(penulis_id=id)
#     context = {
#         'halaman': 'Profil Penulis',
#         'profiles': penulis,
#         'website': 'Perpustakaan'
#     }
#     return render(request, 'produk/penulis.html', context)
