#include<iostream>
#include<cmath>


using namespace std;

int main()
{
	bool tab[99];
	
	for(int i=2;i<=100;i++)
	tab[i]=true;	
	
	for(int k=2;k<=100;k++){	
		if(tab[k]==true){
			for(int j=2*k;j<=100;j+=k)
				tab[j]=false;
		}
	}

	for(int l=2;l<=100;l++)
		if(tab[l]!=false)
			cout<<l<<" ";
		
	return 0;
}
