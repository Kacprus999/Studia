#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m,tab[100][100];

    do{
        scanf("%d %d",&n,&m);
    }while(n>100 && n<2 && m>100 && m<2);

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
            scanf("%d", &tab[i][j]);
    }

    for(int i=m-1; i>=0; i--){
        for(int j=0; j<n; j++){
            printf("%d ", tab[j][i]);
        }
        printf("\n");
    }

    return 0;
}
