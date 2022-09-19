#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=0,y[100],max1,max2;

    do{
        printf("Podaj liczbe uczniow <1,100>: ");
        scanf("%d",&x);
    }while(x>100 || x<1);

    for(int i=0;i<x;i++){
        scanf("%d",&y[i]);
        if(y[i]>200 || y[i]<150){
            i--;
            printf("Zly wzrost");
        }
    }

    max1=y[0];
    max2=y[0];
    for(int i=1;i<x;i++){
        if(max1<y[i])
            max1=y[i];
    }
    for(int i=1;i<x;i++){
        if((y[i]>max2) && (y[i]<max1) )
            max2=y[i];
    }

    FILE *plik;

    plik=fopen("c:\\folder\\wzrosty.txt","w");
    fprintf(plik,"%d", max1);
    fprintf(plik," %d", max2);

    fclose(plik);

    return 0;
}
