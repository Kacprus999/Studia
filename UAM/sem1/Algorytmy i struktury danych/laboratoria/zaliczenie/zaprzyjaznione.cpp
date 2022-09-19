#include<iostream>
#include<cmath>

using namespace std;
int suma_dzielnikow(int n)
{
	int suma=0;
	for(int i=n/2;i>0;i--){
		if(n%i==0)
			suma=suma+i;
	}
	return suma;
}

int main()
{
	for(int i=1;i<10000;i++)
		for(int j=i+1;j<=10000;j++)
			{
				if(i!=j)
				{
					if((suma_dzielnikow(i)==j)&&(suma_dzielnikow(j)==i))
						cout<<i<<"  "<<j<<endl;
				}
			}
	return 0;
}
