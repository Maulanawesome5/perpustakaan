from django.http import HttpResponse
from django.shortcuts import render
from produk.models import Buku as data_buku
from produk.models import Penulis_Buku as data_penulis


def index(request):
    buku = data_buku.objects.all()
    context = {
        'books':buku,
        'halaman':'Beranda',
        'website':'Perpustakaan'
    }
    return render(request, 'index.html', context)

def penulis(request):
    penulis_buku = data_penulis.objects.all()
    context = {
        'daftar_penulis': penulis_buku,
        'halaman': 'Daftar Penulis',
        'website': 'Perpustakaan'
    }
    return render(request, 'penulis.html', context)

def detail_penulis(request, id, inputSlug):
    penulis_buku = data_penulis.objects.get(id=id, slug=inputSlug)
    context = {
        'website': 'Perpustakaan'
    }
    try:
        context['data_penulis'] = penulis_buku
        context['halaman'] = penulis_buku.nama_penulis
        return render(request, 'detail.html', context)
    except:
        return HttpResponse("Disini halaman detail penulis buku ")
    # context = {
    #     'data_penulis': penulis_buku,
    #     'halaman': 'Detail Penulis',
    #     'website': 'Perpustakaan'
    # }
    # return render(request, 'detail.html', context)
