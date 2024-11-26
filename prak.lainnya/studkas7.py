import heapq

# Initialize an empty dictionary to represent the road network graph.
jalur = {}

# Priority Queue class for implementing priority queues.
class PriorityQueue:
    def __init__(self) -> None:
        self.cities = []

    def isEmpty(self):
        return len(self.cities) == 0

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

# CityNode class to represent city nodes in the graph.
class CityNode:
    def __init__(self, city, distance) -> None:
        self.city = str(city)
        self.distance = int(distance)

# Function to read a text file containing graph information and build the graph in the jalur dictionary.
def makeDict():
    filejalan = r"jalan.txt"  # Ensure this path is correct
    try:
        with open(filejalan, 'r') as file:
            for line in file:
                delimeter = line.strip().split(',')
                city1 = delimeter[0].strip()
                city2 = delimeter[1].strip()
                dist = int(delimeter[2].strip())
                jalur.setdefault(city1, []).append(CityNode(city2, dist))
                jalur.setdefault(city2, []).append(CityNode(city1, dist))
    except FileNotFoundError:
        print(f"File {filejalan} tidak ditemukan. Pastikan path file sudah benar.")

# Function to read a text file containing heuristic values and build the heuristic dictionary.
def makeHeuristicDict():
    h = {}
    fileheuristicjalan = r"heuristicjalan.txt"  # Ensure this path is correct
    try:
        with open(fileheuristicjalan, 'r') as file:
            for line in file:
                delimeter = line.strip().split(',')
                node = delimeter[0].strip()
                sld = int(delimeter[1].strip())
                h[node] = sld
    except FileNotFoundError:
        print(f"File {fileheuristicjalan} tidak ditemukan. Pastikan path file sudah benar.")
    return h

# Heuristic function used in GBFS and A*.
def heuristic(node, values):
    return values.get(node, float('inf'))

# Greedy Best-First Search Algorithm.
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

    printOutput(start, end, path, expandList)

# Depth-First Search Algorithm.
def dfs(start, end, path, visited):
    visited.add(start)
    if start == end:
        return True

    for neighbor in jalur[start]:
        if neighbor.city not in visited:
            path[neighbor.city] = start
            if dfs(neighbor.city, end, path, visited):
                return True
            del path[neighbor.city]

    return False

# Function to initiate DFS.
def depthFirstSearch(start, end):
    path = {}
    visited = set()
    if dfs(start, end, path, visited):
        printOutput(start, end, path, visited)
    else:
        print(f"Path from {start} to {end} not found using DFS.")

# Breadth-First Search Algorithm.
def bfs(start, end):
    queue = [start]
    path = {start: None}
    visited = set()

    while queue:
        curr = queue.pop(0)
        visited.add(curr)

        if curr == end:
            break

        for neighbor in jalur[curr]:
            if neighbor.city not in visited and neighbor.city not in queue:
                queue.append(neighbor.city)
                path[neighbor.city] = curr

    printOutput(start, end, path, visited)

# Uniform Cost Search Algorithm.
def uniformCostSearch(start, end):
    pq = PriorityQueue()
    pq.push(start, 0)
    path = {start: None}
    cost = {start: 0}

    while not pq.isEmpty():
        curr = pq.pop()

        if curr == end:
            break

        for neighbor in jalur[curr]:
            new_cost = cost[curr] + neighbor.distance
            if neighbor.city not in cost or new_cost < cost[neighbor.city]:
                cost[neighbor.city] = new_cost
                pq.push(neighbor.city, new_cost)
                path[neighbor.city] = curr

    printOutput(start, end, path, cost)

# Function to print the output.
def printOutput(start, end, path, visited):
    finalpath = []
    i = end

    while i is not None:
        finalpath.append(i)
        i = path.get(i)
    finalpath.reverse()

    print("Path from {} to {}: {}".format(start, end, finalpath))
    print("Cities expanded:", visited)

# Main function to run the algorithm based on user input.
def main():
    makeDict()  # Read the road data
    algorithms = {
        '1': ('BFS', bfs),
        '2': ('DFS', depthFirstSearch),
        '3': ('UCS', uniformCostSearch),
        '4': ('GBFS', greedyBFS),
    }

    print("Choose an algorithm:")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")

    choice = input("Enter your choice (1-4): ")
    if choice in algorithms:
        src = input("Enter starting city: ")
        dst = input("Enter destination city: ")
        algorithms[choice][1](src, dst)
    else:
        print("Invalid choice.")

# Check if the script is executed as the main program.
if __name__ == "__main__":
    main()