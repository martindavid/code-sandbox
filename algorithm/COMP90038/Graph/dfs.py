from __future__ import print_function
from graph_list import Graph

def dfs(G, currentVert, visited):
    visited[currentVert] = True  # mark the visited node
    print("traversal: " + currentVert.get_vertex_ID())
    for nbr in currentVert.get_connections():  # take a neighbouring node
        if nbr not in visited:  # condition to check whether the neighbour node is already visited
            dfs(G, nbr, visited)  # recursively traverse the neighbouring node


def DFSTraversal(G):
    visited = {}  # Dictionary to mark the visited nodes
    for currentVert in G:  # G contains vertex objects
        if currentVert not in visited:  # Start traversing from the root node only if its not visited
            # For a connected graph this is called only once
            dfs(G, currentVert, visited)


if __name__ == '__main__':

    G = Graph()
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_vertex('f')
    G.add_edge('a', 'b', 1)
    G.add_edge('a', 'c', 1)
    G.add_edge('b', 'd', 1)
    G.add_edge('b', 'e', 1)
    G.add_edge('c', 'd', 1)
    G.add_edge('c', 'e', 1)
    G.add_edge('d', 'e', 1)
    G.add_edge('e', 'a', 1)
    print('Graph data:')
    print(G.get_edges())

    DFSTraversal(G)
