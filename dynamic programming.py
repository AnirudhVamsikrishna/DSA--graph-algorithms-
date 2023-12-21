class WeightedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_directed_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def bellman_ford_shortest_paths(self, source):
        distances = [float('inf')] * self.num_vertices
        predecessors = [None] * self.num_vertices
        distances[source] = 0

        for _ in range(self.num_vertices - 1):
            for start, end, weight in self.edges:
                if distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight
                    predecessors[end] = start

        for start, end, weight in self.edges:
            if distances[start] + weight < distances[end]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors

 
graph = WeightedGraph(7)
graph.add_directed_edge(0, 0, 0)
graph.add_directed_edge(1, 5, 4)
graph.add_directed_edge(0, 3, 5)
graph.add_directed_edge(1, 0, 10)
graph.add_directed_edge(1, 4, -6)
graph.add_directed_edge(1, 5, 2)
graph.add_directed_edge(6, 0, 0)

source_node = 6
shortest_distances, predecessors = graph.bellman_ford_shortest_paths(source_node)

print("Shortest distances from source node", source_node)
for vertex in range(graph.num_vertices):
    print(f"Vertex {vertex}: Distance = {shortest_distances[vertex]}, Predecessor = {predecessors[vertex]}")