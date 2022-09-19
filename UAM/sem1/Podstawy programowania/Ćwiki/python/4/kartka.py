n = int(input())
lin=[]
i = 1
while(i<=n):
    linia=input()
    l=len(linia)
    lin.append(linia)
    i=i+1
for i in lin:
    liczby=0
    litery=0
    znaki=len(i)
    for a in i:
        if a.isdigit()==True:
            liczby=liczby+1
        elif a.isalpha()==True:
            litery=litery+1
    print(znaki,litery,liczby)
