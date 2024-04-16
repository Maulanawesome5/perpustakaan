-- Active: 1690520036101@@127.0.0.1@5432@toko_buku@public#produk_buku
SELECT * FROM produk_buku; -- Seleksi semua kolom pada tabel buku
SELECT * FROM produk_penerbit_buku; -- Seleksi semua kolom pada tabel penerbit
SELECT * FROM produk_penulis_buku; -- Seleksi semua kolom pada tabel penulis buku
SELECT * FROM produk_stationery; -- Seleksi semua kolom produk stationery

SELECT judul_buku, tahun, isbn, deskripsi, harga, stok_barang
FROM public.produk_buku
ORDER BY judul_buku ASC; -- Seleksi beberapa kolom saja

-- Seleksi dengan alias
SELECT book.judul_buku AS "Judul",
        book.harga AS "Harga",
        book.stok_barang AS "Stok",
        (book.harga * book.stok_barang) AS "Total Harga"
FROM public.produk_buku AS book;

-- Cara seleksi dan join 3 tabel serta diberikan alias
SELECT book.judul_buku AS "Judul",
        book.tahun AS "Tahun",
        book.harga AS "Harga Rp.",
        wrt.nama_penulis AS "Penulis",
        pub.penerbit AS "Penerbit"
FROM public.produk_buku AS book
JOIN public.produk_penerbit_buku AS pub ON (pub.id = book.penerbit_id)
JOIN public.produk_penulis_buku AS wrt ON (wrt.id = book.penulis_id)
ORDER BY book.judul_buku ASC;

-- UPDATE data dengan klausa WHERE
-- AWAS..!! Tanda kutip ' ' dan tanda kutip " " memiliki makna yang berbeda.
--      Tanda ' ' digunakan untuk menampung nilai kolom.
--      Tanda " " digunakan untuk memberikan nama kolom atau alias (AS).
UPDATE public.produk_buku
        SET kategori = 'buku'
        WHERE kategori != 'buku';

UPDATE public.produk_penerbit_buku
        SET kategori = 'penerbit'
        WHERE kategori != 'penerbit';

UPDATE public.produk_penulis_buku
        SET kategori = 'penulis'
        WHERE kategori != 'penulis';

UPDATE public.produk_buku
        SET deskripsi = 'Date A Live, adalah seri novel ringan Jepang yang ditulis oleh Koushi Tachibana, dengan ilustrasi oleh Tsunako. Ia diterbitkan oleh Fujimi Shobo di bawah label Fujimi Fantasia Bunko mereka. Novel ini pertama kali diterbitkan pada Maret 2011 dan telah selesai sebanyak 22 volume pada Maret 2020. Pada bulan April 2013, adaptasi anime dimulai yang mencakup peristiwa volume 1-4 novel ringan dan berakhir pada bulan Juni 2013. Dub Musim 1 dirilis pada 10 Juni 2014 oleh FUNimation. Musim kedua, berjudul Date A Live II, ditayangkan pada 11 April 2014 hingga 13 Juni 2014 yang meliput peristiwa dari volume 5-7. Versi film dari serial ini, berjudul Date A Live: Mayuri Judgment diumumkan pada akhir musim kedua dan dirilis pada 22 Agustus 2015. Sebuah proyek anime baru diumumkan di Fantasia Bunko Festival pada tanggal 21 Oktober 2017. Anime tersebut berjudul Date A Live III, tayang perdana pada tanggal 11 Januari 2019 dan selesai pada tanggal 29 Maret 2019. Pada tanggal 23 September 2019, dua proyek anime baru diumumkan. proyek anime diumumkan, dan pada 16 Maret 2020, Koushi Tachibana mengonfirmasi bahwa salah satu proyek tersebut adalah musim keempat animenya. Anime bertajuk Date A Live IV ini resmi tayang mulai 8 April 2022 hingga 24 Juni 2022. Season kelima bertajuk Date A Live V telah dikonfirmasi pada 24 Juni 2022.'
        WHERE judul_buku LIKE '%DATE A LIVE%';

-- Menghitung total stok buku beserta harganya
-- Hasilnya sekitar Rp. 304.518.830 (tiga ratus juta) total harga buku yang dimiliki toko
SELECT count(book.judul_buku) AS "Total Judul Buku",
        sum(book.stok_barang) AS "Total Stok Buku",
        sum((book.harga * book.stok_barang)) AS "Total Harga Pasokan"
FROM public.produk_buku AS book;


-- Django apps Wilayah
-- Query tabel wilayah (Provinsi, Kabupaten/Kota, Kecamatan)
SELECT * FROM pg_tables WHERE schemaname = 'public'; -- Melihat daftar tabel

SELECT * FROM wilayah_provinsi; SELECT * FROM wilayah_kabupaten_kota;

SELECT  prov.id AS "Kode Provinsi",
        prov.provinsi AS "Provinsi",
        kab.id AS "Kode Kota/Kabupaten",
        kab.predikat AS "Predikat",
        kab.kabupaten_kota AS "Kabupaten/Kota"
