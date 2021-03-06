from __future__ import print_function

from graph_list import Graph


def dfs(G, current_vert, visited, sequence):
    visited[current_vert] = True  # mark the visited node
    #print("traversal: " + currentVert.get_vertex_ID())
    sequence.append(current_vert.get_vertex_ID())
    for nbr in current_vert.get_connections():  # take a neighbouring node
        if nbr not in visited:  # condition to check whether the neighbour node is already visited
            dfs(G, nbr, visited, sequence)  # recursively traverse the neighbouring node


def DFSTraversal(G):
    sequence = []
    visited = {}  # Dictionary to mark the visited nodes
    for current_vert in G:  # G contains vertex objects
        # Start traversing from the root node only if its not visited
        if current_vert not in visited:
            # For a connected graph this is called only once
            dfs(G, current_vert, visited, sequence)
    print(sequence)
    length = len(sequence)
    for i in range(length, 0, -1):
        print(sequence[i - 1])

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
    #print(G.get_edges())

    DFSTraversal(G)

