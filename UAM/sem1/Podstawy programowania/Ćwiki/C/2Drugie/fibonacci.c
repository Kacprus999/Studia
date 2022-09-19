#include <stdio.h>
#include <stdlib.h>

int main ()
{
    float n=0,x=0,y=0,podatek=0;

    printf("Podaj kwote dochodu: ");
    scanf("%f",&n);

    if (n<0) {
        printf ("\nDochod nie moze byc ujemny\n");
    }
    else if (n>5000 && n<85528){
        x = n - 5000;
        x = x*0.18;
    }
    else if (n>85528){
        y = n - 85528;
        y = y *0.32;
    }

    podatek = x+y;
    printf("Twoj podatek to: ");
    printf("%g", podatek);


    return 0;
}
