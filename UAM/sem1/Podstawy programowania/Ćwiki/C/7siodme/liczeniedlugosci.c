#include <stdio.h>
#include <string.h>

int main(void){

    char dl[1000];
    int len;
    gets(dl);
    len = strlen(dl);
    printf("%d", len);

    return 0;
}
