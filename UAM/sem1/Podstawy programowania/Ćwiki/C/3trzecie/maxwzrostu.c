#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=0,y[10000],z;

    printf("Podaj liczbe uczniow <1,10 000>: ");
    scanf("%d",&x);


    for(int i=0;i<x;i++){
        scanf("%d",&y[i]);
    }
    z=y[0];
    for(int i=1;i<x+1;i++){
        if(z<y[i])
            z=y[i];
    }

    printf("Najwyzsza liczba to %d",z);
    return 0;
}
