#!/usr/bin/python
import psycopg2
from psycopg2 import Error


usernam = raw_input("Podaj nazwe uzytkownika: ")
passwd = raw_input("Podaj haslo: ")
server = raw_input("Podaj serwer hosta: ")
dbname = raw_input("Podaj nazwe bazy danych: ")
zapyt = raw_input("Wprowadz zapytanie bazy danych: ")
print("\n\n\n\n\n")

#zmodyfikowany fragment kodu wziety z https://pynative.com/python-postgresql-tutorial/#h-python-postgresql-database-connection

try:
    # Laczenie sie z baza danych
    polacz = psycopg2.connect(user=usernam, password=passwd, host=server, database=dbname)
    # Tworzenie kursora
    kursor = polacz.cursor()
    # Wykonywanie zapytania
    kursor.execute(zapyt) 
    # zapisywanie zapytania do zmiennej
    wynik = kursor.fetchall()
    
    # wyswietlenie pobranej ilosci wierszy
    print('Liczba pobranych wierszy: ', kursor.rowcount)
    
    #wyswietlanie wierszu po wierszu
    for wiersz in wynik:
        print(wiersz)
      

except (Exception, Error) as error:
    print("Blad podczas laczenia z PostgreSQL", error)
finally:
    if (polacz):
        kursor.close()
        polacz.close()
        print("PostgreSQL polaczenie zostalo zamkniete")