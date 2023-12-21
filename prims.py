INFINITY = 9999999
num_vertices = 3
graph = [
    [0, 5, 10],
    [4, 1, 8],
    [12, 0, 0]
]

edges = [(i, j, graph[i][j]) for i in range(num_vertices) for j in range(num_vertices) if graph[i][j] != 0]


edges.sort(key=lambda edge: edge[2])

visited_vertices = set()
print("Selected Edge: Weight\n")
edges_selected = 0

while edges_selected < num_vertices - 1 and edges:
    start, end, weight = edges.pop(0)

    if start not in visited_vertices or end not in visited_vertices:
        print(f"{start}-{end}:{weight}")
        visited_vertices.update([start, end])
        edges_selected += 1
        
    