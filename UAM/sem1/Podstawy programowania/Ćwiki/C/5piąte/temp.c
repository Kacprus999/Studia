#include <stdio.h>
#include <stdlib.h>

int main()
{
    int tab[14],n=0;

    for(int i=0; i<14; i++){
        scanf("%d", &tab[i]);
    }

    for(int j=1; j<3; j++){
        for(int i=1; i<8; i++){
            printf("MIASTO %d",j);
            printf(", dzien %d",i);
            printf(" = %d",tab[n]);
            printf("\n");
            n++;
        }
    }



    return 0;
}
