#include <iostream>
using namespace std;

int main(){
  int n, cnt, sum;
  sum = 0;
  cin >> n;
  n = 1000 - n;
  int ary[6] = {500, 100, 50, 10, 5, 1};
  for(int i = 0 ; i < 6; i++){
    sum += n / ary[i];
    n %= ary[i];
  }
  cout << sum << endl;
}