#include <iostream>
using namespace std;

int main(){
  int n;
  cin >> n;
  for(int i = 1; i <= n; i++){
    string space(n-i, ' ');
    string star = "";
    for(int j = 1; j <= i; j++){
      star += "* ";
    }
    cout << space << star << '\n';
  }
}