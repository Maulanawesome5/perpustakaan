from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from produk.models import Buku as data_buku
from produk.models import Penulis_Buku as data_penulis
from produk.models import Penerbit_Buku as data_penerbit


def index(request):
    """Function untuk menampilkan halaman beranda website."""
    buku = data_buku.objects.all()
    context = {
        "books": buku,
        "halaman": "Beranda",
        "website": "OnlineBookStore",
    }
    # print(f"\nSiapa User aktif saat ini: {request.user}")
    # print(f"Apa User aktif ter-autentikasi: {request.user.is_authenticated}\n")
    return render(request, "index.html", context)


def penulis(request):
    """Function untuk menampilkan seluruh daftar penulis buku."""
    penulis_buku = data_penulis.objects.all()
    context = {
        "daftar_penulis": penulis_buku,
        "halaman": "Daftar Penulis",
        "website": "OnlineBookStore",
    }
    return render(request, "penulis.html", context)


def detail_penulis(request, id, inputSlug):
    """Function untuk menampilkan detail profil dari penulis buku yang dilihat user."""
    penulis_buku = data_penulis.objects.get(id=id, slug=inputSlug)
    buku_terkait = data_buku.objects.filter(penulis_id=id)
    context = {
        "website": "OnlineBookStore"
    }
    try:
        if request.method == "GET":
            context.update({
                "data_penulis": penulis_buku,
                "halaman": penulis_buku.nama_penulis,
                "related_book": buku_terkait,
            })
            return render(request, "detail.html", context)
    except data_penulis.DoesNotExist:
        return get_object_or_404(data_penulis, id=id, slug=inputSlug)


def penerbit(request):
    """Function untuk menampilkan seluruh daftar penerbit buku."""
    penerbit_buku = data_penerbit.objects.all()
    context = {
        "daftar_penerbit": penerbit_buku,
        "halaman": "Daftar Penerbit",
        "website": "OnlineBookStore"
    }
    return render(request, "penerbit.html", context)


def detail_penerbit(request, id, inputSlug):
    """Function untuk menampilkan detail profil dari penerbit buku yang dilihat user."""
    penerbit_buku = data_penerbit.objects.get(id=id, slug=inputSlug)
    buku_terkait = data_buku.objects.filter(penerbit_id=id)
    context = {
        "website": "OnlineBookStore"
    }
    try:
        if request.method == "GET":
            context.update({
                "data_penerbit": penerbit_buku,
                "halaman": penerbit_buku.penerbit,
                "related_book": buku_terkait,
            })
            return render(request, "detail.html", context)
    except data_penerbit.DoesNotExist:
        return get_object_or_404(data_penerbit, id=id, slug=inputSlug)
