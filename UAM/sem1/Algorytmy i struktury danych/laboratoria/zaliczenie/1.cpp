#include <iostream>
#include <math.h>

using namespace std;

void Armstrong(){
    int potega, suma,a,b;       //a,b pomocniczne

    for(int i=100;i<=999999999;i++){
        a = i,b=0, suma=0, potega=0;

        while(a>0){         //obliczanie ilosci cyfr w liczbie
            a = a/10;       
            b++;
        };
        
        a = i, potega = b, b=0;

        while(a!=0){
            b = a%10;       //pobieranie ostatniej cyfry
            a = a/10;       //usuwanie ostatniej cyfry
            suma = suma + pow(b,potega); 
        };
        if(i==suma)
            cout<<"Dla liczby k = "<<potega<<", A = "<<i<<" jest liczba Armstronga"<<endl;
    }
}

int main(){

    Armstrong();
    return 0;
}