#include <iostream>
using namespace std;

int main(){
  int x;
  cin >> x;
  int ary[x*3+1];
  fill_n(ary, x+1, 0);
  for(int i = 1; i <= x; i++){
    if(ary[i*2] == 0){
      ary[i*2] = ary[i] + 1;
    }else{
      ary[i*2] = ary[i*2] > ary[i] + 1 ? ary[i] + 1 : ary[i*2];
    }
    if(ary[i*3] == 0){
      ary[i*3] = ary[i] + 1;
    }else{
      ary[i*3] = ary[i*3] > ary[i] + 1 ? ary[i] + 1 : ary[i*3];
    }
    if(ary[i+1] == 0){
      ary[i+1] = ary[i] + 1;
    }else{
      ary[i+1] = ary[i+1] > ary[i] + 1 ? ary[i] + 1 : ary[i+1];
    }
  }
  
  cout << ary[x] << endl;
}