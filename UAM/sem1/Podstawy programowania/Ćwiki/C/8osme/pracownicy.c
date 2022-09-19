#include <stdio.h>
#include <string.h>

int main(void){

    struct pracownicy{
        struct dane_os{
            char imie[30];
            char nazwisko[30];
            char pesel[11];
        };
        int wynagrodzenie2018[12];
    };

    return 0;
}
