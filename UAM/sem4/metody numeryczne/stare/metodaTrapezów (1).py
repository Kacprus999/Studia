# program do przyblizonego calkowania przy pomocy metody trapezow (funkcje liniowe)
# trzeba pamiętać żeby zmieniać funkcję przed każdym użyciem programu
def funkcja(x):
    return x * x * x + 1


def trapezy(x0, xn, n):
    h = (xn - x0) / n
    calka = funkcja(x0) + funkcja(xn)
    for i in range(1, n):
        k = x0 + i * h
        calka = calka + 2 * funkcja(k)
    calka = calka * h / 2
    return calka


dolna_granica = float(input("Wprowadź dolną granicę "))
gorna_granica = float(input("Wprowadź górną granicę  "))
liczba_przedzialow = int(input("Wprowadź liczbę przedzialow (b-a)/krok "))

wynik = trapezy(dolna_granica, gorna_granica, liczba_przedzialow)
print("Przybliżony wynik tego całkowania to: %0.6f " % wynik)
