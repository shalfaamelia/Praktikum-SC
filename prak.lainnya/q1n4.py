from collections import deque

# Representasi graf dari peta
graph = {
    'Siantar': ['Tebing', 'Pardagangan', 'Parapat', 'Raya'],
    'Tebing': ['Binjai', 'Medan', 'Siantar'],
    'Pardagangan': ['Siantar', 'Sipirok'],
    'Parapat': ['Siantar'],
    'Raya': ['Siantar', 'Sipirok'],
    'Binjai': ['Tebing'],
    'Medan': ['Tebing', 'Asahan'],
    'Sipirok': ['Pardagangan', 'Raya', 'Tanjung', 'Asahan'],
    'Asahan': ['Medan', 'Sipirok', 'Kisaran'],
    'Tanjung': ['Sipirok'],
    'Kisaran': ['Asahan']
}

# DLS Algoritma (Depth-Limited Search)
def dls(graph, start, goal, depth, path=None):
    if path is None:
        path = []

    path.append(start)
    
    if start == goal:
        return path
    
    if depth == 0:
        return None

    for neighbor in graph[start]:
        if neighbor not in path:
            result = dls(graph, neighbor, goal, depth - 1, path.copy())
            if result:
                return result

    return None

# Input pengguna untuk kota awal, tujuan, dan batas kedalaman
start_city = input("Masukkan kota awal untuk DLS: ")
goal_city = input("Masukkan kota tujuan untuk DLS: ")
depth_limit = int(input("Masukkan batas kedalaman: "))

result = dls(graph, start_city, goal_city, depth_limit)

if result:
    print("\nJalur ditemukan dengan DLS:", result)
else:
    print("\nJalur tidak ditemukan dalam batas kedalaman yang diberikan.")