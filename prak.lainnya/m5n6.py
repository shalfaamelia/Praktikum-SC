# Menerima input dari pengguna
harga_produk = float(input("Masukkan harga produk (USD): "))
kategori_produk = input("Masukkan kategori produk: ").lower()
diskon = float(input("Masukkan persentase diskon (%): "))

# Logika proposisi untuk mengevaluasi penawaran
tawaran_diterima = (harga_produk > 100) or ((kategori_produk == "elektronik" and diskon > 10) or (kategori_produk == "pakaian" and diskon > 20))

# Menampilkan hasil evaluasi
if tawaran_diterima:
    print("Tawaran diterima")
else:
    print("Tawaran ditolak")