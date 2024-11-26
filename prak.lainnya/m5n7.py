# Daftar penyakit
penyakit = ["flu", "demam berdarah", "malaria"]

# Daftar gejala
gejala = ["demam", "batuk", "pilek", "sakit kepala", "nyeri otot"]

# Hubungan antara penyakit dan gejala
hubungan = {
    "flu": ["demam", "batuk", "pilek"],
    "demam berdarah": ["demam tinggi", "bintik merah pada kulit"],
    "malaria": ["demam", "menggigil", "sakit kepala", "nyeri otot"]
}

# Meminta input gejala pasien
print("Pilih gejala yang dialami pasien dari daftar berikut:")
print(gejala)

# Menginput gejala pasien
gejala_pasien = []
while True:
    gejala_input = input("Masukkan gejala (ketik 'selesai' untuk berhenti): ").lower()
    if gejala_input == 'selesai':
        break
    elif gejala_input in gejala:
        gejala_pasien.append(gejala_input)
    else:
        print("Gejala tidak ada dalam daftar, silakan masukkan gejala yang valid")

# Mencari penyakit yang cocok dengan gejala pasien
penyakit_ditemukan = False
for p in penyakit:
    if set(gejala_pasien).issubset(hubungan.get(p, [])):
        print("Pasien menderita", p)
        penyakit_ditemukan = True
        break

# Jika tidak ada penyakit yang cocok
if not penyakit_ditemukan:
    print("Pasien tidak menderita penyakit flu, demam berdarah, atau malaria")