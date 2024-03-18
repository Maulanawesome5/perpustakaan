-- Active: 1690520036101@@127.0.0.1@5432@toko_buku@public#produk_buku
SELECT * FROM produk_buku; -- Seleksi semua kolom pada tabel buku

SELECT judul_buku, tahun, isbn, deskripsi, harga, stok_barang
FROM public.produk_buku
ORDER BY judul_buku ASC; -- Seleksi beberapa kolom saja

-- Seleksi dengan alias
SELECT judul_buku AS "Judul",
        harga AS "Harga",
        stok_barang AS "Stok",
        (harga * stok_barang) AS "Total Pasokan"
FROM public.produk_buku;

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