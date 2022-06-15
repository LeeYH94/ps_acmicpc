#include <iostream>
#include <cmath>

using namespace std;

int main(){
  const long double pi = 3.141592653589793238;
  long long num;
  cin >> num;
  long double result = num * num * pi;
  cout << fixed;
  cout.precision(6);
  cout << round(result * 1000000) / 1000000 << endl;
  cout << round(2 * num * num * 1000000)/ 1000000 << endl;
}