import string


class Node:
    def __init__(self,value,index=None):
        self.value = value
        self.index = index

    def __repr__(self):
        return f"{self.value}"

class Graph:
    @classmethod
    def create_graph_by_list(cls, nodes):
        return Graph( row=len(nodes), col=len(nodes), nodes=nodes)

    def __init__(self, row, col,nodes=None):
        self.alph = string.ascii_uppercase[:row]
        self.data = [[0]* col for _ in range((row))]
        self.nodes = nodes
        for i in range(len(nodes)):
            self.nodes[i].index = i

    def __connect(self,node1,node2,weight=1):
        node1 = self.isinstance(node1)
        node2 = self.isinstance(node2)
        self.data[node1][node2] = weight

    def connect(self,node1,node2,weight=1):
        self.__connect(node1,node2,weight)
        self.__connect(node2,node1,weight)


    def connections_from(self,node):
        node = self.isinstance(node)
        return [(self.nodes[col],self.data[node][col]) for col in range(len(self.data[node])) if self.data[node][col] != 0]

    def show(self):
        print( "  ["," ".join(self.alph)+"]")

        self.alph_iter = iter(self.alph)
        for row in self.data:

            print(next(self.alph_iter),row)

    def isinstance(self,node):
        if not isinstance(node,Node) and not isinstance(node,int):
            raise ValueError('bad value')
        elif isinstance(node,int):
            return node
        else:
            return node.index

    def dijkstra(self,node):
        nodenum = self.isinstance(node)
        dist = [None]*len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([self.nodes[nodenum]])

        dist[nodenum][0] = 0
        queue = [i for i in range(len(self.nodes))]
        seen = set()
        while len(queue)>0:
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            queue.remove(min_node)
            seen.add(min_node)
            connections = self.connections_from(min_node)
            for (node,weight) in connections:
                tot_dist  = weight + min_dist
                if tot_dist< dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

w_graph = Graph.create_graph_by_list([a, b, c, d, e, f])

w_graph.connect(a, b, 5)
w_graph.connect(a, c, 10)
w_graph.connect(a, e, 2)
w_graph.connect(b, c, 2)
w_graph.connect(b, d, 4)
w_graph.connect(c, d, 7)
w_graph.connect(c, f, 10)
w_graph.connect(d, e, 3)

w_graph.show()

print(w_graph.dijkstra(a))
