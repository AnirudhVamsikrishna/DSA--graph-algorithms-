class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def breadth_first_search(self, start_node):
        visited_nodes = {node: False for node in self.graph}
        queue = []
        visited_nodes[start_node] = True
        queue.append(start_node)

        result = []

        while queue:
            current_node = queue.pop(0)
            result.append(current_node) 

            for neighbor in self.graph[current_node]:
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    queue.append(neighbor)

        return result

graph = Graph({
    'A': ['C', 'D'],
    'B': ['C', 'A'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['A'],
}) 

starting_node = 'D'
result_sequence = graph.breadth_first_search(starting_node)

print(f"BFS starting from node '{starting_node}':", result_sequence)
