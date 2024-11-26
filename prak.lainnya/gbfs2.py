import heapq

# Inisialisasi dictionary kosong untuk merepresentasikan graf jaringan jalan di Romania.
jalur = {}

# Definisi kelas PriorityQueue untuk implementasi antrian prioritas.
class PriorityQueue:
    def __init__(self) -> None:  # Perbaikan pada penggunaan __init__
        self.cities = []  # Inisialisasi daftar kosong untuk menyimpan elemen antrian prioritas.

    def isEmpty(self):
        return len(self.cities) == 0

    def check(self):
        print(self.cities)

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))  # Menambahkan elemen ke antrian prioritas berdasarkan biaya.

    def pop(self):
        return heapq.heappop(self.cities)[1]  # Menghapus dan mengembalikan elemen dengan biaya terendah.

# Definisi kelas CityNode untuk merepresentasikan node kota dalam graf.
class CityNode:
    def __init__(self, city, distance) -> None:  # Perbaikan pada penggunaan __init__
        self.city = str(city)
        self.distance = int(distance)  # Pastikan jarak adalah integer untuk kalkulasi jarak

# Fungsi untuk membaca file teks yang berisi informasi graf dan membangun graf di dalam dictionary "jalur".
def makeDict():
    filejalan = r"C:\xampp\htdocs\Praktikum SC\jalan.txt"  # Pastikan path ini benar
    try:
        with open(filejalan, 'r') as file:
            for line in file:
                delimeter = line.strip().split(',')
                city1 = delimeter[0].strip()
                city2 = delimeter[1].strip()
                dist = int(delimeter[2].strip())  # Pastikan jarak dikonversi menjadi integer
                jalur.setdefault(city1, []).append(CityNode(city2, dist))
                jalur.setdefault(city2, []).append(CityNode(city1, dist))
    except FileNotFoundError:
        print(f"File {filejalan} tidak ditemukan. Pastikan path file sudah benar.")

# Fungsi untuk membaca file teks yang berisi nilai heuristik dan membangun dictionary nilai heuristik "h".
def makeHeuristicDict():
    h = {}
    fileheuristicjalan = r"C:\xampp\htdocs\Praktikum SC\heuristicjalan.txt"  # Pastikan path ini benar
    try:
        with open(fileheuristicjalan, 'r') as file:
            for line in file:
                delimeter = line.strip().split(',')
                node = delimeter[0].strip()
                sld = int(delimeter[1].strip())  # Jalan lurus harus dalam bentuk integer
                h[node] = sld
    except FileNotFoundError:
        print(f"File {fileheuristicjalan} tidak ditemukan. Pastikan path file sudah benar.")
    return h

# Fungsi heuristik yang digunakan dalam pencarian GBFS.
def heuristic(node, values):
    return values.get(node, float('inf'))  # Jika node tidak ditemukan dalam nilai heuristik, beri nilai infinity

# Fungsi utama yang menjalankan algoritma GBFS.
def greedyBFS(start, end):
    path = {}
    q = PriorityQueue()
    h = makeHeuristicDict()

    q.push(start, 0)
    path[start] = None
    expandList = []

    while not q.isEmpty():
        curr = q.pop()
        expandList.append(curr)

        if curr == end:
            break
        
        for new in jalur[curr]:
            if new.city not in path:  
                f_cost = heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = curr

    # Fungsi untuk mencetak output hasil pencarian.
    printOutput(start, end, path, expandList)

# Fungsi untuk mencetak output hasil pencarian.
def printOutput(start, end, path, expandList):
    finalpath = []
    i = end

    while path.get(i) is not None:
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("Program Greedy Best-First-Search")
    print(f"{start} => {end}")
    print("Kota yang dilewati dengan jarak terpendek:\t" + str(finalpath))

# Fungsi utama yang dijalankan saat skrip ini dieksekusi.
def main():
    src = "Arad"
    dst = "Bucharest"
    makeDict()          
    greedyBFS(src, dst) 

# Pengecekan apakah skrip ini dijalankan sebagai program utama.
if __name__ == "__main__":
    main()