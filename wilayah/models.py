from django.db import models


# Create your models here.
class Provinsi(models.Model):
    provinsi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. {self.provinsi}"

    class Meta:
        ordering = ["id"]


class Kabupaten_Kota(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    kabupaten_kota = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id}. {self.kabupaten_kota}"

    class Meta:
        ordering = ["id"]
