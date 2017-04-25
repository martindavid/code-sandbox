import sys

class Vertex:

    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
        # In degree count
        self.in_degree = 0
        # Out degree count
        self.out_degree = 0

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def set_in_degree(self, in_degree):
        self.in_degree = in_degree
    
    def get_in_degree(self):
        return self.in_degree

    def get_vertex_ID(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
