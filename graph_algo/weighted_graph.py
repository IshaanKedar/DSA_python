class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)] if weighted else None

        for edge in edges:
            if weighted:
                node1, node2, w = edge
                self.data[node1].append(node2)
                self.weight[node1].append(w)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(w)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i in range(self.num_nodes):
                connections = zip(self.data[i], self.weight[i])
                result += f"{i}: {list(connections)}\n"
        else:
            for i in range(self.num_nodes):
                result += f"{i}: {self.data[i]}\n"
        return result

    def __str__(self):
        return self.__repr__()


# ============================
# EXAMPLES
# ============================

print("==> Example 1: Undirected Unweighted Graph")
num_nodes1 = 5
edges1 = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4), (3, 2)]
graph1 = Graph(num_nodes1, edges1)
print(graph1)

print("\n==> Example 2: Directed Unweighted Graph")
edges2 = [(0, 1), (0, 2), (1, 3), (3, 4)]
graph2 = Graph(5, edges2, directed=True)
print(graph2)

print("\n==> Example 3: Undirected Weighted Graph")
edges3 = [(0, 1, 3), (1, 2, 5), (2, 3, 2), (3, 4, 4)]
graph3 = Graph(5, edges3, weighted=True)
print(graph3)

print("\n==> Example 4: Directed Weighted Graph")
edges4 = [(0, 1, 3), (0, 3, 2), (1, 2, 1), (2, 4, 7)]
graph4 = Graph(5, edges4, directed=True, weighted=True)
print(graph4)
