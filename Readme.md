# Tentang Aplikasi

Aplikasi toko buku online (merupakan replika dari website **Gramedia.com**) yang saya beri nama "OnlineBookStore". Bukan hanya buku, ada juga peralatan tulis dan peralatan kantor / *stationery* yang bisa dibeli. Aplikasi ini berbasis web yang dibuat menggunakan bahasa pemrograman Python dan framework Django. DBMS aplikasi ini menggunakan PostgreSQL.

### Catatan Developer

Proyek ini awalnya adalah membuat aplikasi `perpustakaan` berbasis web. Namun saya langsung mengubah konsep dan mekanismenya menjadi seperti **toko buku online**. Mungkin beberapa orang kontributor akan heran mengapa terdapat folder bernama [perpustakaan](perpustakaan), bukannya `toko_buku`.

Karena proyek sudah terlanjut di *generate* dengan nama `perpustakaan`, maka kemungkinan akan rumit mengubahnya. Namun lain waktu pasti akan segera saya ubah menjadi `toko_buku` sesuai dengan mekanismenya.

## DISCLAIMER

APLIKASI INI DIBUAT BERTUJUAN UNTUK EDUKASI SEMATA. SAYA MEMBUAT INI KARENA SEDANG SENGGANG, DAN MUNGKIN DI MASA DEPAN AKAN BERGUNA SEBAGAI PROJECT SIAP PAKAI UNTUK TUGAS PERKULIAHAN ATAU PORTFOLIO SAAT MELAMAR PEKERJAAN.

BERIKUTNYA, SUMBER DAYA KONTEN SEPERTI GAMBAR COVER BUKU DAN FOTO PRODUK STATIONERY, LOGO PERUSAHAAN PENERBIT, FOTO PROFIL PENULIS, DAN SEMUA ISI DATABASE DIPEROLEH DARI BERBAGAI SITUS INTERNET DENGAN CARA DOWNLOAD ATAU COPY PASTE. HAL TERSEBUT TIDAK DIMAKSUDKAN UNTUK PEMBAJAKAN, PENCURIAN ATAU PELANGGARAN HAK CIPTA ATAS KARYA ATAU PRODUK RESMI SUATU PIHAK.

TUJUANNYA SEPERTI YANG TERTULIS PADA PARAGRAF PERTAMA. ADAPUN TUJUAN LAINNYA DARI SEGI TEKNIS PENGEMBANGAN APLIKASI, SEPERTI PENATAAN DESAIN LAYOUT DAN MEMPELAJARI BAGAIMANA MEKANISME SUATU APLIKASI TOKO BUKU. 

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

### 2. Pembuatan Virtual Environment

Virtual Environment adalah lingkungan pengembangan aplikasi Python yang secara khusus terisolasi dari interpreter utama Python, yang telah terinstal pada perangkat komputer. Tujuannya untuk memisahkan *package* atau modul yang ada pada interpreter utama, dengan yang hanya diperlukan untuk proyek ini. Cara untuk membuat virtual environment adalah buka terminal atau command prompt, navigasikan pada folder `toko_buku`. Kemudian ketikkan perintah ini pada terminal atau command prompt anda

```console
python -m venv Env
```

Maka seharusnya akan muncul suatu folder bernama `Env` di dalam proyek anda. Berikutnya `venv` merupakan nama *package* atau modul bawaan Python yang berfungsi untuk membuat lingkungan pengembangan virtual. Setelahnya, struktur folder proyek anda akan menjadi seperti ini

```
D:.
├───data
├───docs
├───Env          # Folder Env berisi instalasi modul
├───perpustakaan
....
├───manage.py
└───requirements.txt
```

### 3. Aktivasi Virtual Environment

Di dalam folder Env terdapat banyak file seperti interpreter Python versi virtual, dan file konfigurasi lainnya. Terutama file bernama `activate`, `activate.bat`, dan `activate.ps1` yang berfungsi untuk mengaktifkan virtual environment. Untuk mengaktifkan virtual environment hanya perlu mengetikkan perintah

