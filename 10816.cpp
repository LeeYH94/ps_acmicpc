#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  int n, m, x;
  scanf("%d", &n);
  vector<int> vec(n);
  for(int i = 0; i < n; i++){
    scanf("%d", &x);
    vec[i] = x;
  }
  sort(vec.begin(), vec.end());

  scanf("%d", &m);
  for(int i = 0; i < m; i++){
    scanf("%d", &x);
    printf("%d ", upper_bound(vec.begin(), vec.end(), x) - lower_bound(vec.begin(), vec.end(), x));
  }
}