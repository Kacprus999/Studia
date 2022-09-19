#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double a,b,c,delta,x1,x2;

	cout<<"Podaj wartosc zmiennej a: ";
	cin>>a;
	cout<<"Podaj wartosc zmiennej b: ";
	cin>>b;
    cout<<"Podaj wartosc zmiennej c: ";
	cin>>c;

    cout<<endl<<endl<<endl;


    if(a!=0){
        cout<<"Twoj wzor to: "<<a<<"x^2+"<<b<<"x+"<<c<<"=0"<<endl<<endl;
        delta = (b*b)-(4*a*c);
        if (delta>0){
            x1 = (-b-sqrt(delta))/(2*a);
            x2 = (-b+sqrt(delta))/(2*a);
            cout<<"Pierwiastki wynosza: "<<x1<<" i "<<x2<<endl<<endl;
        }
        else if (delta==0){
            x1 = (-b)/(2*a);
            cout<<"Pierwiastek wynosi: "<<x1<<endl<<endl;
        }
        else if (delta<0)
	        cout<<"nie ma rozwiazan rzeczywistych"<<endl<<endl;
    }
    else
        cout<<"funkcja jest liniowa"<<endl;

    system("PAUSE");
	return 0;
}
