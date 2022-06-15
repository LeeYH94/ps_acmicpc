#include <iostream>
#include <ctime>
using namespace std;

int main(){
  time_t start = clock();
  while(1){
    double leftTime = (clock() - start) / (double)CLOCKS_PER_SEC;
    cout << (clock() - start) / (double)CLOCKS_PER_SEC << endl;
    // cout << leftTime << endl;
  }
}