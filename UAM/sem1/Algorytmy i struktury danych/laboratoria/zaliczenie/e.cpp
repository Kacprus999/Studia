#include<iostream>
#include<cmath>
#include<cstdlib>

using namespace std;

float eps=0.0000000001;

float silnia(float n){
	if(n==1 || n==0)
	return 1;
	else return n*silnia(n-1);
}

int main(){
	double e=1;
	int i=1;
	
	while(fabs((1/silnia(i+1))-(1/silnia(i)))>=eps){
		e=e+1/silnia(i);
		i++;
	}
	cout<<"e="<<e;
	
	return 0;
}
