#include <iostream>
using namespace std;

int main(){
  int n, m, k;
  cin >> n >> m >> k;
  int team = 0;
  while(n >= 2 && m >= 1){
    n -= 2;
    m--;
    team++;
  }

  while(n + m < k){
    team--;
    n += 2;
    m++;
  }
  cout << team << '\n';
}