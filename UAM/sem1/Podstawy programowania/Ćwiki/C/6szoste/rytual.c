#include <stdio.h>
#include <math.h>

int main (void)
{

    int x[20],test,lisc=0,kwiat=0,zero,licznik=0;

    do{
        scanf("%d",&test);
        for(int i=0;i<test;i++){
            do{
                scanf("%d",&x[i]);
            }while(x[i]>100 || x[i]<2);
        }
        scanf("%d",&zero);
    }while(zero!=0 && (test>20 || x<0) );

    for(int i=0;i<test;i++){
        do{
            if(x[i]%2==0){
                x[i]=x[i]/2;
                kwiat++;
            }
            else{
                x[i]=3*x[i]+1;
                lisc++;
            }
            licznik++;
        }while(x[i]!=1);

        if(licznik<16)
            printf("TAK %d %d \n",kwiat , lisc);
        else
            printf("NIE \n");

        licznik=0,lisc=0,kwiat=0;
    }


    return 0;
}