FROM public.wilayah_kabupaten_kota AS kab
JOIN public.wilayah_provinsi AS prov ON (kab.provinsi_id = prov.id)
ORDER BY prov.id ASC;

INSERT INTO public.wilayah_kabupaten_kota (provinsi_id, predikat, kabupaten_kota)
VALUES
    (31, 'Kabupaten', 'Halmahera Barat'),
    (31, 'Kabupaten', 'Halmahera Tengah'),
    (31, 'Kabupaten', 'Halmahera Utara'),
    (31, 'Kabupaten', 'Halmahera Selatan'),
    (31, 'Kabupaten', 'Kepulauan Sula'),
    (31, 'Kabupaten', 'Halmahera Timur'),
    (31, 'Kabupaten', 'Pulau Morotai'),
    (31, 'Kabupaten', 'Pulau Taliabu'),
    (31, 'Kota', 'Ternate'),
    (31, 'Kota', 'Tidore Kepulauan');

INSERT INTO public.wilayah_kabupaten_kota (provinsi_id, predikat, kabupaten_kota)
VALUES
    (32, 'Kabupaten', 'Buru'),
    (32, 'Kabupaten', 'Buru Selatan'),
    (32, 'Kabupaten', 'Kepulauan Aru'),
    (32, 'Kabupaten', 'Maluku Barat Daya'),
    (32, 'Kabupaten', 'Maluku Tengah'),
    (32, 'Kabupaten', 'Maluku Tenggara'),
    (32, 'Kabupaten', 'Maluku Tenggara Barat'),
    (32, 'Kabupaten', 'Seram Bagian Barat'),
    (32, 'Kabupaten', 'Seram Bagian Timur'),
    (32, 'Kota', 'Ambon'),
    (32, 'Kota', 'Tual');

INSERT INTO public.wilayah_kabupaten_kota (provinsi_id, predikat, kabupaten_kota)
VALUES
    (33, 'Kabupaten', 'Fakfak'),
    (33, 'Kabupaten', 'Kaimana'),
    (33, 'Kabupaten', 'Manokwari'),
    (33, 'Kabupaten', 'Manokwari Selatan'),
    (33, 'Kabupaten', 'Maybrat'),
    (33, 'Kabupaten', 'Pegunungan Arfak'),
    (33, 'Kabupaten', 'Raja Ampat'),
    (33, 'Kabupaten', 'Sorong'),
    (33, 'Kabupaten', 'Sorong Selatan'),
    (33, 'Kabupaten', 'Tambrauw'),
    (33, 'Kabupaten', 'Teluk Bintuni'),
    (33, 'Kabupaten', 'Teluk Wondama');

INSERT INTO public.wilayah_kabupaten_kota (provinsi_id, predikat, kabupaten_kota)
VALUES
    (34, 'Kabupaten', 'Asmat'),
    (34, 'Kabupaten', 'Biak Numfor'),
    (34, 'Kabupaten', 'Boven Digoel'),
    (34, 'Kabupaten', 'Deiyai'),
    (34, 'Kabupaten', 'Dogiyai'),
    (34, 'Kabupaten', 'Intan Jaya'),
    (34, 'Kabupaten', 'Jayapura'),
    (34, 'Kabupaten', 'Jayawijaya'),
    (34, 'Kabupaten', 'Keerom'),
    (34, 'Kabupaten', 'Kepulauan Yapen'),
    (34, 'Kabupaten', 'Lanny Jaya'),
    (34, 'Kabupaten', 'Mamberamo Raya'),
    (34, 'Kabupaten', 'Mamberamo Tengah'),
    (34, 'Kabupaten', 'Mappi'),
    (34, 'Kabupaten', 'Merauke'),
    (34, 'Kabupaten', 'Mimika'),
    (34, 'Kabupaten', 'Nabire'),
    (34, 'Kabupaten', 'Nduga'),
    (34, 'Kabupaten', 'Paniai'),
    (34, 'Kabupaten', 'Pegunungan Bintang'),
    (34, 'Kabupaten', 'Puncak'),
    (34, 'Kabupaten', 'Puncak Jaya'),
    (34, 'Kabupaten', 'Sarmi'),
    (34, 'Kabupaten', 'Supiori'),
    (34, 'Kabupaten', 'Tolikara'),
    (34, 'Kabupaten', 'Waropen'),
    (34, 'Kabupaten', 'Yahukimo'),
    (34, 'Kabupaten', 'Yalimo'),
    (34, 'Kota', 'Jayapura');

SELECT kab.id AS "kabupaten_kota_id",
        kab.predikat AS "predikat",
        kab.kabupaten_kota AS "nama",
        prov.id AS "provinsi_id",
        prov.provinsi AS "nama_provinsi"
FROM public.wilayah_kabupaten_kota AS kab
JOIN public.wilayah_provinsi AS prov ON (kab.provinsi_id = prov.id)
ORDER BY prov.id ASC;

SELECT * FROM wilayah_kabupaten_kota AS kab WHERE kab.provinsi_id = 38;
