from django.urls import path
from .views import (IndexProductView, DetailProductView,
                    DetailStationery, filter)


app_name = "produk"

urlpatterns = [
    path('', IndexProductView.as_view(), name='index'),
    path('<str:c>/', filter, name='filter'),
    path('buku/<int:pk>/<slug:slug>/',
         DetailProductView.as_view(), name='detail-buku'),
    path('stationery/<int:pk>/<slug:slug>/',
         DetailStationery.as_view(), name='detail-stationery'),
]
