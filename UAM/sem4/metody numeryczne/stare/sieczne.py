# program do rozwiazywania równań nieliniowych za pomocą siecznych

def funkcja(x):
    return x * x * x - x * x - 2


def sieczne(x1, x2):
    n = 0
    xm = 0
    x0 = 0
    c = 0
    iterationNumber = 0
    if funkcja(x1) * funkcja(x2) < 0:
        while True:
            iterationNumber = iterationNumber + 1
            x0 = ((x1 * funkcja(x2) - x2 * funkcja(x1)) / (funkcja(x2) - funkcja(x1)))
            c = funkcja(x1) * funkcja(x0)
            x1 = x2
            x2 = x0
            n = n + 1
            if c == 0:
                break
            xm = ((x1 * funkcja(x2) - x2 * funkcja(x1)) / (funkcja(x2) - funkcja(x1)))
            if abs(xm - x0) < epsilon and funkcja(x0) < epsilon:
                break
        print("Pierwiastek z równania wynosi: ", "%.10f" % x0)
        print("Liczba iteracji: " + str(iterationNumber))


x1 = 1
x2 = 2
epsilon = 0.00001
sieczne(x1, x2)
