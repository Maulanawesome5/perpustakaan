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

def penulis(request):
    penulis_buku = Penulis_Buku.objects.all()
    context = {
        'penulis': penulis_buku,
        'halaman': 'Profil Penulis',
        'website': 'Perpustakaan'
    }
    return render(request, 'produk/penulis.html', context)
