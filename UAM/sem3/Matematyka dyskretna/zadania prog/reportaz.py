class Graph(object):

    # inicjalizacja matrixa
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # dodanie krawedzi
    def add_edge(self, v1, v2):
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1

    # usuniecie krawedzi
    def remove_edge(self, v1, v2):
        if not self.adjMatrix[v1][v2] == 0:
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def connumb(self, v1):
        return sum(self.adjMatrix[v1])
        
    def isconnected(self, v1, v2):
        if self.adjMatrix[v1][v2] == 1:
            return True
            
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print 
            
    def DFS(self, start, visited):
         
        # Print current node
        print(start, end = ' ')
        #wyj+= start + " "
        # Set current node as visited
        visited[start] = True
 
        # For every node of the graph
        for i in range(self.v):
             
            # If some node is adjacent to the
            # current node and it has not
            # already been visited
            if (Graph.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)   
                
wejscie = input() #wprowadzenie ilosci lini i maksymalnego polaczenia
wejscie = wejscie.split() #rozdzielenie ich po spacji
m=int(wejscie[1]) #przypisanie liczby drog
n=int(wejscie[0]) #przypisanie liczby miast

wyj = []   
g = Graph(n)


for x in range(m): #iterowanie do liczby drog
    kom = input()
    kom = kom.split()
    len_kom = len(kom)
    for x in range(len_kom):
        kom[x] = int(kom[x])
     
    g.add_edge(kom[0],kom[1])
    
visited = [False] * n


#print(*wyj, sep = "\n")
g.DFS(0,visited)