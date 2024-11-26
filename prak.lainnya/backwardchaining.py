class BackwardChainingExpertSystem:
    def __init__(self):
        # Basis pengetahuan: aturan yang menghubungkan kandungan gizi dengan gejala
        self.rules = {
            "P1: Karbohidrat": ["A1", "A2"],
            "P2: Protein": ["A5", "A6"],
            "P3: Vitamin": ["A3", "A4", "A9", "A10"],
            "P4: Zat Besi": ["A7", "A8"],
            "P5: Asam Folat": ["A11", "A12"]
        }
        self.known_facts = []  # Fakta yang diketahui (gejala yang dialami)

    def add_fact(self, fact):
        # Menambahkan fakta (gejala) ke daftar fakta yang diketahui
        self.known_facts.append(fact)

    def backward_chain(self, goal):
        # Melakukan backward chaining untuk menentukan apakah sebuah goal dapat dicapai berdasarkan fakta yang diketahui.
        if goal in self.rules:
            required_conditions = self.rules[goal]
            return all(condition in self.known_facts for condition in required_conditions)
        return False

    def diagnose(self):
        # Mengembalikan kandungan gizi yang relevan berdasarkan gejala.a1
        results = []
        for nutrient, conditions in self.rules.items():
            if self.backward_chain(nutrient):
                results.append(nutrient)
        return results


# Contoh penggunaan sistem pakar
if __name__ == "__main__":
    system = BackwardChainingExpertSystem()
    
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

    # Masukkan gejala berdasarkan input pengguna
    print("\nMasukkan gejala yang dialami (contoh: A1, A2):")
    gejala_input = input().split(", ")
    
    # Tambahkan fakta ke sistem
    for g in gejala_input:
        system.add_fact(g.strip())
    
    # Diagnosa berdasarkan backward chaining
    print("\nRekomendasi Kandungan Gizi yang Dibutuhkan:")
    recommendations = system.diagnose()
    if recommendations:
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("Tidak ada rekomendasi kandungan gizi berdasarkan gejala yang diberikan.")