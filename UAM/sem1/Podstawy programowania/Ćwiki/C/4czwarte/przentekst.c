#include <stdio.h>
#include <stdlib.h>

int main()
{
    char pomoc[100];
    FILE *plik;
    plik=fopen("c:\\folder\\pierwszy.txt","r");
    fgets(pomoc,100,plik);
    fclose(plik);

    FILE *plik2;
    plik2=fopen("c:\\folder\\drugi.txt","w");
    fputs(pomoc,plik2);

    fclose(plik2);
    return 0;
}


// D:\\1Koronalia\\uniwerek\\Podstawy programowania\\Æwiki\\4czwarte\\
// C:\\folder\\
