#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  vector<int> vec;
  bool flag;
  for(int i = 2; i < 10001; i++){
    flag = true;
    for(int j = 2; j <= sqrt(i); j++){
      if(i % j == 0){
        flag = false;
      }
    }
    if(flag) vec.push_back(i);
  }

  int t, n, a, b;
  cin >> t;
  for(int i = 0; i < t; i++){
    cin >> n;
    a = b = n / 2;
    while(true){
      if(find(vec.begin(), vec.end(), a) != vec.end()
           && find(vec.begin(), vec.end(), b) != vec.end()) break;
      a--;
      b++;
    }
    cout << a << " " << b << '\n';
  }
}