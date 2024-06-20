from django.contrib import admin
from django.urls import path, include
from produk.views import (AuthorListView, AuthorDetailView,
                          PublisherListView, PublisherDetailView, SearchResultView)
from .views import IndexHomePagesViews


urlpatterns = [
    path('', IndexHomePagesViews.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('penulis/', AuthorListView.as_view(), name="penulis"),
    path('penulis/<int:pk>/<slug:slug>',
         AuthorDetailView.as_view(), name="writer_detail"),
    path('penerbit/', PublisherListView.as_view(), name="penerbit"),
    path('penerbit/<int:pk>/<slug:slug>',
         PublisherDetailView.as_view(), name="publisher_detail"),
    path('produk/', include("produk.urls", namespace="produk")),
    path('search/', SearchResultView.as_view(), name="search_result"),
]
