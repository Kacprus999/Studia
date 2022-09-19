#include <stdio.h>
#include <string.h>

int main(void){

    char na1[1000];
    char alfa[] = "abcdefghijklmnopqrstuwxyz";
    char liczba[]= "0123456789";
    gets(na1);

    FILE *plik;
    plik=fopen("wynik.txt","a+");

    int liczba1,liczba2,licznik=0,litera=0;
    liczba1 = strlen(na1);
    liczba2 = strlen(alfa);

    for(int i=0;i<liczba1;i++){
        for(int j=0;j<liczba2;j++){
            if(na1[i] == alfa[j])
                litera++;
        }
        for(int j=0;j<10;j++){
            if(na1[i] == liczba[j])
                licznik++;
        }
    }
    fprintf(plik,"Mamy %d litery \nMamy %d cyfry", litera,licznik);

    fclose(plik);
    return 0;
}
