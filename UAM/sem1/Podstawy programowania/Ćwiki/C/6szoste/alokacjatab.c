#include <stdio.h>
#include <math.h>

int main (void)
{

    int *tab;
    tab = malloc(100*sizeof(*tab));

    for(int i=0; i<100; i++)
        tab[i] = i;

    free(tab);
    return 0;
}
