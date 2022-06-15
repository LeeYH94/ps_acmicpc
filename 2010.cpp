#include <stdio.h>
using namespace std;

int main(){
  int t, num, cnt;
  scanf("%d", &t);
  cnt = 1;
  for(int i = 0; i < t; i++){
    scanf("%d", &num);
    cnt += num-1;
  }
  printf("%d\n", cnt);
}