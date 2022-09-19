#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*a liczb� zestaw�w
    W pierwszej linii znajduje si� liczba D, oznaczaj�c danych. Ka�dy zestaw danych mie�ci si� w jednej linii i sk�ada si� z sze�ciu liczb: a1, a2, a3, a4, a5,
    k (ai<=1000, k<=10 000). Liczby a1..a5 oznaczj� dost�pn� w bankomacie liczb� baknot�w odpowiednio o nomina�ach 10, 20, 50, 100, 200 frank�w szwajcarskich. Natomiast liczba k oznacza ��dan� kwot� do wp�aty.

    Dla ka�dego zestawu danych powinna pojawi� si� jedna linia w wyniku zawieraj�ca pojedyncze s�owo TAK lub NIE, oznaczaj�ce czy w danej chwili w bankomacie da si� wyp�aci� ��dan� kwot�.
    */
    int D=0,a[5],k;

    scanf("%d",&D);


    for(int i=0;i<D;i++){

        for(int j=0;j<5;j++){
            scanf("%d",&a[j]);
            if(a[j]>1000){
                printf("Podales za duza liczbe banknotow \n");
                j--;
            }
        }
        scanf("%d",&k);

        if(k>10000)
            printf("Podales za duza kwote \n");
        else{

            while((a[4]>0) && (k>=200))
                k=k-200;

            while((a[3]>0) && (k>=100))
                k=k-100;

            while((a[2]>0) && (k>=50))
                k=k-50;

            while((a[1]>0) && (k>=20))
                k=k-20;

            while((a[0]>0) && (k>=10))
                k=k-10;

            if(k==0)
                printf("TAK");
            else
                printf("NIE");

        }

    }

    return 0;
}
