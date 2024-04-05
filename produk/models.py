from django.db import models
from django.utils.text import slugify


# Create your models here.
class Abstract_Product(models.Model):
    OPSI_KATEGORI = (("penulis", "Penulis"),
                     ("penerbit", "Penerbit"),
                     ("buku", "Buku"),
                     ("stationery", "Stationery"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, editable=False)
    kategori = models.CharField(max_length=50, choices=OPSI_KATEGORI)

    class Meta:
        abstract = True


class Penulis_Buku(Abstract_Product):
    nama_penulis = models.CharField(max_length=100, unique=True)
    nama = models.CharField(max_length=100, blank=True)
    tentang_penulis = models.TextField(blank=True)
    foto_profil = models.CharField(max_length=100, blank=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama_penulis)
        super(Penulis_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nama_penulis

    class Meta:
        ordering = ['nama_penulis']


class Penerbit_Buku(Abstract_Product):
    penerbit = models.CharField(max_length=100, unique=True)
    instansi = models.CharField(max_length=100)
    tentang_penerbit = models.TextField(blank=True)
    logo_penerbit = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.instansi)
        super(Penerbit_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.penerbit}"

    class Meta:
        ordering = ['penerbit']


class Buku(Abstract_Product):
    judul_buku = models.CharField(max_length=255, unique=True)
    penulis = models.ForeignKey(Penulis_Buku, on_delete=models.CASCADE)
    penerbit = models.ForeignKey(Penerbit_Buku, on_delete=models.CASCADE)
    tahun = models.IntegerField()
    deskripsi = models.TextField()
    sampul_buku = models.CharField(max_length=255, blank=True)
    thumbnail_sampul = models.CharField(max_length=255, blank=True)
    harga = models.IntegerField(default=0)
    stok_barang = models.IntegerField(default=0)
    isbn = models.CharField(max_length=255, blank=True)
    berat = models.FloatField(default=0.0)
    panjang = models.FloatField(default=0.0)
    lebar = models.FloatField(default=0.0)
    jumlah_halaman = models.IntegerField(default=0)
    is_discount = models.BooleanField(default=False)  # False-True
    discount = models.IntegerField(blank=True, null=True)
    harga_diskon = models.IntegerField(default=0)  # price-(price*discount/100)

    def price_after_discount(self) -> int:
        """Jika terdapat diskon, maka harga final produk adalah setelah dikurangi diskon."""
        self.harga_diskon = self.harga - (self.harga * self.discount / 100)

    def save(self, *args, **kwargs):
        # Function ini akan dieksekusi pada setiap perubahan data
        # saat menekan tombol save pada Halaman Admin
        self.slug = slugify(self.judul_buku)

        if self.is_discount == True:
            self.price_after_discount()
        elif self.is_discount == False:
            self.discount = 0
            self.harga_diskon = 0

        super(Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.judul_buku

    class Meta:
        ordering = ['judul_buku']


class Stationery(Abstract_Product):
    nama_produk = models.CharField(max_length=255)
    gambar_produk = models.CharField(max_length=255, blank=True)
    stok_barang = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)
    is_discount = models.BooleanField(default=False)  # False-True
    discount = models.IntegerField(blank=True, null=True)
    harga_diskon = models.IntegerField(default=0)  # price-(price*discount/100)

    def price_after_discount(self) -> int:
        """Jika terdapat diskon, maka harga final produk adalah setelah dikurangi diskon."""
        self.harga_diskon = self.harga - (self.harga * self.discount / 100)

    def save(self, *args, **kwargs):
        # Function ini akan dieksekusi pada setiap perubahan data
        # saat menekan tombol save pada Halaman Admin
        self.slug = slugify(self.nama_produk)

        if self.is_discount == True:
            self.price_after_discount()
        elif self.is_discount == False:
            self.discount = 0
            self.harga_diskon = 0

        super(Stationery, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nama_produk

    class Meta:
        ordering = ['nama_produk']
