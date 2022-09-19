#include <stdio.h>
#include <stdlib.h>

int main ()
{
    int n, m;

    printf("Podaj liczbe (n) i (m) z przedzialu <-100;100>: ");
    scanf("%d",&n);
    scanf("%d",&m);

    if (n<-100 || n>100 || m<-100 || m>100) {
        printf ("\nPodales zla liczbe \n");
    }
    else{
        return m+n;
    }
    return 0;
}
