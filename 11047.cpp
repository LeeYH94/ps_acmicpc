#include <iostream>
#include <vector>
using namespace std;

int main(){
  int n, k;
  cin >> n >> k;
  vector<int> vec;
  int cnt = 0;
  for(int i = 0; i < n; i++){
    int temp;
    cin >> temp;
    vec.push_back(temp);
  }
  for(int i = n-1; i >= 0; i--){
    cnt += k / vec[i];
    k = k % vec[i];
  }
  cout << cnt << endl;
}