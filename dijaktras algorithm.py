class WeightedGraph:
    INFINITY = 9999999999  

    def __init__(self, vertices_count):
        self.num_vertices = vertices_count
        self.adj_matrix = [[0 for _ in range(vertices_count)] for _ in range(vertices_count)]

    def display_shortest_distances(self, distances):
        print("Vertex \tDistance from Source")
        for node in range(self.num_vertices):
            print(node, "\t\t ", distances[node], "\n")

    def find_min_distance_vertex(self, distances, visited_set):
        min_distance = self.INFINITY
        min_vertex = -1

        for vertex in range(self.num_vertices):
            if distances[vertex] < min_distance and not visited_set[vertex]:
                min_distance = distances[vertex]
                min_vertex = vertex

        return min_vertex

    def dijkstra_algorithm(self, source_vertex):
        distances = [self.INFINITY] * self.num_vertices
        distances[source_vertex] = 0
        visited_set = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            current_vertex = self.find_min_distance_vertex(distances, visited_set)
            visited_set[current_vertex] = True

            for neighbor_vertex in range(self.num_vertices):
                if (
                    self.adj_matrix[current_vertex][neighbor_vertex] > 0
                    and not visited_set[neighbor_vertex]
                    and distances[neighbor_vertex] > distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]
                ):
                    distances[neighbor_vertex] = distances[current_vertex] + self.adj_matrix[current_vertex][neighbor_vertex]

        self.display_shortest_distances(distances) 


weighted_graph = WeightedGraph(5)
weighted_graph.adj_matrix = [
    [1, 9, 0, 8, 7],
    [0, 11, 15, 2, 0],
    [2, 0, 0, 0, 0],
    [0, 6, 0, 8, 0],
    [4, 0, 8, 0, 0],
    [0, 14, 0, 3, 0]
]

weighted_graph.dijkstra_algorithm(1)