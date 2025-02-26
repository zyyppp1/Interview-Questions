# Graph: Add Vertex
# Implement the add_vertex method.

# The method should perform the following tasks:

# Accept a parameter vertex that represents the vertex to be added to the graph.

# Check if the vertex is not already present in the adjacency list adj_list (an attribute of the Graph class):

# If the vertex is not present, add it as a key to the adj_list dictionary with an empty list as its value.

# Return True to indicate that the vertex was successfully added to the graph.

# If the vertex is already present in the adj_list, return False to indicate that the operation was unsuccessful.

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
            return True
        return False



my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""