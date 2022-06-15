#include <iostream>
#include <vector>
using namespace std;

int main(){
  vector<string> vec;
  int n;
  string temp, ans = "";
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> temp;
    vec.push_back(temp);
  }

  for(int j = 0; j < temp.size(); j++){
    bool flag = true;
    for(int i = 0; i < n; i++){
      if(vec[i][j] != temp[j]) flag = false;
    }
    if(!flag){
      ans += "?";
    }else{
      ans += temp[j];
    }
  }
  cout << ans << '\n';
}