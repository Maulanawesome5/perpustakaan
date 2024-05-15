from django.contrib import admin
from .models import Buku, Penulis_Buku, Penerbit_Buku, Stationery


# Register your models here.
class Admin_Produk(admin.ModelAdmin):
    readonly_fields = ["slug", "updated", "created", "kategori",]


admin.site.register(Buku, Admin_Produk)
admin.site.register(Penulis_Buku, Admin_Produk)
admin.site.register(Penerbit_Buku, Admin_Produk)
admin.site.register(Stationery, Admin_Produk)
