from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from produk.models import Buku as Book, Stationery


class IndexHomePagesViews(ListView):
    template_name = "index.html"
    queryset = Book.objects.all() \
        .exclude(stok_barang=0) \
        .order_by("-harga", "discount")[:40]

    context_object_name = "books"
    extra_context = {"halaman": "Beranda", "website": "OnlineBookStore"}

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["stationery"] = Stationery.objects.all()

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
