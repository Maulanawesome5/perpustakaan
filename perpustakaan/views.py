from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from produk.models import Buku as data_buku
from produk.models import Penulis_Buku as data_penulis
from produk.models import Penerbit_Buku as data_penerbit


# # Views untuk beranda aplikasi
def index(request):
    buku = data_buku.objects.all()
    context = {
        'books': buku,
        'halaman': 'Beranda',
        'website': 'OnlineBookStore'
    }
    return render(request, 'index.html', context)


# # Views menampilkan `halaman belum dibuat`
def under_cons(request):
    messages = "<h1>Page is under construction. Come back later!</h1>"
    return HttpResponse(messages)


# # Views untuk penulis buku
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
        if request.method == 'GET':
            context.update({
                'data_penulis': penulis_buku,
                'halaman': penulis_buku.nama_penulis,
                'related_book': buku_terkait,
            })
            return render(request, 'detail.html', context)
    except data_penulis.DoesNotExist:
        return get_object_or_404(data_penulis, id=id, slug=inputSlug)


# # Views untuk penerbit buku
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
        if request.method == 'GET':
            context.update({
                'data_penerbit': penerbit_buku,
                'halaman': penerbit_buku.penerbit,
                'related_book': buku_terkait,
            })
            return render(request, 'detail.html', context)
    except data_penerbit.DoesNotExist:
        return get_object_or_404(data_penerbit, id=id, slug=inputSlug)
