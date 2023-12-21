class GraphProcessor:
    MAX_DISTANCE = 999999

    @staticmethod
    def floyd_warshall(graph):
        num_vertices = len(graph)
        distances = [list(row) for row in graph]

        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        GraphProcessor.print_solution(distances)

    @staticmethod
    def print_solution(distances):
        num_vertices = len(distances)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distances[i][j] == GraphProcessor.MAX_DISTANCE:
                    print("INF", end=" ")
                else:
                    print(distances[i][j], end=" ")
            print(" ")


weighted_graph = [
    [0, 0, 0, 0],
    [11, 0, 5, 15],
    [GraphProcessor.MAX_DISTANCE, 10, GraphProcessor.MAX_DISTANCE, GraphProcessor.MAX_DISTANCE],
    [0, 8, 6, 4]
]

print("The shortest distances between every pair of vertices ")
GraphProcessor.floyd_warshall(weighted_graph)  