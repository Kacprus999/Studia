#include<iostream>
#include<cmath>

using namespace std;
 
int main()
{


	for(int n=2;n<=100;n++)
	{
		int suma=0;
		
		for(int i=n/2;i>0;i--)
			if(n%i==0)
				suma=suma+i;

		if(suma==n)
			cout<<suma<<endl;
	}
	return 0;
}
