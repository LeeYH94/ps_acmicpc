#include <stdio.h>
#include <cmath>
#include <vector>
using namespace std;

vector<bool> isPrime(1000001, false);

int main(){
  for (int i = 2; i <= 1000001; i++) 
		isPrime[i] = true;

	for (int i = 2; i*i <= 1000001; i++) {
		if(isPrime[i]) // 소수이면
			for (int j = i*i; j <= 1000001; j += i) { 
				isPrime[j] = false;
		}
	}

  int n, a, b;
  while(true){
    scanf("%d", &n);
    if(n == 0) break;
    int idx = 0;
    a = 3;
    bool flag = true;
    while(true){
      b = n-a;
      if(isPrime[a] && isPrime[b]) break;
      a += 2;
      if(a > b){
        flag = false;
        break;
      }
    }
    if(!flag){
      printf("Goldbach's conjecture is wrong.\n");
    }else{
      printf("%d = %d + %d\n", n, a, b);
    }
  }
}