#include <iostream>
#include <vector>
using namespace std;

int main(){
  int n, k, x, num;
  cin >> n >> k;
  vector<vector<int>> vec(n+1, vector<int>(k+1, 0));

  for(int i = 1; i <= n; i++){
    vector<int> temp(k);
    for(int j = 1; j <= k; j++){
      cin >> x;
      vec[i][j] = x;
    }
  }

  for(int i = 1; i <= n; i++){
    for(int j = 1; j <= k; j++){
      vec[i][j] = vec[i][j-1] + vec[i][j];
    }
  }

  for(int j = 1; j <= k; j++){
    for(int i = 1; i <= n; i++){
      vec[i][j] = vec[i-1][j] + vec[i][j];
    }
  }
  cin >> num;
  int a, b, aa, bb;
  for(int i = 0; i < num; i++){
    cin >> a >> b >> aa >> bb;
    cout << vec[aa][bb] - vec[a-1][bb] - vec[aa][b-1] + vec[a-1][b-1] << '\n';
  }
}