class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.graphDictionary = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graphDictionary.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.graphDictionary, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.graphDictionary:
            self.graphDictionary[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graphDictionary:
            self.graphDictionary[vertex1].append(vertex2)
        else:
            self.graphDictionary[vertex1] = [vertex2]

    def generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.graphDictionary:
            for neighbour in self.graphDictionary[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graphDictionary:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res
