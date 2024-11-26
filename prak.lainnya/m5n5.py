# Menerima nput data dari pengguna
ipk = float(input("Masukkan IPK mahasiswa: "))
pendapatan_orang_tua = int(input("Masukkan pendapatan orang tua mahasiswa (dalam rupiah): "))
sanksi = input("Apakah mahasiswa pernah mendapatkan sanksi akademik? (ya/tidak): ").lower()

# Syarat-syarat mendapatkan beasiswa
ipk_minimal = 3.0
pendapatan_maksimal = 2000000
pernah_kena_sanksi = (sanksi == "ya")

# Menentukan kelayakan mendapatkan beasiswa
if ipk >= ipk_minimal and pendapatan_orang_tua <= pendapatan_maksimal and not pernah_kena_sanksi:
    print("Mahasiswa memenuhi syarat untuk menerima beasiswa")
else:
    print("Mahasiswa tidak memenuhi syarat untuk menerima beasiswa")