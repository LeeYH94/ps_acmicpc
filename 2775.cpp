#include <iostream>
#include <vector>
using namespace std;

int main(){
  int t, n, k;
  cin >> t;
  vector<vector<int>> vec(15, vector<int>(15, 0));

  for(int i = 0; i < 15; i++){
    for(int j = 1; j < 15; j++){
      if(i == 0){
        vec[i][j] = j;
      }else{
        for(int k = 0; k <= j; k++){
          vec[i][j] += vec[i-1][k];
        }
      }
    }
  }

  for(int i = 0; i < t; i++){
    cin >> n >> k;
    cout << vec[n][k] << '\n';
  }
}