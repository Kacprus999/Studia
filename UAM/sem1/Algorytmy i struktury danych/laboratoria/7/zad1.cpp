#include<iostream>
#include<stack>
#include <cstdlib>
#include<queue>
using namespace std;


void print_que(queue<int>q){
	cout<<"wyswietlanie kolejki"<<endl;
	queue<int>kolejka=q;
	while(!kolejka.empty()){
		cout<<" "<<kolejka.front();		//wyswietlenie pierwszego ele
		kolejka.pop();		//wyrzucenie pierwszego ele
	}
	cout<<endl;
}

stack<int> insert_stack(stack<int>s){
	cout<<"Podaj 10 elementow stosu: "<<endl;
	int ele;
	for(int i=0;i<10;i++){
		cin>>ele;
		s.push(ele);	//wstawienie na gore stosu
	}
	cout<<endl;
	return s;
}

queue<int> insert_que(stack<int>s1,stack<int>s2,queue<int>q){
	while(!s1.empty()){
		q.push(s1.top());		//wstawianie pierwszego stacku do kolejki
		s1.pop();
	}

	while(!s2.empty()){
		q.push(s2.top());		//wstawianie drugiego stacku do kolejki
		s2.pop();
	}
	return q;
}
int main(){

	stack<int>s1;
	stack<int>s2;
	queue<int>q;

	s1=insert_stack(s1);
	s2=insert_stack(s2);

	q=insert_que(s1,s2,q);

	print_que(q);

	return 0;
}
