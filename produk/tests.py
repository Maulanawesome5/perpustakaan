from django.test import TestCase
from django.urls import reverse
from .models import Buku, Penulis_Buku, Penerbit_Buku, Stationery


# Create your tests here.
class PenulisBukuModelTest(TestCase):
    """Unit test untuk model `Penulis_Buku`. Isi tabel berisi informasi sederhana"""

    def test_nama_penulis(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        self.assertEqual(str(penulis), "Ucup Surucup")


class PenerbitBukuModelTest(TestCase):
    """Unit test untuk model `Penulis_Buku`. Isi tabel berisi informasi sederhana"""

    def test_penerbit_string_representation(self):
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC",
                                                instansi="PT. XYZ")
        self.assertEqual(str(penerbit), "Penerbit ABC")


class BukuModelTest(TestCase):
    """Unit test untuk model produk `Buku`. Karena tabel buku berelasi dengan\
    tabel `Penulis_Buku` dan `Penerbit_Buku`,\nmaka wajib membuat instance penulis dan penerbit.
    """

    def test_judul_buku(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC")
        buku = Buku.objects.create(judul_buku="My Book", kategori="buku",
                                   penulis=penulis, penerbit=penerbit,
                                   tahun=2023, harga=50000, stok_barang=10,
                                   berat=0.1, panjang=17.9, lebar=17.9,
                                   jumlah_halaman=269, is_discount=True,
                                   discount=0, harga_diskon=0, deskripsi="Description")
        self.assertEqual(str(buku), "My Book")

    def test_total_discount(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC")
        buku = Buku.objects.create(judul_buku="My Book", kategori="buku",
                                   penulis=penulis, penerbit=penerbit,
                                   tahun=2023, berat=0.1, panjang=17.9, lebar=17.9,
                                   jumlah_halaman=269, deskripsi="Description",
                                   stok_barang=10, harga=150000, is_discount=True,
                                   discount=25, harga_diskon=0)
        buku.harga_diskon = buku.harga - (buku.harga * buku.discount / 100)
        self.assertEqual(int(buku.harga_diskon), 112500)


class StationeryModelTest(TestCase):
    def test_nama_produk_stationery(self):
        nama = Stationery.objects.create(nama_produk="Ballpoint")
        self.assertEqual(str(nama), "Ballpoint")

    def test_total_discount(self):
        atk = Stationery.objects.create(kategori="stationery", nama_produk="Ballpoint",
                                        stok_barang=50, harga=28000, is_discount=False,
                                        discount=0, harga_diskon=0)
        atk.is_discount = True
        atk.discount = 25
        atk.harga_diskon = atk.harga - (atk.harga * atk.discount / 100)
        self.assertEqual(int(atk.harga_diskon), 21000)


class RoutingTest(TestCase):
    def setUp(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC",
                                                instansi="Instansi XYZ")
        buku = Buku.objects.create(judul_buku="Buku Ini Berkualitas", kategori="buku",
                                   penulis=penulis, penerbit=penerbit, slug="buku-ini-berkualitas",
                                   tahun=2023, berat=0.1, panjang=17.9, lebar=17.9,
                                   jumlah_halaman=269, deskripsi="Description",
                                   stok_barang=10, harga=150000, is_discount=True,
                                   discount=25, harga_diskon=0)

    def test_index_url(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_penulis_url(self):
        url = reverse("penulis")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_penerbit_url(self):
        url = reverse("penerbit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_produk_url(self):
        url = reverse("produk:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_filter_url_buku(self):
        url = reverse("produk:filter", args=["buku"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_filter_url_stationery(self):
        url = reverse("produk:filter", args=["stationery"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
