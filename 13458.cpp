#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  int n, b, num, temp;
  double c;
  cin >> n;
  int ary[n];
  long long sum = 0;

  for(int i = 0; i < n; i++){
    cin >> num;
    ary[i] = num;
  }

  cin >> b >> c;

  for(int i = 0; i < n; i++){
    temp = ary[i] - b;
    sum++;
    if(temp > 0) sum += ceil(temp / c);
  }
  cout << sum << endl;
}