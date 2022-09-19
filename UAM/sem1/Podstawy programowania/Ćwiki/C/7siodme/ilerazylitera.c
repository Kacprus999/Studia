#include <stdio.h>
#include <string.h>

int main(void){

    char na1[1000],litera;

    scanf("%c",&litera);
    scanf("%s",&na1);

    int liczba;
    liczba = strlen(na1);
    int licznik=0;

    for(int i=0;i<liczba;i++){
        if(na1[i]==litera)
            licznik++;
    }

    printf("%c = %d ",litera,licznik);

    return 0;
}
