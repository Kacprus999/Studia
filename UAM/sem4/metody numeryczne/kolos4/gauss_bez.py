import numpy as np
import sys

# nalezy wprowadzic macierz oraz wektor jako dodatkowa kolumne macierzy
a = [
    [1,-1,2,2,0],
    [2,-2,1,0,1],
    [-1,2,1,-2,1],
    [2,-1,4,0,2]
]
n = len(a)

# wlasciwy algorytm
for i in range(n):

    print('------ step ' + str(i) + ' -----')
    print('macierz wejsciowa')
    y = np.array(a)
    print(y)

    if a[i][i] == 0.0:
        sys.exit('(' + str(i) +') dzielenie przez zero')

    #eliminacja gaussa  
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
    
    print('(' + str(i) +') po eliminacji gaussa')
    y = np.array(a)
    print(y)

#tablica wynikowa
x = np.zeros(n)

#obliczenie przeszukiwaniem wstecz (back substitution)
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

#wynik
for i in range(n):
    print('X%d = %0.2f' %(i+1,x[i]), end = '\t')