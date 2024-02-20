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
    if request.method == "GET":
        print("\n")
        print(f"""Debugging Mode
        \rJudul Buku   = {context['books'].judul_buku}
        \rPK Penulis   = {context['books'].penulis_id}
        \rPenulis      = {context['books'].penulis}
        \rURL Penulis  = {context['books'].penulis.slug}
        \rPK Penerbit  = {context['books'].penerbit_id}
        \rPenerbit     = {context['books'].penerbit}
        \rURL Penerbit = {context['books'].penerbit.slug}
        \rHarga        = {context['books'].harga}
        \rSlug         = {context['books'].slug}
    """)
    return render(request, 'produk/detail.html', context)
