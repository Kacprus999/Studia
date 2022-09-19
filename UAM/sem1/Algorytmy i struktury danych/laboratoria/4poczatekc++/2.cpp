#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int m, n,i=1;

	cout<<"Podaj wartosc zmiennej m: ";
	cin>>m;
	cout<<"Podaj wartosc zmiennej n: ";
	cin>>n;
    cout<<endl<<endl<<endl;
    if(m>n && n!=0){
        do{
            m=m-n;
            i+=1;
        }while(m>=n);
        cout<<"Reszta to: "<<m<<endl;
        cout<<"Iloraz calkowity to: "<<i-1<<endl;
    }
    else if(n>m && m!=0){
        do{
            n=n-m;
            i+=1;
        }while(n>=m);
        cout<<"Reszta to: "<<m<<endl;
        cout<<"Iloraz calkowity to: "<<i-1<<endl;
    }

	system("PAUSE");
	return 0;
}
