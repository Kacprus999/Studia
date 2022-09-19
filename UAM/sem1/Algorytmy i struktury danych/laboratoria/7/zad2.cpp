#include <list>
#include<iostream>
#include<stack>
#include <cstdlib>

using namespace std;

int main()
{
	list<int>lista;
	stack<int>s;
	int ele;

	cout<<"Podaj 10 elementow listy: "<<endl;
	for(int i=0;i<10;i++){
		cin>>ele;
		lista.push_back(ele);
	}

	cout<<endl<<"Wstawienie z listy do stosu... "<<endl<<endl;

	while(!lista.empty()){
		s.push(lista.front());
		lista.pop_front();
	}

	cout<<"Wyswietlenie stosu:"<<endl;
	while(!s.empty()){
		cout<<s.top()<<" ";
		s.pop();
	}

	return 0;
}
