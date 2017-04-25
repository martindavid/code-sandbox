from __future__ import print_function
from vertex import Vertex


class Graph:
    def __init__(self, num_vertices, is_directed=False, cost=0):
        self.adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.is_directed = is_directed
        self.vertices = []
        for i in range(0, num_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)

    def set_vertex(self, vtx, id):
        if 0 <= vtx < self.num_vertices:
            self.vertices[vtx].set_vertex_ID(id)

    def get_vertex(self, n):
        for vertexin in range(0, self.num_vertices):
            if n == self.vertices[vertexin].get_vertex_ID():
                return vertexin

        return -1

    def add_edge(self, frm, to, cost=0):
        if self.get_vertex(frm) != -1 and self.get_vertex(to) != -1:
            self.adj_matrix[self.get_vertex(frm)][self.get_vertex(to)] = cost
            if not self.is_directed: # if not directed both size needs to be updated
                self.adj_matrix[self.get_vertex(to)][self.get_vertex(frm)] = cost

    def get_vertices(self):
        vertices = []
        for vertxin in range(0, self.num_vertices):
            vertices.append(self.vertices[vertxin].get_vertex_ID())
        return vertices

    def print_matrix(self):
        for u in range(0, self.num_vertices):
            row = []
            for v in range(0, self.num_vertices):
                row.append(self.adj_matrix[u][v])
            print(row)

    def get_edges(self):
        edges = []
        for v in range(0, self.num_vertices):
            for u in range(0, self.num_vertices):
                if self.adj_matrix[u][v] != -1:
                    vid = self.vertices[v].get_vertex_ID()
                    wid = self.vertices[u].get_vertex_ID()
                    edges.append((vid, wid, self.adj_matrix[u][v]))
        return edges
