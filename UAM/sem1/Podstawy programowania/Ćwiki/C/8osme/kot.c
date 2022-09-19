#include <stdio.h>
#include <string.h>

int main(void){

    struct kot{
        char imie[15];
        char rasa[30];
        char masc[30];
        int wiek;
    };
    struct kot pierwszy;

    scanf("%s", &pierwszy.imie);
    scanf("%s", &pierwszy.rasa);
    scanf("%s", &pierwszy.masc);
    scanf("%d", &pierwszy.wiek);

    printf(" imie: %s \n rasa: %s \n masc: %s \n wiek: %d",pierwszy.imie, pierwszy.rasa, pierwszy.masc, pierwszy.wiek);
    return 0;
}
