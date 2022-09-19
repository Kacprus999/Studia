#include <stdio.h>

int main ()
{
    int x = 1,tab[100];

    printf ("Podaj liczbe z przedzialu 1 do 100 \n");
    scanf("%d",&x);
    if(x>0 && x<101){
        for(int i=0;i<x;i++){
            scanf("%d",&tab[i]);
        }
        for(int i=0;i<x;i++){
            if(tab[i]>0)
                printf ("1 ");
            else
                printf ("0 ");
        }
    }
    else
        printf ("Podales zla liczbe \n");





return 0;
}
