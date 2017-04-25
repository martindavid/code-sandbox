from __future__ import print_function

from Graph.graph_list import Graph

if __name__ == '__main__':
    # g = { "a" : ["b", "c"],
    #       "b" : ["d", "e"],
    #       "c" : ["d", "e"],
    #       "d" : ["e"],
    #       "e" : ["a"],
    #       "f" : []
    #     }
    # graph = Graph(g)

    # print("Vertices of graph:")
    # print(graph.vertices())

    # print("Edges of graph:")
    # print(graph.edges())

    G = Graph()
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_edge('a', 'b', 4)
    G.add_edge('a', 'c', 1)
    G.add_edge('c', 'b', 2)
    G.add_edge('b', 'e', 4)
    G.add_edge('c', 'd', 4)
    G.add_edge('d', 'e', 4)
    print('Graph Data')
    print(G.get_edges())
