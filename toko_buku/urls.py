from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('penulis/', views.penulis, name="penulis"),
    path('penulis/<int:id>/<str:inputSlug>',
         views.detail_penulis, name="writer_detail"),
    path('penerbit/', views.penerbit, name="penerbit"),
    path('penerbit/<int:id>/<str:inputSlug>',
         views.detail_penerbit, name="publisher_detail"),
    path('produk/', include("produk.urls", namespace="produk")),
]