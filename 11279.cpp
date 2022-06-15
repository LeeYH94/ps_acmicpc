#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;

int main(){
  priority_queue<int, vector<int>, less<int>> pq;
  int n, x;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d", &x);
    if(x == 0){
      if(pq.empty()){
        printf("%d\n", 0);
      }else{
        printf("%d\n", pq.top());
        pq.pop();
      }
    }else{
      pq.push(x);
    }
  }
}
