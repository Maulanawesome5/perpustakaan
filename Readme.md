# Tentang Aplikasi

Aplikasi Pengelolaan Pustaka Buku (Perpustakaan) berbasis web yang dibuat menggunakan bahasa pemrograman Python dan framework Django.

## Cara Dumpdata dan Loaddata

Data yang telah dimasukkan ke dalam database akan di keluarkan menjadi suatu file berformat JSON. Disini saya.... **bla bla bla nanti diteruskan di rumah**

```shell
python manage.py dumpdata produk.buku --indent 2 > "data/produk.buku.json"
```

Untuk dua tabel lainnya dalam database ```produk``` juga **bla bla bla lanjut di rumah**

```shell
# Dump data tabel penerbit buku
python manage.py dumpdata produk.penerbit_buku --indent 2 > "data/produk.penerbit.json"

# Dump data tabel penulis buku
python manage.py dumpdata produk.penulis_buku --indent 2 > "data/produk.penulis.json"
```

## Will be update soon
