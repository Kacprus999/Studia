#include <stdio.h>
#include <string.h>

int main(void){

    char na1[1000],na2[1000];
    gets(na1);
    gets(na2);
    int wy = strcmp(na1,na2);
    if(wy == 0){
        printf("Napisy sa rowne");
    }
    else
        printf("napisy nie sa rowne");

    return 0;
}
