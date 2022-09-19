#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){

    int T,x[50],y[50],wynik;

    do{
        scanf("%d",&T);
    }while(T<0 && T>51);

    for(int i=0;i<T;i++){
        do{
            scanf("%d %d",&x[i],&y[i]);
        }while(x[i]<0 && x[i]>101 && y[i]<0 && y[i]>101);

    }
    for(int i=0;i<T;i++){
        wynik=x[i]*y[i];
        printf("%d \n",wynik);
    }
    return 0;
}

