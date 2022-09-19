#include <stdio.h>
#include <stdlib.h>

int main ()
{
    int n, m;

    printf("Podaj liczbe: ");
    scanf("%d",&n);

    if (n<0) {
        printf ("\nLiczba jest ujemna \n");
    }
    else
        printf ("\nLiczba jest dodatnia \n");

    return 0;
}
