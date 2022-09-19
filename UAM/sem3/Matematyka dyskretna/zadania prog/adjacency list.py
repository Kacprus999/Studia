# Python3 implementation of the above approach

# A utility function to add an edge in an
# undirected graph.
def addEdge(adj, u, v):
    if not u in adj[v]:
        adj[u].append(v);
        adj[v].append(u);
	
# A utility function to delete an edge in an
# undirected graph.
def delEdge(adj, u, v):
	
	# Traversing through the first vector list
	# and removing the second element from it
    if u in adj[v]:
        for i in range(len(adj[u])):
        
            if (adj[u][i] == v):
                
                adj[u].pop(i);
                break;
        
        # Traversing through the second vector list
        # and removing the first element from it
        for i in range(len(adj[v])):
        
            if (adj[v][i] == u):
                
                adj[v].pop(i);
                break;
        
# A utility function to pr the adjacency list
# representation of graph
def prGraph(adj, V):
	
	for v in range(V):
		
		print("vertex " + str(v), end = ' ')
		
		for x in adj[v]:
			print("-> " + str(x), end = '')
			
		print()
	print()
	
# Driver code
if __name__=='__main__':

        V = 5;
        adj = [[] for i in range(V)]

        # Adding edge as shown in the example figure
        addEdge(adj, 0, 1);
        addEdge(adj, 0, 4);
        addEdge(adj, 1, 2);
        addEdge(adj, 3, 4);
        addEdge(adj, 1, 3);
        addEdge(adj, 1, 4);
        addEdge(adj, 2, 3);
        addEdge(adj, 3, 4);

        # Pring adjacency matrix
        prGraph(adj, V);

        # Deleting edge (1, 4)
        # as shown in the example figure
        delEdge(adj, 1, 4);
        delEdge(adj, 0,3);

        # Pring adjacency matrix
        prGraph(adj, V);

    # This code is contributed by rutvik_56