1. Windows
```shell
Env\Scripts\activate.bat
```

Maka folder proyek anda akan menampilkan tulisan seperti `(Env) D:\toko_buku>` pada command prompt untuk pengguna Windows.

2. MacOS dan Linux
```shell
source Env/bin/activate
```

Maka folder proyek anda akan menampilkan tulisan seperti `(Env) your_name:$` pada terminal untuk pengguna MacOS dan Linux.

### 4. Instalasi Package pada Virtual Environment

Pada direktori proyek ini, terdapat suatu file bernama [requirements.txt](requirements.txt) yang berisi nama dan versi berbagai *package* atau modul Python yang hanya diperlukan untuk proyek ini. Anda perlu menginstalnya ke dalam virtual environment dengan mengetikan perintah pada terminal atau command prompt

```shell
pip install -r requirements.txt
```

Tunggu hingga proses instalasinya selesai. Jika berhasil dan tidak terdapat error maka jika anda mengetikkan perintah `pip list` pada terminal atau command prompt akan menampilkan hasil seperti ini

```terminal
(Env) D:\toko_buku>pip list
Package             Version
------------------- ---------
asgiref             3.7.2
certifi             2023.7.22
charset-normalizer  3.2.0
Django              4.1.13
django-crispy-forms 2.0
idna                3.4
mysqlclient         2.2.0
pip                 24.0
psycopg2            2.9.9
python-dotenv       1.0.0
requests            2.31.0
setuptools          63.2.0
sqlparse            0.4.4
typing_extensions   4.7.1
tzdata              2023.3
urllib3             2.0.4

(Env) D:\toko_buku>
```

### 5. Instalasi DBMS dan Pembuatan Database

Disini saya menggunakan *database management system* bernama PostgreSQL. Jika anda menggunakan lainnya seperti MySQL atau MariaDB/XAMPP, maka anda harus mengubah isi file [perpustakaan/settings.py](perpustakaan/settings.py) pada bagian variabel `DATABASES` dan menyesuaikannya dengan DBMS yang anda pakai, seperti di bawah ini

```python
DATABASES = {
    'default': {
                  # ubah postgresql menjadi mysql
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'toko_buku',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432, # ubah menjadi 3306
    }
}
```

Untuk DBMS lainnya yang tidak saya sebutkan silahkan mencari caranya di internet atau di [halaman ini](https://docs.djangoproject.com/en/4.1/ref/settings/#databases).

Berikutnya anda perlu membuat database bernama `toko_buku` pada DBMS yang anda pakai. Anda hanya perlu masuk ke Database client dan mengetikkan query seperti

```sql
CREATE DATABASE toko_buku;
```

Jika sudah berhasil dan tidak terdapat pesan error, maka anda bisa exit dari Database client.

### 6. Migrasi Model ke DBMS

Proses migrasi merupakan proses sinkronisasi dan konversi dari model framework menjadi tabel dalam database. Sampai pada tahap ini, **anda belum menjalankan server Django sama sekali**. Jika setup belum selesai, maka saya khawatir aplikasi akan mengalami error. Di sini kita akan mulai berinteraksi dengan perangkat manajemen dari Django, yaitu file [manage.py](manage.py)

Untuk melakukan proses migrasi, anda perlu mengetikkan perintah di bawah ini pada terminal atau command prompt:

```console
python manage.py migrate
```

Jika berhasil dan tidak ada pesan error pada saat proses migrasi, maka berikutnya anda bisa mencoba untuk menjalankan server Django.

> **WARNING>** Kurang dan lebihnya akan di update lain waktu....

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

### Error saat Dumpdata dan Loaddata

Saya pernah mengalami error saat melakukan proses restore data. Beberapa jenis error tersebut yang bisa saya sebutkan adalah seperti dibawah ini beserta dengan cara saya mengatasinya

Masalah Format Zona Waktu (Timezone)

Masalah Unicode Character

## Will be update soon
