#include <iostream>
using namespace std;

bool self[10001];
void initial(int);

int main(){
  fill_n(self, 10000, true);
  for(int i = 1; i <= 10000; i++){
    if(self[i]) initial(i);
  }
  
  for(int i = 1; i <= 10000; i++){
    if(self[i]) cout << i << endl;
  }
}

void initial(int x){
  int sum = x;
  while(x > 0){
    sum += x % 10;
    x /= 10;
  }
  if(self[sum]){
    self[sum] = false;
    initial(sum);
  }
}