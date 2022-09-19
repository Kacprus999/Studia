#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=0,y=0,z=0,t=0;

    printf("Podaj liczbe jakiej chcesz szukac: ");
    scanf("%d",&x);
    printf("Podaj ilosc liczb jakie chcesz podac: ");
    scanf("%d",&y);

    for(int i=0;i<y;i++){
        scanf("%d",&t);
        if(t == x)
            z++;
    }
    FILE *plik;
    char tp = z;

    plik=fopen("c:\\folder\\liczbawystapien.txt","w");


    fputs(z,plik); // wczytanie do pliku.


    fclose(plik);
   return 0;
}
