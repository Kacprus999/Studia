x = input()
x = x.split()
maxx = int(max(x))
minn = int(min(x))
if minn < 0:
    print(maxx-minn)
else:
    print("brak liczby ujemnej")
        
    
