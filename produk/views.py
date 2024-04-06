from django.shortcuts import render
from .models import Buku, Stationery


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


def filter(request, c: str):
    buku = Buku.objects.filter(kategori=c)
    stationery = Stationery.objects.filter(kategori=c)
    context = {
        'books': buku,
        'halaman': 'Produk',
        'stationery': stationery,
        'website': 'OnlineBookStore',
    }

    return render(request, 'produk/index.html', context)


def detail_buku(request, inputSlug):
    buku = Buku.objects.get(slug=inputSlug)
    context = {
        'books': buku,
        'halaman': 'Detail Buku',
        'website': 'OnlineBookStore'
    }
    return render(request, 'produk/detail.html', context)


def detail_stationery(request, inputSlug):
    stationery = Stationery.objects.get(slug=inputSlug)
    context = {
        'halaman': 'Detail Buku',
        'stationery': stationery,
        'website': 'OnlineBookStore'
    }
    return render(request, 'produk/detail.html', context)
