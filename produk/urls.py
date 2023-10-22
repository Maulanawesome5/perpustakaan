from django.urls import path
from . import views


app_name = "produk"

urlpatterns = [
    path('', views.index, name='index'),
    path('buku/<slug:inputSlug>/', views.detail, name='detail'),
]