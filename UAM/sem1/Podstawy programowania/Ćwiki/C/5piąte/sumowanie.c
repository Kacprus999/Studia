#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,tab[100000],wyn=0;

    scanf("%d",&n);

    for(int i=0; i<n; i++){
        scanf("%d", &tab[i]);
    }

    for(int i=0; i<n; i++){
        wyn = wyn +tab[i];
    }
    printf("%d",wyn);


    return 0;
}
