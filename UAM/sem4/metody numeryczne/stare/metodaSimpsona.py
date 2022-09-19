#funkcja
def f(x):
    return x * x * x + 1



def simpson13(x0, xn, n):
    h = (xn - x0) / n

    calka = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        if i % 2 == 0:
            calka = calka + 2 * f(k)
        else:
            calka = calka + 4 * f(k)

    calka = calka * h / 3

    return calka


dolna_granica = float(input("Wprowadź dolną granicę "))
gorna_granica = float(input("Wprowadź górną granicę  "))
liczba_przedzialow = int(input("Wprowadź liczbę przedzialow (b-a)/krok "))

wynik = simpson13(dolna_granica, gorna_granica, liczba_przedzialow)
print("Integration result by Simpson's 1/3 method is: %0.6f" % wynik)