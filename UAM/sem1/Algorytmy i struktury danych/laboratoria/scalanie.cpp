#include<iostream>
#include<cstdlib>
using namespace std;

int *pom;

void scal(int tab[], int min, int mid, int max){
    int i = min, j = mid + 1;

    for(int i = min;i<=max; i++) 
        pom[i] = tab[i];  

    for(int k=min;k<=max;k++){
        if(i<=mid)
            if(j <= max)
                if(pom[j]<pom[i])
                    tab[k] = pom[j++];
                else
                    tab[k] = pom[i++];
            else
                tab[k] = pom[i++];
        else
            tab[k] = pom[j++];
    }
}
void sort(int tab[],int min, int max){
	if(max<=min) return; 
	int mid = (max+min)/2;
	sort(tab, min, mid); 
	sort(tab, mid+1, max);
	scal(tab, min, mid, max);
}
int main()
{
	int *tab,n;
	cin>>n;
	tab = new int[n];
	pom = new int[n];
	for(int i=0;i<n;i++)
		cin>>tab[i];

	sort(tab,0,n-1);
	for(int i=0;i<n;i++)
		cout<<tab[i]<<" ";
	
	system("pause");
	return 0;
}