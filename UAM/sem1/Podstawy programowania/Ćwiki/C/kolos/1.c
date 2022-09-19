#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int najwspwie(int a, int b){
    int pom;

    while(b!=0){
        pom = b;
        b=a%b;
        a=pom;
    }

    return a;
}

int main(){

    int n,a[20],b[20];

    printf("Podaj liczbe zestawow danych <1,20> \n");
    do{
        scanf("%d",&n);
    }while(n<0 && n>21);

    printf("Podaj liczbe dzieci w grupach <10,30> (po spacji)\n");
    for(int i=0; i<n;i++){
        do{
            scanf("%d %d",&a[i],&b[i]);
        }while( a[i]<10 && a[i]>30 && b[i]<10 && b[i]<30 );
    }

    for(int i=0; i<n; i++){
        printf("Liczba potrzebnych cukierkow dla zestawu %d wynosi: %d \n",i+1,a[i]/najwspwie(a[i],b[i])*b[i]);
    }

    return 0;
}
