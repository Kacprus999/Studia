#dodanie krawedzi w grafie
def addEdge(adj, u, v):
        adj[u].append(v)
        adj[v].append(u) 
def connumb(adj, u):
    numb = []
    for i in adj[u]:
        numb.append(i)      
    return numb
def arraytostring(array):
    string  = ""
    for x in range(len(array)):
        string += str(array[x])
        string += " "
    return string

wejscie = input() #wprowadzenie ilosci lini i maksymalnego polaczenia
wejscie = wejscie.split() #rozdzielenie ich po spacji
m=int(wejscie[1]) #przypisanie wartosci maksymalnej liczby komend
n=int(wejscie[0]) #przypisanie maksymalnej wartosci

pol = [[] for i in range(n)] # lista połączen
wyj = []
V = n;
for x in range(m): #iterowanie do liczby komend
    kom = input()
    kom = kom.split()
    len_kom = len(kom)
    for x in range(len_kom):
        kom[x] = int(kom[x])
    if kom[0] == 4: #liczba polaczen z kom[1]
        wyj.append(len(connumb(pol,kom[1])))
    elif kom[0] == 5:
        array = connumb(pol,kom[1])
        array.sort()
        wyj.append(arraytostring(array))
    elif kom[0] == 1: # dodanie polaczenia z kom[1] do kom[2] i na odwrót 
        addEdge(pol,kom[1],kom[2])
print(*wyj, sep = "\n")