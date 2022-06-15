#include <iostream>
using namespace std;

int gcd(int x, int y){
  int temp;
  if(x < y){
    temp = x;
    x = y;
    y = temp;
  }
  int rest;
  while(y != 0){
    rest = x % y;
    x = y;
    y = rest;
  }
  return x;
}

int main(){
  int t, temp;
  int m, n, x, y;
  bool flag;
  cin >> t;
  for(int i = 0; i < t; i++){
    cin >> m >> n >> x >> y;
    temp = x;
    flag = true;
    while(true){
      if(temp > m * n / gcd(m, n)){
        flag = false;
        break;
      }
      if(temp % n == y % n) break;
      temp += m;
    }
    if(flag){
      cout << temp << '\n';
    }else{
      cout << -1 << '\n';
    }
  }
}