#include <iostream>
using namespace std;

int main(){
  int t, x1, y1, r1, x2, y2, r2;
  cin >> t;
  for(int i = 0; i < t; i++){
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    int d = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1);

    if(r1 < r2) swap(r1, r2);
    int add = (r1 + r2) * (r1 + r2);
    int sub = (r1 - r2) * (r1 - r2);

    if(sub < d && d < add){
      cout << 2 << '\n';
    }else if((sub == d && d != 0) || add == d){
      cout << 1 << '\n';
    }else if(d > add || d < sub){
      cout << 0 << '\n';
    }else if(d == 0){
      if(r1 == r2){
        cout << -1 << '\n';
      }else{
        cout << 0 << '\n';
      }
    }
  }
}