import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf directed
G = nx.DiGraph()

# Menambahkan node dan edge sesuai dengan graf yang diberikan
edges = [
    ('S', 'A', 3),
    ('S', 'D', 2),
    ('A', 'B', 5),
    ('A', 'C', 10),  # Edge A ke C dengan bobot 10
    ('B', 'C', 2),
    ('B', 'D', 1),
    ('C', 'G', 4),   # Edge dari C ke G dengan bobot 4
    ('D', 'E', 4),
    ('E', 'G', 3),
]

# Menambahkan edges ke graf
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Menggambar graf
plt.figure(figsize=(8, 6))

# Posisi node
pos = {
    'S': (0, 0), 
    'A': (1, 1), 
    'B': (2, 1), 
    'C': (3, 0), 
    'D': (1, 0), 
    'E': (2, -1), 
    'G': (3, -1)
}

# Menggambar node dan edges
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_size=10, font_weight='bold', arrows=True)

# Menggambar bobot pada edges
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Menambahkan heuristic di bawah setiap node
heuristics = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0  # G seharusnya h=0
}

for node, (x, y) in pos.items():
    plt.text(x, y - 0.1, f"h={heuristics[node]}", fontsize=9, ha='center')

plt.title("Graf Node dan Edge dengan Heuristic")
plt.axis('off')  # Mematikan axis
plt.show()