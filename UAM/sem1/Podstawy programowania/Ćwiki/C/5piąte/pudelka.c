#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,tab[100],y,a[1000],b[1000],wyn=0;

    do{
        scanf("%d",&x);
    }while(x>1000 && x<1);

    for(int i=0;i<x;i++){
        do{
            scanf("%d",&tab[i]);
        }while(tab[i]>100);
    }

    do{
        scanf("%d",&y);
    }while(y>1000 && y<1);

     for(int i=0;i<y;i++){
        do{
            scanf("%d %d",&a[i],&b[i]);
        }while(a[i]<1 && b[i]<a[i] && b[i]>x);
    }

    for(int i=0;i<y;i++){
        for(int j=a[i]-1;j<b[i];j++)
            wyn=wyn+tab[j];
        printf("\n%d", wyn);
        wyn = 0;
    }


    return 0;
}
