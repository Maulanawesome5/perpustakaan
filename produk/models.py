from django.db import models
from django.utils.text import slugify


# Create your models here.
class Abstract_Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, editable=False)

    class Meta:
        abstract = True


class Penulis_Buku(Abstract_Product):
    nama_penulis = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama_penulis)
        super(Penulis_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nama_penulis
    
    class Meta:
        ordering = ['nama_penulis']


class Penerbit_Buku(Abstract_Product):
    penerbit = models.CharField(max_length=100)
    instansi = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.instansi)
        super(Penerbit_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.penerbit}"

    class Meta:
        ordering = ['penerbit']


class Buku(Abstract_Product):
    judul_buku = models.CharField(max_length=255)
    penulis = models.ForeignKey(Penulis_Buku, on_delete=models.CASCADE, default='')
    penerbit = models.ForeignKey(Penerbit_Buku, on_delete=models.CASCADE, default='')
    tahun = models.IntegerField()
    deskripsi = models.TextField()
    sampul_buku = models.CharField(max_length=255, blank=True)
    thumbnail_sampul = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_buku)
        super(Buku, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.judul_buku
    
    class Meta:
        ordering = ['judul_buku']
