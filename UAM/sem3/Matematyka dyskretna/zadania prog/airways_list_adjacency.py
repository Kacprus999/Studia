#dodanie krawedzi w grafie
def addEdge(adj, u, v):
    if not u in adj[v]:
        adj[u].append(v)
        adj[v].append(u)
#usuniecie krawedzi
def delEdge(adj, u, v):
	# usuniecie z pierwszej listy drugiego elementu
    for i in range(len(adj[u])):	
        if (adj[u][i] == v):	
            adj[u].pop(i)
            break;
        # usuniecie z drugiej listy pierwszego elementu
    for i in range(len(adj[v])):
        if (adj[v][i] == u):		
            adj[v].pop(i)
            break;
def isconnected(adj, u, v):
    for i in range(len(adj[u])):
        if(adj[u][i] == v):
            return True;
            break;
    return False;
    
"""       
visited = set() # Set to keep track of visited nodes.

def dfs(visited, adj, node):
    if node not in visited:
        visited.add(node)
        for x in adj[node]:
            dfs(visited, adj, x)
"""           
def connumb(adj, u):
    numb = []
    for i in adj[u]:
        numb.append(i)      
    return numb

wejscie = input() #wprowadzenie ilosci lini i maksymalnego polaczenia
wejscie = wejscie.split() #rozdzielenie ich po spacji
m=int(wejscie[1]) #przypisanie wartosci maksymalnej liczby komend
n=int(wejscie[0]) #przypisanie maksymalnej wartosci

if m < 1000000 and n < 1000:
    pol = [[] for i in range(n)] # lista połączen
    wyj = []
    V = n;
    for x in range(m): #iterowanie do liczby komend
        kom = input()
        kom = kom.split()
        len_kom = len(kom)
        for x in range(len_kom):
            kom[x] = int(kom[x])
        if kom[1] < n:
            if len_kom == 2 and kom[0] == 4: #liczba polaczen z kom[1]
                #dfs(visited,pol,kom[1])
                #wyj.append(len(visited))
                wyj.append(len(connumb(pol,kom[1])))
            elif len_kom == 3:
                if kom[2]<n:
                    #test1 = str(kom[1])+str(kom[2])
                    #test2 = str(kom[2])+str(kom[1])
                    if kom[0] == 1: # dodanie polaczenia z kom[1] do kom[2] i na odwrót 
                        #sprawdz = next(i for i in pol if i == test) 
                        addEdge(pol,kom[1],kom[2])
                    elif kom[0] == 2: # usuniecie polaczeniz z kom[1] do kom[2] i na odwrót
                        delEdge(pol, kom[1], kom[2])
                    elif kom[0] == 3: # pytanie tak/nie czy istnieje polaczenie z kom[1] do kom[2]
                        if isconnected(pol, kom[1],kom[2]) == True:
                            wyj.append("TAK")
                        else:
                            wyj.append("NIE")
                else:
                    continue
            else:
                continue
        else:
            continue
    print(*wyj, sep = "\n")