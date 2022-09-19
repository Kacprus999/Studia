#include <stdio.h>
#include <stdlib.h>

int main()
{
    int d,n,vip=0,wynik[100],znane[500][500];

    do{
        scanf("%d",&d);
    }while(d<1 && d>100);


    for(int i=0;i<d;i++){
        wynik[i]=0;

        do{
            scanf("%d",&n);
        }while(n<1 && n>500);

        for(int w=0;w<n;w++){
            for(int k=0;k<n;k++){
                scanf("%d",&znane[w][k]);
                vip=vip+znane[w][k];
            }
            if (vip==1)
                wynik[i]= w+1;

            vip=0;
        }
    }
    for(int i=0;i<d;i++)
        printf("%d \n", wynik[i]);

    return 0;
}
