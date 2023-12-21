class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def dfs_recursive(self, current_node, visited=None):
        if visited is None:
            visited = set()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
            for neighbour in self.graph.get(current_node, []):
                self.dfs_recursive(neighbour, visited)

    def depth_first_search(self, start_node):
        print("The Depth-First Search:")
        self.dfs_recursive(start_node)
        print()   


custom_graph = {
    'a': ['b', 'd', 'c', 'e'],
    'b': ['f'],
    'c': ['e', 'b', 'd'],
    'd': ['b', 'a', 'f'],
    'e': [],
    'f': ['a', 'b']
}

graph_instance = Graph(custom_graph)
graph_instance.depth_first_search('c')
