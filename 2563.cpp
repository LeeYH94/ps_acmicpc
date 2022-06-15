#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  const int MAX = 101;
  vector<vector<bool>> vec(MAX, vector<bool>(MAX, false));
  int t, x1, y1;
  cin >> t;

  for(int i = 0; i < t; i++){
    cin >> x1 >> y1;
    for(int i = y1; i < y1+10; i++){
      for(int j = x1; j < x1+10; j++){
        vec[j][i] = true;
      }
    }
  }

  int cnt = 0;
  for(int i = 0; i < MAX; i++){
    for(int j = 0; j < MAX; j++){
      if(vec[j][i]) cnt++;
    }
  }
  cout << cnt <<'\n';
}