#include <stdio.h>
#include <string.h>

int main(void){

    char na1[1000];
    char alfa[] = "abcdefghijklmnopqrstuwxyz";
    gets(na1);

    int liczba1,liczba2;
    liczba1 = strlen(na1);
    liczba2 = strlen(alfa);

    int litera[liczba2];
    for(int i=0;i<liczba2;i++)
        litera[i] = 0;

    for(int i=0;i<liczba1;i++){
        for(int j=0;j<liczba2;j++){
            if(na1[i] == alfa[j])
                litera[j]++;
        }
    }

    for(int j=0;j<liczba2;j++){
            if(litera[j]!=0)
                printf("%c: %d \n",alfa[j],litera[j]);
        }


    return 0;
}
