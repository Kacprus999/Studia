print("Jak chcesz to zrobic? (1-reczne wprowadzenie danych, 2-z pliku)")
wybor = int(input())
if wybor == 1:
    print("\nPodaj klucz: ")
    klucz = int(input())
    print("Podaj tekst: ")
    tekst = input()
    kod = ""
    for i in tekst:
        if i.islower():
            i_index = ord(i) - ord('a')
            i_zmienione = (i_index + klucz) % 26 + ord('a')
            i_nowy=chr(i_zmienione)
            kod += i_nowy
        elif i.isupper():
            i_index = ord(i) - ord('A')
            i_zmienione = (i_index + klucz) % 26 + ord('A')
            i_nowy=chr(i_zmienione)
            kod += i_nowy
        else:
            kod += i
    print(kod)
elif wybor == 2:
    print("\nZamiana z pliku:")
    plik=open('szyfr.py')
    import linecache
    klucz=int(linecache.getline('szyfr.py',1))
    tekst=linecache.getline('szyfr.py',2)
    
    kod = ""
    for i in tekst:
        if i.islower():
            i_index = ord(i) - ord('a')
            i_zmienione = (i_index + klucz) % 26 + ord('a')
            i_nowy=chr(i_zmienione)
            kod += i_nowy
        elif i.isupper():
            i_index = ord(i) - ord('A')
            i_zmienione = (i_index + klucz) % 26 + ord('A')
            i_nowy=chr(i_zmienione)
            kod += i_nowy
        else:
            kod += i
    print(kod)
    plik.close()
else:
    print("zly wybor")
