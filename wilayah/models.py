from django.db import models


# Create your models here.
class Provinsi(models.Model):
    provinsi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. {self.provinsi}"

    class Meta:
        ordering = ["id"]


class Kabupaten_Kota(models.Model):
    PREDIKAT_CHOICES = (("Kabupaten", "Kabupaten"), ("Kota", "Kota"),
                        ("DKI", "Daerah Khusus Ibukota"), ("DI", "Daerah Istimewa"),
                        ("Kota Adm.", "Kota Administrasi"), ("Kab. Adm.", "Kabupaten Administrasi"))
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    predikat = models.CharField(max_length=20, blank=True, null=True,
                                choices=PREDIKAT_CHOICES)
    kabupaten_kota = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.predikat} {self.kabupaten_kota}"

    class Meta:
        ordering = ["provinsi_id", "id"]


class Distrik(models.Model):
    # distrik = models.CharField(max_length=50)
    pass
