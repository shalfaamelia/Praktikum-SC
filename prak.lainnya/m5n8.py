# Data tempat wisata dan aktivitas
wisata = {
    "Bali": ["wisata budaya", "bermain air", "pedesaan"],
    "Lombok": ["mendaki gunung", "wisata alam", "bermain air"],
    "Yogyakarta": ["wisata budaya", "wisata sejarah", "kuliner"],
    "Malang": ["wisata gunung", "kuliner", "wisata anak"]
}

# Meminta input aktivitas dari pengguna
print("Aktivitas wisata yang tersedia: ")
aktivitas_tersedia = set(aktivitas for aktivitas_list in wisata.values() for aktivitas in aktivitas_list)
print(", ".join(aktivitas_tersedia))

# Input preferensi aktivitas pengguna
preferensi_pengguna = []
while True:
    aktivitas_input = input("Masukkan aktivitas wisata yang diinginkan (ketik 'selesai' untuk berhenti): ").lower()
    if aktivitas_input == "selesai":
        break
    elif aktivitas_input in aktivitas_tersedia:
        preferensi_pengguna.append(aktivitas_input)
    else:
        print("Aktivitas tidak tersedia, silakan coba lagi.")

# Menyaring tempat wisata berdasarkan aktivitas yang diinginkan pengguna
tempat_ditemukan = False
print("\nBerdasarkan preferensi Anda, tempat wisata yang direkomendasikan:")
for kota, aktivitas in wisata.items():
    if set(preferensi_pengguna).issubset(aktivitas):
        print(f"- {kota} (aktivitas: {', '.join(aktivitas)})")
        tempat_ditemukan = True

# Jika tidak ada tempat yang cocok
if not tempat_ditemukan:
    print("Tidak ada tempat wisata yang cocok dengan preferensi Anda.")