#include <stdio.h>
#include <stdlib.h>
#include <stack>

using namespace std;

typedef struct BTNode{
  int n, *K, *A;
  struct BTNode **P;
} BTNode;

BTNode *getBTNode(int m){
  BTNode *node = (BTNode *)malloc(sizeof(BTNode));
  node->n = 0;
  node->K = (int *)malloc(sizeof(int) * (m-1));
  node->A = NULL;
  node->P = (BTNode **)calloc(m, sizeof(BTNode *));
  return node;
}

typedef BTNode *BTree;

int binarySearch(int K[], int n, int key){
  int x = 0;
  int mid;
  while(x <= n){
    mid = (int)(n+x)/2;
    if(K[mid] == key) break;
    if(K[mid] > key) n = mid-1;
    else x = mid+1;
  }
  return mid;
}

int* sortArr(int K[], int n){
  for(int i = 0; i < n-1; i++){
    if(K[i] > K[i+1]){
      int temp = K[i];
      K[i] = K[i+1];
      K[i+1] = temp;
    }
  }
  return K;
}

void insertBT(BTree *T, int m, int newKey){
  BTree x = *T;
  BTree y = NULL;
  stack<BTree> s;
  stack<int> iStack;
  printf("1");

  while(x != NULL){
    printf("2");
    int i = binarySearch(x->K, m-2, newKey);

    if(i < x->n && newKey == x->K[i]) return; // newKey already exists in T

    s.push(x);
    iStack.push(i);

    x = (BTree)x->P[i];
  }
  printf("1");
  // insert key and node while popping parent node from stack while 
  while(!s.empty()){
    x = s.top();
    x->K = sortArr(x->K, x->n);
    int idx = iStack.top();

    s.pop();
    iStack.pop();

    if(x->n < m-1){
      x->K[x->n] = newKey;
      x->n = x->n + 1;
      
      if(y != NULL) x->P[idx] = y;
      return;
    }

    //case of overflow
    BTree tempNode = getBTNode(m+1);
    tempNode->A = x->A;
    tempNode->K = x->K;
    tempNode->n = x->n;
    tempNode->P = x->p;

    tempNode->K[x->n] = newKey;
    tempNode->P[x->n] = y;
    tempNode->n++;

    y = getBTNode(m);
    for(int i = 0; i < tempNode->n; i++){
      if(i < (tempNode->n)/2){
        x->K[i] = tempNode->K[i];
        x->P[i] = tempNode->P[i];
      }else{
        y->K[i-(tempNode->n)/2] = tempNode->K[i];
        y->P[i-(tempNode->n)/2] = tempNode->P[i];
      }
    }
    newKey = tempNode->K[m/2];
    delete tempNode;
  }
  printf("1");
  *T = getBTNode(m);
  (*T)->K[0] = newKey;
  (*T)->P[0] = x;
  (*T)->P[1] = y;
  (*T)->n = 1;
}

void deleteBT(BTree *T, int m, int oldKey){

}

void inorderBT(BTree T){
  if(T == NULL) return;

  for(int i = 0; i < T->n; i++){
    inorderBT(T->P[i]);
    printf("%d ", (T->K[i]));
  }

  inorderBT(T->P[T->n]);
}

int main(){
  FILE *f;
  for(int m = 3; m <= 4; m++){
    BTree T = NULL;

    f = fopen("./insertSequence.txt", "r");
    for(int n; !feof(f);){
      fscanf(f, "%d", &n);
      insertBT(&T, m, n);
      printf("\n");
      inorderBT(T);
      printf("\n");
    }
    fclose(f);

    // f = fopen("./deleteSequence.txt", "r");
    // for(int n; !feof(f);){
    //   fscanf(f, "%d", &n);
    //   deleteBT(&T, m, n);
    //   inorderBT(T);
    //   printf("\n");
    // }
    // fclose(f);
  }
}




