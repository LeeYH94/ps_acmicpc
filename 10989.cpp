#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  vector<int> vec(10001);
  fill_n(vec.begin(), 10001, 0);
  int n, num;
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> num;
    vec[num] += 1;
  }  
  for(int i = 0; i < 10001; i++){
    if(vec[i] != 0){
      for(int j = 0; j < vec[i]; j++){
        cout << i << '\n';
      }
    }
  }
}