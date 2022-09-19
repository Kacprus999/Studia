#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int a, b;

	cout<<"Podaj wartosc zmiennej a: ";
	cin>>a;
	cout<<"Podaj wartosc zmiennej b: ";
	cin>>b;	
	cout<<"Przed zamiana: a = "<<a<<", b = "<<b<<endl;
    cout<<endl<<endl<<endl;

	a = a - b;
	b = b + a;
	a = b - a;
	
	cout<<"Po zamianie: a = "<<a<<", b = "<<b<<endl;

	system("PAUSE");
	return 0;
}