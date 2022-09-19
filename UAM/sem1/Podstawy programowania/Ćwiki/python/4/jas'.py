n=int(input())
if n>=1 and n<=1000:
    imiona=[]
    wyksztalcenie=[]
    i=1
    while(i<=n):
        linia=input()
        tablica=linia.split()
        imie=tablica[0]
        wyksz=tablica[1]
        if (imie.isalpha()==True)and(wyksz=="p" or wyksz=="s" or wyksz=="g" or wyksz=="w"):
            if wyksz=="p":
                wyksztalcenie.append(1)
            elif wyksz=="g":
                wyksztalcenie.append(2)
            elif wyksz=="s":
                wyksztalcenie.append(3)
            else:
                wyksztalcenie.append(4)
            imiona.append(imie)
        i=i+1
    i=0
    minimalne=input()
    if minimalne=="p":
        wyk=1
    elif minimalne=="g":
        wyk=2
    elif minimalne=="s":
        wyk=3
    else:
        wyk=4
    while(i<n):
        if(wyksztalcenie[i]>=wyk):
            print(imiona[i])
        i=i+1
        
        
