from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView
from .models import Buku, Stationery, Penulis_Buku, Penerbit_Buku


class IndexProductView(ListView):
    """
    Class View untuk menampilkan halaman Beranda produk.
    """
    template_name = "produk/index.html"
    model = Buku
    context_object_name = "books"
    extra_context = {'halaman': 'Produk', 'website': 'OnlineBookStore'}

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["stationery"] = Stationery.objects.all()

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        print("Isi data QuerySet:\n{}".format(self.queryset))

        return super().get(request, *args, **kwargs)


class SearchResultView(ListView):
    """
    Class View untuk melakukan pencarian data.
    """
    model = Buku
    template_name = "search.html"
    extra_context = {}

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")
        object_list = Buku.objects.filter(
            Q(title__icontains=query)
        )

        # Update context dengan kata kunci dari pencarian di HTML
        self.extra_context.update({"keyword": query})

        return object_list

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.queryset = self.get_queryset()
        not_found = len(self.queryset)

        if not_found == 0:
            self.extra_context.update({
                "message": "Tidak ditemukan."
            })

        return super().get(request, *args, **kwargs)


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


class DetailStationery(DetailView):
    template_name = "produk/detail.html"
    model = Stationery
    context_object_name = "stationery"
    extra_context = {"halaman": "", "website": "OnlineBookStore"}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True

        if request.method == "GET":
            self.extra_context.update({
                "halaman": Stationery.objects.get(id=kwargs.get("pk")).nama_produk,
            })

        return super().get(request, *args, **kwargs)


class DetailProductView(DetailView):
    template_name = "produk/detail.html"
    model = Buku
    context_object_name = "books"
    extra_context = {"halaman": "", "website": "OnlineBookStore"}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print("Isi context\n{}\n".format(context))
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True

        if request.method == "GET":

            self.extra_context.update({
                "halaman": Buku.objects.get(id=kwargs.get("pk")).judul_buku,
            })

            # berisi AnonymousUser jika tidak login
            print("Siapa user saat ini: {}\n".format(request.user))

            # berisi dict pk dan slug produk
            # {'pk': 20, 'slug': 'anggara-kasih'}
            print("Isi data kwargs\n{}\n".format(kwargs))

        return super().get(request, *args, **kwargs)


class AuthorListView(ListView):
    """
    Class View untuk menampilkan halaman Beranda penulis buku.
    """
    model = Penulis_Buku
    context_object_name = "daftar_penulis"
    extra_context = {"halaman": "Daftar Penulis",
                     "website": "OnlineBookStore"}


class AuthorDetailView(DetailView):
    """
    Class View untuk menampilkan halaman Detail penulis buku yang dipilih (di klik).
    """
    model = Penulis_Buku
    context_object_name = "data_penulis"
    extra_context = {"halaman": "", "website": "OnlineBookStore"}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True
        self.queryset = Penulis_Buku.objects.filter(id=kwargs.get("pk"))

        if request.method == "GET":
            self.extra_context.update({
                "halaman": Penulis_Buku.objects.get(id=kwargs.get("pk")).nama_penulis,
                "related_book": Buku.objects.filter(penulis_id=kwargs.get("pk")),
            })

        return super().get(request, *args, **kwargs)


class PublisherListView(ListView):
    """
    Class View untuk menampilkan halaman Beranda penerbit buku.
    """
    model = Penerbit_Buku
    context_object_name = "daftar_penerbit"
    extra_context = {"halaman": "Daftar Penerbit",
                     "website": "OnlineBookStore"}


class PublisherDetailView(DetailView):
    """
    Class View untuk menampilkan halaman Detail penerbit buku yang dipilih (di klik).
    """
    model = Penerbit_Buku
    context_object_name = "data_penerbit"
    extra_context = {"halaman": "", "website": "OnlineBookStore"}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True
        self.queryset = Penerbit_Buku.objects.filter(id=kwargs.get("pk"))

        if request.method == "GET":
            self.extra_context.update({
                "halaman": Penerbit_Buku.objects.get(id=kwargs.get("pk")).penerbit,
                "related_book": Buku.objects.filter(penerbit_id=kwargs.get("pk")),
            })

        return super().get(request, *args, **kwargs)
