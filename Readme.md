# Tentang Aplikasi

Aplikasi toko buku online (merupakan replika dari website **Gramedia.com**) yang saya beri nama "OnlineBookStore". Bukan hanya buku, ada juga peralatan tulis dan peralatan kantor / *stationery* yang bisa dibeli. Aplikasi ini berbasis web yang dibuat menggunakan bahasa pemrograman Python dan framework Django. DBMS aplikasi ini menggunakan PostgreSQL.

## DISCLAIMER

APLIKASI INI DIBUAT BERTUJUAN UNTUK EDUKASI SEMATA. SAYA MEMBUAT INI KARENA SEDANG SENGGANG, DAN MUNGKIN DI MASA DEPAN AKAN BERGUNA SEBAGAI PROJECT SIAP PAKAI UNTUK TUGAS PERKULIAHAN ATAU PORTFOLIO SAAT MELAMAR PEKERJAAN.

## PREREQUISITE

Beberapa hal yang harus anda pelajari dan persiapkan untuk mengembangkan project ini yaitu :

1. Belajar bahasa pemrograman Python.
   * Sudah menginstal interpreter Python. Bisa anda download di halaman [python.org](https://www.python.org/downloads/)
   * Pilih IDE atau Text Editor favoritmu (PyCharm, Visual Studio, Sublime, dsb).
   * Bisa mengakses Python dari Command Prompt atau Terminal.
2. Belajar basis data --> relational DBMS (MySQL, PostgreSQL, dsb).
   * Sudah menginstal DBMS dan terkoneksi ke server (localhost).
   * Bisa mengakses DBMS dari Command Prompt atau Terminal.
3. Terbiasa atau pernah memakai Command Prompt atau terminal Mac/Linux.
   * Karena kita akan menjalankan server Django
   * Kita perlu mencoba version control system seperti Git dan GitHub
4. Konsep arsitektur MVC (Model, View, Controller).
5. Rajin nonton YouTube tutorial ngoding !!
   1. Playlist Belajar Pemrograman
      * [Python Dasar](https://www.youtube.com/playlist?list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY)
      * [Python Object Oriented](https://www.youtube.com/playlist?list=PLZS-MHyEIRo7ab0-EveSvf4CLdyOECMm0)
      * [Web Framewok Django](https://www.youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld)
   2. Belajar Basis Data & DBMS
      * [MySQL](https://www.youtube.com/playlist?list=PL-CtdCApEFH_P2_2zR6pvDublvpD3fF6W)
      * [PostgreSQL](https://www.youtube.com/playlist?list=PL-CtdCApEFH8KU1ewoHnRb78AyQBCtkxd)

> **NOTE :** Akan di update atau berubah di lain waktu.

## Instalasi

Jika anda memutuskan untuk berkolaborasi dalam pengembangan aplikasi ini, maka sekarang saya akan menjelaskan cara instalasi dan cara menjalankan aplikasi "OnlineBookStore" ini.

### 1. Pembuatan Workspace

Buatlah suatu folder untuk memulai project ini di dalam komputer anda. Contohnya disini saya membuat folder bernama `toko_buku` di dalam Local Disk D. Setelahnya anda bisa melakukan git clone pada repository ini supaya lebih cepat dalam pengerjaan.

Cara melakukan clone adalah dengan membuka terminal atau command prompt anda ke folder `toko_buku`. Pastikan untuk sudah menginstal [Git](https://git-scm.com/downloads) di komputer anda. Setelahnya ketikan perintah ini

```console
git clone https://github.com/Maulanawesome5/perpustakaan.git
```

Maka sekarang, isi workspace `toko_buku` anda seharusnya seperti dibawah ini

```
D:.
├───data
├───docs
├───perpustakaan
├───produk
│   ├───migrations
│   ├───static
│   │   └───produk
│   │       ├───buku
│   │       ├───penerbit
│   │       ├───penulis
│   │       └───stationery
│   ├───templates
│   │   └───produk
├───static
│   ├───css
│   ├───icon
│   ├───img
│   ├───js
│   └───vendor
│       ├───bootstrap
│       └───jquery
├───templates
│    └───snippets
├───.gitignore
├───Readme.md
├───db.sqlite3
├───manage.py
└───requirements.txt
```

## Dumpdata dan Loaddata

Data yang telah dimasukkan ke dalam *database management system* / DBMS, khususnya disini saya menggunakan PostgreSQL bisa dikeluarkan atau dimasukkan (*backup & restore*). Jika anda ingin berkontribusi bersama dalam pengembangan aplikasi ini, saya telah membuatkan beberapa dan saya menaruhnya di dalam folder [data](data/). Jadi jika anda ingin menambahkan data baru atau menghapus suatu data tanpa memulainya dari awal, silahkan pergunakan file berformat JSON di dalam [data](data/).

Dibawah ini merupakan perintah untuk mengeluarkan / *dump data* dari DBMS :

```shell
python manage.py dumpdata produk.buku --indent 2 > "data/produk.buku.json"
```

Harap perhatikan konvensi atau aturan pemberian nama pada file backup demi mempermudah proses *backup & restore*. Disana saya menetapkan konvensi nama seperti `produk.buku.json` dimana **produk** adalah nama Django apps (folder bernama produk beserta semua isinya). Sedangkan **buku** merupakan nama python class di dalam file [models.py](produk/models.py). Class tersebut akan di konversi menjadi tabel di dalam DBMS PostgreSQL. Demikian juga untuk dua tabel lainnya dalam Django apps **produk** anda harus menggunakan perintah

```shell
# Dump data tabel penerbit buku
python manage.py dumpdata produk.penerbit_buku --indent 2 > "data/produk.penerbit.json"

# Dump data tabel penulis buku
python manage.py dumpdata produk.penulis_buku --indent 2 > "data/produk.penulis.json"
```

Berikutnya adalah penjelasan tentang memuat data (*loaddata*) / proses *restore* dari file JSON yang berada di dalam folder [data](data), dimasukkan ke dalam DBMS yang akan dipakai. Gunakan perintah seperti di bawah ini :

```shell
# Load data tabel penerbit buku
python manage.py loaddata "data/produk.penerbit.json"

# Load data tabel penulis buku
python manage.py loaddata "data/produk.penulis.json"
```

Jika anda hanya ingin melakukan restore terhadap data [produk](produk/models.py) saja, maka anda harus memulainya terlebih dulu dari penerbit ataupun penulis. Jika anda melakukan restore dari data [buku](data/produk.buku.json) terlebih dahulu maka akan terjadi error, sebab data itu memiliki *foreign key* yang terhubung dengan tabel penerbit dan tabel penulis.

## Will be update soon
