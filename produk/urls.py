from django.urls import path
from . import views


app_name = "produk"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:c>/', views.filter, name='filter'),
    path('buku/<slug:inputSlug>/', views.detail_buku, name='detail-buku'),
    path('stationery/<slug:inputSlug>/', views.detail_stationery,
         name='detail-stationery'),
]
