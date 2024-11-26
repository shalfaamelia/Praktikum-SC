class NutrientExpertSystem:
    def __init__(self):
        # Basis pengetahuan: aturan yang menghubungkan gejala dengan kandungan gizi
        self.rules = [
            {"conditions": ["A1", "A2"], "conclusion": "P1: Karbohidrat"},
            {"conditions": ["A3", "A4"], "conclusion": "P3: Vitamin"},
            {"conditions": ["A5", "A6"], "conclusion": "P2: Protein"},
            {"conditions": ["A7", "A8"], "conclusion": "P4: Zat Besi"},
            {"conditions": ["A9", "A10"], "conclusion": "P3: Vitamin"},
            {"conditions": ["A11", "A12"], "conclusion": "P5: Asam Folat"}
        ]
        self.facts = []  # Fakta awal (gejala yang dialami)
        self.inferences = []  # Kesimpulan yang dihasilkan

    def add_fact(self, fact):
        """Menambahkan fakta ke sistem."""
        self.facts.append(fact)
        self.apply_rules()

    def apply_rules(self):
        """Melakukan forward chaining untuk menemukan kesimpulan."""
        for rule in self.rules:
            if all(condition in self.facts for condition in rule["conditions"]):
                conclusion = rule["conclusion"]
                if conclusion not in self.inferences:
                    self.inferences.append(conclusion)

    def get_inferences(self):
        """Mengembalikan daftar kesimpulan."""
        return self.inferences


# Contoh penggunaan sistem pakar
if __name__ == "__main__":
    system = NutrientExpertSystem()
    
    print("Data Gejala Kekurangan Gizi:")
    gejala_list = [
        "A1: Badan mudah lesu, letih, dan cepat capek",
        "A2: Tidak bersemangat",
        "A3: Mudah tersinggung",
        "A4: Stres dan selalu sakit kepala",
        "A5: Suka mengantuk",
        "A6: Berat badan tidak normal",
        "A7: Nafsu makan tidak baik",
        "A8: Buang air besar tidak lancer dan sering terjadi sembelit",
        "A9: Bibir kering dan pecah-pecah",
        "A10: Gusi sering mengalami pendarahan",
        "A11: Adanya kantung mata hitam/gelap",
        "A12: Kaki Bengkak"
    ]
    for gejala in gejala_list:
        print(f"- {gejala}")

    # Masukkan fakta berdasarkan gejala
    print("\nMasukkan gejala yang dialami (contoh: A1, A2):")
    gejala_input = input().split(", ")
    
    # Tambahkan fakta ke sistem
    for g in gejala_input:
        system.add_fact(g.strip())
    
    # Tampilkan kesimpulan
    print("\nRekomendasi Kandungan Gizi yang Dibutuhkan:")
    for inference in system.get_inferences():
        print(f"- {inference}")