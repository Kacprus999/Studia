import math
#program do przyblizonego calkowania przy pomocy metody trapezow (funkcje liniowe)


def fun(x):
    wzor_funkcji = math.exp()**x - math.sin(x)
    return wzor_funkcji
    

def trapezy(x0, xn, n):
    h = (xn - x0) / n
    calka = fun(x0) + fun(xn)
    for i in range(1,n):
        k = x0 + i*h
        calka = calka + 2 * fun(k)
    calka = calka * h/2
    return calka

a = -4
b = -3
n = 4

wynik = trapezy(a, b, n)

print("wynik: %0.6f " % wynik)
