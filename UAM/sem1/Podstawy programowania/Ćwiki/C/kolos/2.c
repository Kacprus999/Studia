#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){

    int n,a[100];

    printf("Podaj dlugosc tablicy <1,100> \n");
    do{
        scanf("%d",&n);
    }while( n<0 && n>101);

    printf("Podaj elementy tablicy (odzielone spacja, tylko liczby calkowite) \n");
    for(int i=0; i<n;i++){
        scanf("%d",&a[i]);
    }

    for(int i=0; i<n; i++){
        if( a[i]%3!=0 ){
            printf("%d ", a[i]);
        }
    }

    return 0;
}
