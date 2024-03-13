from django.http import HttpResponse
from django.shortcuts import render
from produk.models import Buku as data_buku
from produk.models import Penulis_Buku as data_penulis
from produk.models import Penerbit_Buku as data_penerbit


def index(request):
    buku = data_buku.objects.all()
    context = {
        'books':buku,
        'halaman':'Beranda',
        'website':'OnlineBookStore'
    }
    return render(request, 'index.html', context)

def penulis(request):
    penulis_buku = data_penulis.objects.all()
    context = {
        'daftar_penulis': penulis_buku,
        'halaman': 'Daftar Penulis',
        'website': 'OnlineBookStore'
    }
    return render(request, 'penulis.html', context)

def detail_penulis(request, id, inputSlug):
    penulis_buku = data_penulis.objects.get(id=id, slug=inputSlug)
    buku_terkait = data_buku.objects.filter(penulis_id=id)
    context = {
        'website': 'OnlineBookStore'
    }
    try:
        context['data_penulis'] = penulis_buku
        context['halaman'] = penulis_buku.nama_penulis
        context['related_book'] = buku_terkait
        return render(request, 'detail.html', context)
    except:
        return HttpResponse("Disini halaman detail penulis buku ")

def penerbit(request):
    penerbit_buku = data_penerbit.objects.all()
    context = {
        'daftar_penerbit': penerbit_buku,
        'halaman': 'Daftar Penerbit',
        'website': 'OnlineBookStore'
    }
    return render(request, 'penerbit.html', context)

def detail_penerbit(request, id, inputSlug):
    penerbit_buku = data_penerbit.objects.get(id=id, slug=inputSlug)
    buku_terkait = data_buku.objects.filter(penerbit_id=id)
    context = {
        'website': 'OnlineBookStore'
    }
    try:
        context['data_penerbit'] = penerbit_buku
        context['halaman'] = penerbit_buku.penerbit
        context['related_book'] = buku_terkait
        return render(request, 'detail.html', context)
    except:
        return HttpResponse("Disini halaman detail penerbit buku.")
