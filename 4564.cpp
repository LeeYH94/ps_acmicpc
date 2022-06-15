#include <iostream>
using namespace std;

int card(int);

int main(){
  int n;
  while(true){
    cin >> n;
    if(n == 0) break;
    cout << n << " ";
    while(n >= 10){
      n = card(n);
      cout << n << " ";
    }
    cout << endl;
  }
}

int card(int x){
  int result = 1;
  while(x > 0){
    result *= x % 10;
    x /= 10;
  }
  return result;
}