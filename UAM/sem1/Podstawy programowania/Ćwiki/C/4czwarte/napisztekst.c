#include <stdio.h>
#include <stdlib.h>

int main()
{

    FILE *plik;
    char tp[] = "Nasz tekst";
    //printf("Wpisz jeden wiersz : ");

    plik=fopen("c:\\folder\\tekstowy.txt","w");


    fputs(tp,plik); // wczytanie do pliku.


    fclose(plik);

    return 0;
}


// D:\\1Koronalia\\uniwerek\\Podstawy programowania\\Æwiki\\4czwarte\\
// C:\\folder\\
