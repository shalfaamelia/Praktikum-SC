def aStarAlgo(start_node, stop_node):
    # Inisialisasi open_set dan closed_set
    open_set = set([start_node])
    closed_set = set()

    # Inisialisasi g dan parents
    g = {}  # Menyimpan jarak dari node awal
    parents = {}  # Menyimpan map adjacency dari semua node

    # Jarak dari node awal ke dirinya sendiri adalah 0
    g[start_node] = 0
    # Node awal tidak memiliki parent, jadi set dirinya sebagai parent
    parents[start_node] = start_node

    # Loop selama masih ada node dalam open_set
    while len(open_set) > 0:
        n = None

        # Temukan node dengan f(n) = g(n) + h(n) terkecil
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        # Jika node n adalah stop_node, maka kita mulai membangun kembali path
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print(f'Path found: {path}')
            return path

        # Untuk setiap tetangga dari n, tambahkan ke open_set jika belum ada
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # Jika sudah ada, periksa apakah rute yang lebih pendek ditemukan
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # Pindahkan n dari open_set ke closed_set
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Fungsi untuk mendapatkan tetangga dan jaraknya dari node v
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Fungsi heuristik yang mengembalikan jarak estimasi ke goal
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

# Graf yang menggambarkan jaringan node dan jaraknya
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Eksekusi algoritma A* dari node A ke node G
aStarAlgo('A', 'G')