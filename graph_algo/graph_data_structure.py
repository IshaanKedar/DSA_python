num_nodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(3,4),(3,2)]

#adjacency list

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes
        self.data = [[] for x in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n,neighbors in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()

graph1 = Graph(num_nodes,edges)

print(graph1)

