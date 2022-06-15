#include <iostream>
#include <stack>
using namespace std;

// int binarySearch(int K[], int n, int key){
//   int x = 0;
//   int idx;
//   while(true){
//     idx = (int)(n+x)/2;
  
//     if(K[idx] == key){
//       break;
//     }else if(K[idx] > key){
//       n = idx; 
//     }else{
//       x = idx;
//     }
//   }
//   return idx;
// }

// int main(){
//   int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//   cout << binarySearch(arr, 10, 1);
//   cout << binarySearch(arr, 10, 2);
//   cout << binarySearch(arr, 10, 3);
//   cout << binarySearch(arr, 10, 4);
//   cout << binarySearch(arr, 10, 5);
//   cout << binarySearch(arr, 10, 6);
//   cout << binarySearch(arr, 10, 7);
//   cout << binarySearch(arr, 10, 8);
//   cout << binarySearch(arr, 10, 9);
//   cout << binarySearch(arr, 10, 10);
// }
