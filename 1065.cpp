#include <iostream>
using namespace std;

int main(){
  int n;
  int cnt = 0;
  cin >> n;
  int a, b;

  for(int i = 1; i <= n; i++){
    if(i < 100){
      cnt++;
      continue;
    }else if(i == 1000){
      continue;
    }else{
      a = i / 100 - (i / 10) % 10;
      b = (i / 10) % 10 - i % 10;
      if(a == b) cnt++;
    }
  }
  cout << cnt << endl;
}