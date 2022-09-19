#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	int A=100;
	
	for(int a=A;a<1000000000;a++)
	{
		int B=a,i=0;
		for( ;B>=1;i++)
			B=B/10;

		int suma=0;
		B=a;
		for(int j=1;j<=i;j++){
			int r=B%10;
			suma=suma+pow(r,i);
			//cout<<"suma "<<j<<"= "<<suma<<endl;
			B=B/10;	
		}
		
		if(a==suma)
		cout<<a<<endl;
	}
	return 0;
}
