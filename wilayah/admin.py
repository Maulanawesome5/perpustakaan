from django.contrib import admin
from .models import Provinsi, Kabupaten_Kota


# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ("kabupaten_kota", "provinsi",)


admin.site.register(Provinsi)
admin.site.register(Kabupaten_Kota, RegionAdmin)
