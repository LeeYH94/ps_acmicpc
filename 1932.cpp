#include <iostream>
#include <vector>
using namespace std;

int main(){
  int n, temp;
  cin >> n;
  vector<vector<int>> vec(n, vector<int>(n));
  for(int i = 0; i < n; i++){
    for(int j = 0; j <= i; j++){
      cin >> temp;
      vec[i][j] = temp;
    }
  }
  for(int i = 1; i < n; i++){
    for(int j = 0; j <= i; j++){
      if(j == 0){
        vec[i][0] += vec[i-1][0];
      }else if(j == i){
        vec[i][j] += vec[i-1][j-1];
      }else{
        vec[i][j] += vec[i-1][j-1] > vec[i-1][j] ? vec[i-1][j-1] : vec[i-1][j];
      } 
    }
  }
  int max_num = 0;
  for(int i = 0 ; i < n; i++){
    max_num = max_num > vec[n-1][i] ? max_num : vec[n-1][i];
  }
  cout << max_num << endl;
}