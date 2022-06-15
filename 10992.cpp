#include <iostream>
using namespace std;

int main(){
  int n;
  cin >> n;
  if(n == 1){
    cout << "*";
    return 0;
  }
  string space(n-1, ' ');
  cout << space << "*\n";
  for(int i = 2; i < n; i++){
    string space2(n-i, ' ');
    string space3(2*(i-2)+1, ' ');
    cout << space2 << "*" << space3 << "*\n";
  }
  string s(2*n-1, '*');
  cout << s;
}