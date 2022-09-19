#include <stdio.h>
#include <stdlib.h>

int pokolenia(int m){
    if(m==1)
        return 7;
    else if(m%2==0)
        return 5*pokolenia(m-1)+ pokolenia(m-1);
    else
        return 3*pokolenia(m-1)+ pokolenia(m-1);
}

int main()
{
    int n, m, wynik;

    do{
        scanf("%d",&n);
    }while(n<1 && n>20);

    for(int i=0;i<n;i++){
        do{
            scanf("%d",&m);
        }while(m<1 && m>15);
        printf("%d \n",pokolenia(m));
    }


    return 0;
}



