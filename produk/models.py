from django.db import models
from django.utils.text import slugify


# Create your models here.
class Abstract_Product(models.Model):
    """
    CLass abstrak yang menampung beberapa properti data yang sama dan diwarisi oleh class lainnya.
    """
    __OPSI_KATEGORI = (("penulis", "Penulis"),
                       ("penerbit", "Penerbit"),
                       ("buku", "Buku"),
                       ("stationery", "Stationery"))

    def get_category_data(self):
        """Method getter untuk mengakses variabel `__OPSI_KATEGORI`"""
        return self.__OPSI_KATEGORI

    def set_category_data(self, w=False, p=False, b=False, s=False):
        """
        Method setter untuk mengubah nilai atribut atau kolom `kategori`.
        Function ini berguna untuk query filter data.
            - Parameter `w` artinya writer atau penulis buku.
            - Parameter `p` artinya publisher atau penerbit buku.
            - Parameter `b` artinya produk buku
            - Parameter `s` artinya produk stationery (alat tulis)
        """
        try:
            if w == True:
                self.kategori = self.get_category_data()[0][0]
                self.save(force_insert=True, force_update=True)
            if p == True:
                self.kategori = self.get_category_data()[1][0]
                self.save(force_insert=True, force_update=True)
            if b == True:
                self.kategori = self.get_category_data()[2][0]
                self.save(force_insert=True, force_update=True)
            if s == True:
                self.kategori = self.get_category_data()[3][0]
                self.save(force_insert=True, force_update=True)
        except:
            return False

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, editable=False)
    kategori = models.CharField(max_length=50, blank=True, editable=False)

    class Meta:
        abstract = True


class Penulis_Buku(Abstract_Product):
    """Class ini merupakan data model tentang seorang `penulis buku`."""
    nama_penulis = models.CharField(max_length=100, unique=True)
    nama = models.CharField(max_length=100, blank=True)
    tentang_penulis = models.TextField(blank=True)
    foto_profil = models.CharField(max_length=100, blank=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama_penulis)
        self.set_category_data(w=True)
        super(Penulis_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nama_penulis

    def get_class_name(self):
        return self.__class__.__name__

    class Meta:
        ordering = ['nama_penulis']


class Penerbit_Buku(Abstract_Product):
    """Class ini merupakan data model perusahaan `penerbit buku`."""
    penerbit = models.CharField(max_length=100, unique=True)
    instansi = models.CharField(max_length=100)
    tentang_penerbit = models.TextField(blank=True)
    logo_penerbit = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.instansi)
        self.set_category_data(p=True)
        super(Penerbit_Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.penerbit}"

    def get_class_name(self):
        return self.__class__.__name__

    class Meta:
        ordering = ['penerbit']


class Buku(Abstract_Product):
    """Class ini merupakan model untuk data `produk buku`."""
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

    def is_discounted(self):
        """
        Function setter untuk memeriksa kondisi kolom field `is_discount`. Jika field
        tersebut bernilai True, maka akan mengeksekusi function `price_after_discount`.
        Jika `is_discount` bernilai False, maka fields `discount` dan `harga_diskon`
        akan di setting kembali menjadi nilai defaultnya.
        """
        if self.is_discount == True:
            self.price_after_discount()

        else:
            self.discount = 0
            self.harga_diskon = 0

    def price_after_discount(self) -> int:
        """Jika terdapat diskon, maka harga final produk adalah setelah dikurangi diskon."""
        self.harga_diskon = self.harga - (self.harga * self.discount / 100)

    def save(self, *args, **kwargs):
        # Function ini akan dieksekusi pada setiap perubahan data
        # saat menekan tombol save pada Halaman Admin
        self.slug = slugify(self.judul_buku)
        self.set_category_data(b=True)
        self.is_discounted()

        super(Buku, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.judul_buku

    def get_class_name(self):
        return self.__class__.__name__

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

    def is_discounted(self):
        """
        Function setter untuk memeriksa kondisi kolom field `is_discount`. Jika field
        tersebut bernilai True, maka akan mengeksekusi function `price_after_discount`.
        Jika `is_discount` bernilai False, maka fields `discount` dan `harga_diskon`
        akan di setting kembali menjadi nilai defaultnya.
        """
        if self.is_discount == True:
            self.price_after_discount()

        else:
            self.discount = 0
            self.harga_diskon = 0

    def price_after_discount(self) -> int:
        """Jika terdapat diskon, maka harga final produk adalah setelah dikurangi diskon."""
        self.harga_diskon = self.harga - (self.harga * self.discount / 100)

    def save(self, *args, **kwargs):
        # Function ini akan dieksekusi pada setiap perubahan data
        # saat menekan tombol save pada Halaman Admin
        self.slug = slugify(self.nama_produk)
        self.set_category_data(s=True)
        self.is_discounted()

        super(Stationery, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nama_produk

    def get_class_name(self):
        return self.__class__.__name__

    class Meta:
        ordering = ['nama_produk']
