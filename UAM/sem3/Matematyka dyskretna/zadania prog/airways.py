class Graph(object):

    # inicjalizacja matrixa
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # dodanie krawedzi
    def add_edge(self, v1, v2):
        if not v1 == v2:
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
wejscie = input() #wprowadzenie ilosci lini i maksymalnego polaczenia
wejscie = wejscie.split() #rozdzielenie ich po spacji
m=int(wejscie[1]) #przypisanie wartosci maksymalnej liczby komend
n=int(wejscie[0]) #przypisanie maksymalnej wartosci

wyj = []   
g = Graph(n)

for x in range(m): #iterowanie do liczby komend
    kom = input()
    kom = kom.split()
    len_kom = len(kom)
    for x in range(len_kom):
        kom[x] = int(kom[x])
    if kom[0] == 4: #liczba polaczen z kom[1]
        wyj.append(g.connumb(kom[1]))
    elif kom[0] == 1: # dodanie polaczenia z kom[1] do kom[2] i na odwrót 
        g.add_edge(kom[1],kom[2])
    elif kom[0] == 2: # usuniecie polaczeniz z kom[1] do kom[2] i na odwrót
        g.remove_edge(kom[1], kom[2])
    elif kom[0] == 3: # pytanie tak/nie czy istnieje polaczenie z kom[1] do kom[2]
        if g.isconnected(kom[1],kom[2])== True:
            wyj.append("TAK")
        else:
            wyj.append("NIE")
print(*wyj, sep = "\n")