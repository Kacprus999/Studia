# program do rozwiazywania rownan nieliniowych metoda stycznych
# dla pierwiastków krotnych!
def funkcja(x):
    return x * x * x - x * x - 2


def pochodna(x):
    return 3 * x * x - 2 * x


# tutaj ustawia sie dokladnosc
epsilon = 0.00001


def newtonStyczne(x):
    # poczatkowa liczba iteracji
    iterationNumber = 0
    while True:
        iterationNumber = iterationNumber + 1
        h = x
        x = x - funkcja(x) / pochodna(x)
        if abs(h - x) < epsilon and funkcja(x) < epsilon:
            print("Wartosc pierwiastka: ", "%.10f" % x)
            print("Liczba iteracji : " + str(iterationNumber))
            return x


def newtonStyczneR(x):
    iterationNumber = 0
    # tutaj nalezy podac r
    r = 2
    while True:
        iterationNumber = iterationNumber + 1
        h = x
        x = x - r * (funkcja(x) / pochodna(x))
        if abs(h - x) < epsilon and funkcja(x) < epsilon:
            print("Metoda newtona z R. Wartosc pierwiastka: ", "%.10f" % x)
            print("Liczba iteracji : " + str(iterationNumber))
            return x


# podajemy x0
x0 = 2
newtonStyczne(x0)
#newtonStyczneR(x0)
