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
    //printf("Twoja liczba pojawila sie %d razy ",z);

    FILE *plik;
    plik=fopen("c:\\folder\\liczbawystapien.txt","w");
    fprintf(plik,"%d",z); // wczytanie do pliku.
    fclose(plik);

   return 0;
}
