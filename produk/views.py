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

    """
    # cara akses data dari queryset
    if request.method == "GET":
        print("\n")
        print("Debugging Log")
        print(buku[0].judul_buku)
        print(buku[0].harga)
        print(buku[0].penulis)
        print(buku[0].penerbit)
        print("\n")
    """

    return render(request, 'produk/index.html', context)

def detail(request, inputSlug):
    buku = Buku.objects.get(slug=inputSlug)
    context = {
        'books': buku,
        'halaman': 'Detail Buku',
        'website': 'Perpustakaan'
    }
    return render(request, 'produk/detail.html', context)

def penulis(request):
    penulis_buku = Penulis_Buku.objects.all()
    context = {
        'penulis': penulis_buku,
        'halaman': 'Profil Penulis',
        'website': 'Perpustakaan'
    }
    if request.method == "GET":
        print("\n")
        print(penulis_buku)
        print("\n")
    return render(request, 'produk/penulis.html', context)

# def profilPenulis(request, id):
#     """
#     Masih gagal diakses
#     """
#     penulis = Penulis_Buku.objects.get(penulis_id=id)
#     context = {
#         'halaman': 'Profil Penulis',
#         'profiles': penulis,
#         'website': 'Perpustakaan'
#     }
#     return render(request, 'produk/penulis.html', context)
