from django.shortcuts import render
from produk.models import Buku as data_buku


def index(request):
    buku = data_buku.objects.all()
    context = {
        'books':buku,
        'halaman':'Beranda',
        'website':'Perpustakaan'
    }
    return render(request, 'index.html', context)