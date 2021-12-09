#include <iostream>

int getAbc(int N){
	if(1 <= N <= 125){
      return 4;
    }
  
  	if(126 <= N <= 211){
      return 6;
    }
  
  	return 8;
}

int main(){
  int n;
  cin >> n;
  cout << getAbc(n);
  return 0;
}