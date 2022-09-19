#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int a,b,c,p,s;

	cout<<"Podaj wartosc zmiennej a: ";
	cin>>a;
	cout<<"Podaj wartosc zmiennej b: ";
	cin>>b;
    cout<<"Podaj wartosc zmiennej c: ";
	cin>>c;
    cout<<endl<<endl<<endl;

    if((a<b+c || b<a+c || c<a+b) && a>0 && b>0 && c>0){
        p=(a+b+c)/2;
        s=sqrt(p*(p-a)*(p-b)*(p-c));
        cout<<"Pole trojkata wynosi: "<<s<<endl;
    }
    else
        cout<<"Nie mozna zrobic trojkata z takich zmiennych"<<endl;
	system("PAUSE");
	return 0;
}
