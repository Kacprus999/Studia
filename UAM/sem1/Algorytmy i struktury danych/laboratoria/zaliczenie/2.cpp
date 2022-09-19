#include <iostream>
#include <math.h>

using namespace std;

void doskonale(){
    int suma;

    for(int i=6;i<pow(10,9);i++){
        suma=0;

        for(int j=1;j<=i/2;j++){
            if(i%j==0)
                suma = suma+j;
        }

        if(i==suma)
            cout<<"Liczba "<<i<<" jest liczba doskonala"<<endl;
    }
}

int main(){

    doskonale();

    return 0;
}
