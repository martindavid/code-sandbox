class Vertex:
    def __init__(self, node):
        self.id = node
        # Mark all nodes unvisited
        self.visited = False

    def add_neighbor(self, neighbor, G):
        G.add_edge(self.id, neighbor)

    def get_connections(self, G):
        return G.adjMatrix(self.id)

    def get_vertex_ID(self):
        return self.id

    def set_vertex_ID(self, id):
        self.id = id

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)
