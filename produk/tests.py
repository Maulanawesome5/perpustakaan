from django.test import TestCase
from django.urls import reverse
from .models import Buku, Penulis_Buku, Penerbit_Buku

# Create your tests here.
class PenulisBukuModelTest(TestCase):
    def test_nama_penulis(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        self.assertEqual(str(penulis), "Ucup Surucup")


class PenerbitBukuModelTest(TestCase):
    def test_penerbit_string_representation(self):
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC", instansi="PT. XYZ")
        self.assertEqual(str(penerbit), "Penerbit ABC")


class BukuModelTest(TestCase):
    def test_judul_buku(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC", instansi="PT. XYZ")
        buku = Buku.objects.create(judul_buku="My Book", penulis=penulis, penerbit=penerbit, tahun=2023, deskripsi="Description")
        self.assertEqual(str(buku), "My Book")


class RoutingTest(TestCase):
    def setUp(self):
        penulis = Penulis_Buku.objects.create(nama_penulis="Ucup Surucup")
        penerbit = Penerbit_Buku.objects.create(penerbit="Penerbit ABC", instansi="Instansi XYZ")
        buku = Buku.objects.create(
            slug="sample-slug",
            judul_buku="Sample Book",
            penulis=penulis,
            penerbit=penerbit,
            tahun=2018,
            deskripsi="Lorem ipsum dolor sit amet"
        )

    def test_index_url(self):
        url = reverse("produk:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_url(self):
        url = reverse("produk:detail", args=["sample-slug"])
        response = self.client.get(url)
        print(response.content)
        self.assertEqual(response.status_code, 200)

