#include <iostream>
#include <math.h>

using namespace std;

void zaprzyjaznione(){
    int sumaa,sumab;

    for(int i=2;i<pow(10,4);i++){
        sumaa=0;
        sumab=0;

        for(int j=1;j<=i/2;j++){
            if(i%j==0)
                sumaa = sumaa+j;
        }
        if(i<sumaa){
            for(int x=1;x<=sumaa/2;x++){
                if(sumaa%x==0)
                    sumab = sumab+x;
            }
                if(sumab==i)
                    cout<<"Liczba "<<i<<" jest zaprzyjazniona z liczba "<<sumaa<<endl;
        }
    }
}

int main(){

    zaprzyjaznione();

    return 0;
}