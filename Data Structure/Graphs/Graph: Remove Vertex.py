# Graph: Remove Vertex
# The remove_vertex method takes a vertex as input and removes it from the graph, along with all edges connected to it.

# The method returns True if the vertex was successfully removed and False if the vertex was not present in the graph.

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,v1):
        if v1 in self.adj_list.keys():
            for i in self.adj_list[v1]:
                self.adj_list[i].remove(v1)
            del self.adj_list[v1]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')


print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')


print('\nGraph after remove_vertex():')
my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""