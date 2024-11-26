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

# BFS Algoritma
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_path = []

    while queue:
        city = queue.popleft()
        if city not in visited:
            visited.add(city)
            bfs_path.append(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_path

# DFS Algoritma
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_path = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_path.extend(dfs(graph, neighbor, visited))
    
    return dfs_path

# Input pengguna untuk kota awal
start_city = input("Masukkan kota awal untuk BFS dan DFS: ")
print("\nJalur BFS:", bfs(graph, start_city))
print("Jalur DFS:", dfs(graph, start_city))