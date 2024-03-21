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

-- Menghitung total stok buku beserta harganya
-- Hasilnya sekitar Rp. 304.518.830 (tiga ratus juta) total harga buku yang dimiliki toko
SELECT count(book.judul_buku) AS "Total Judul Buku",
        sum(book.stok_barang) AS "Total Stok Buku",
        sum((book.harga * book.stok_barang)) AS "Total Harga Pasokan"
FROM public.produk_buku AS book;
