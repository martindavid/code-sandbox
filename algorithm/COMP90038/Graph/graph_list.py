from vertex_list import Vertex

class Graph:
    def __init__(self, is_directed=False):
        self.vertice_dict = {}
        self.num_vertices = 0
        self.is_directed = is_directed

    def __iter__(self):
        return iter(self.vertice_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertice_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertice_dict:
            return self.vertice_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertice_dict:
            self.add_vertex(frm)
        if to not in self.vertice_dict:
            self.add_vertex(to)
        self.vertice_dict[frm].add_neighbor(self.vertice_dict[to], cost)
        if not self.is_directed: # if not directed, set cost for both edges
            self.vertice_dict[to].add_neighbor(self.vertice_dict[frm], cost)

        # add in degree for directed graph
        if self.is_directed:
            self.vertice_dict[to].in_degree += 1

    def get_vertices(self):
        return self.vertice_dict.keys()

    def get_edges(self):
        edges = []
        for node in self.vertice_dict:
            current_vert = self.vertice_dict[node]
            for neighbor in current_vert.get_connections():
                current_vert_ID = current_vert.get_vertex_ID()
                neighbor_ID = neighbor.get_vertex_ID()
                edges.append((current_vert_ID, neighbor_ID, current_vert.get_weight(neighbor)))
        return edges