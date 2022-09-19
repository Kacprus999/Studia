#include <stdio.h>
#include <string.h>

int main(void){

    char na1[1000],na2[1000];
    gets(na1);
    gets(na2);
    strcat(na1,na2);
    printf("%s", na1);

    return 0;
}
