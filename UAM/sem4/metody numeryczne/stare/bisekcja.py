# program do bisekcji
def funkcja(x):
    return x * x * x - x * x - 2


def bisekcja(a, b):
    iterationNumber = 0
    c = (a + b) / 2
    while True:
        c = (a + b) / 2
        print(c)
        iterationNumber = iterationNumber + 1
        if funkcja(c) == 0 or abs(funkcja(c)) < epsilon:
            break
        y = funkcja(a) * funkcja(c)
        if y < 0:
            b = c
        else:
            a = c

    print("Pierwiastek z równania wynosi: ", "%.10f" % c)
    print("Liczba iteracji: " + str(iterationNumber))


# tutaj wprowadzamy dane
a = 1
b = 2
epsilon = 0.00001
bisekcja(a, b)
