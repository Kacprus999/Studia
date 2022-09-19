#include <stdio.h>
#include <stdlib.h>

int main()
{

    FILE *plik;
    char tp[11];
    //printf("Wpisz jeden wiersz : ");

    plik=fopen("c:\\folder\\tekstowy.txt","r");

    fgets(tp,11,plik);
    printf("%s",tp); // wczytanie do pliku.


    fclose(plik);

    return 0;
}


// D:\\1Koronalia\\uniwerek\\Podstawy programowania\\Æwiki\\4czwarte\\
// C:\\folder\\
