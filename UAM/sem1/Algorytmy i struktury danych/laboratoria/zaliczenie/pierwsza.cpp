#include<iostream>
#include<cmath>

using namespace std;

int pierwsza(int a){
	for(int d=a/2;d>1;d--)	
		if(a%d==0)
			return 0;
	return 1;
}
int main(){
	for(int n=1;n<=100;n++)
	{
		if(pierwsza(n)==1)
			cout<<n<<endl;
		
	}
	return 0;
}
