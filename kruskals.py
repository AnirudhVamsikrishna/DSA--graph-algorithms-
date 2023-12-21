class MinimumSpanningTreeFinder:
    def __init__(self, graph):
        self.edges = [(weight, node1, node2) for node1, neighbors in graph.items() for node2, weight in neighbors.items()]
        self.edges.sort()
        self.parent_nodes = {node: node for node in graph}

    def find_root_node(self, node):
        if self.parent_nodes[node] != node:
            self.parent_nodes[node] = self.find_root_node(self.parent_nodes[node])
        return self.parent_nodes[node]

    def union_root_nodes(self, root1, root2):
        self.parent_nodes[root1] = root2

    def kruskal_minimum_spanning_tree(self):
        minimum_spanning_tree = []
        for weight, node1, node2 in self.edges:
            root1, root2 = self.find_root_node(node1), self.find_root_node(node2)
            if root1 != root2:
                self.union_root_nodes(root1, root2)
                minimum_spanning_tree.append((weight, node1, node2))

        return minimum_spanning_tree


custom_graph = {
    'A': {'B': 4},
    'B': {'A': 2, 'C': 2, 'D': 0},
    'C': {'A': 1}, 
    'D': {'B': 4, 'C': 0}
}

tree_finder = MinimumSpanningTreeFinder(custom_graph)
result_tree = tree_finder.kruskal_minimum_spanning_tree()
print("Minimum Spanning Tree (Kruskal's Algorithm):", result_tree)
