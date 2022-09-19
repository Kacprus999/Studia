#dodanie krawedzi w grafie
def addEdge(adj, u, v):
	adj[u].append(v)
	adj[v].append(u)
#usuniecie krawedzi
def delEdge(adj, u, v):
	# usuniecie z pierwszej listy drugiego elementu
	for i in range(len(adj[u])):	
		if (adj[u][i] == v)		
			adj[u].pop(i)
			break;
	# usuniecie z drugiej listy pierwszego elementu
	for i in range(len(adj[v])):
		if (adj[v][i] == u):		
			adj[v].pop(i)
			break;


wejscie = input() #wprowadzenie ilosci lini i maksymalnego polaczenia
wejscie = wejscie.split() #rozdzielenie ich po spacji
m=int(wejscie[1]) #przypisanie wartosci maksymalnej liczby komend
n=int(wejscie[0]) #przypisanie maksymalnej wartosci

if m < 1000000 and n < 1000:
    pol = [] # lista połączen
    wyj = []
    for x in range(m): #iterowanie do liczby komend
        kom = input()
        kom = kom.split()
        len_kom = len(kom)
        for x in range(len_kom):
            kom[x] = int(kom[x])
        if kom[1] < n:
            if len_kom == 2 and kom[0] == 4: #liczba polaczen z kom[1]
                liczba = [v for v in pol if str(kom[1]) in v]
                wyj.append(int(len(liczba)/2))
            elif len_kom == 3:
                if kom[2]<n:
                    test1 = str(kom[1])+str(kom[2])
                    test2 = str(kom[2])+str(kom[1])
                    if kom[0] == 1: # dodanie polaczenia z kom[1] do kom[2] i na odwrót 
                        #sprawdz = next(i for i in pol if i == test) 
                        if not test1 in pol: # jesli nie ma polaczenia to je dodaj
                            pol.append(test1)
                            pol.append(test2)
                        else: # jesli jest to nic nie rob
                            continue
                    elif kom[0] == 2: # usuniecie polaczeniz z kom[1] do kom[2] i na odwrót
                        if test1 in pol: # jesli jest polaczenie to je usun
                          pol.remove(test1)
                          pol.remove(test2)
                        else: # jesli nie ma to nic nie rob
                            continue
                    elif kom[0] == 3: # pytanie tak/nie czy istnieje polaczenie z kom[1] do kom[2]
                        if test1 in pol:
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