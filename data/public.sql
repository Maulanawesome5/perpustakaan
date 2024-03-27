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
