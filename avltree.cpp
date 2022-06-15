#include <stdio.h>
#include <stdlib.h>
#include <stack>

using namespace std;

extern inline int max(int a, int b) { return a < b ? b : a;}

typedef struct AVLNode{
  int key, address, height, bf;
  struct AVLNode *left, *right;
} AVLNode;

AVLNode *getAVLNode(){
  AVLNode *node = (AVLNode *)malloc(sizeof(AVLNode));
  node->height = 1;
  node->bf = 0;
  node->left = node->right = NULL;
  return node;
}

typedef AVLNode *AVLTree;

int height(AVLTree T){
  if(T == NULL) return 0;
  return T->height;
}

void rotateLL(AVLTree *T, AVLNode *x, AVLNode *f){
  f->left->right = f;
  f->left = x->right; 
}

void rotateRR(AVLTree *T, AVLNode *x, AVLNode *f){
  f->right->left = f;
  f->right = x->left;
}

void rotateLR(AVLTree *T, AVLNode *x, AVLNode *f){
  rotateRR(T, x->right, x);
  rotateLL(T, x, f);
}

void rotateRL(AVLTree *T, AVLNode *x, AVLNode *f){
  rotateRR(T, x->left, x);
  rotateLL(T, x, f);
}

void insertAVL(AVLTree *T, int newKey){
  AVLNode *p = *T;
  AVLNode *q = nullptr;
  AVLNode *x = nullptr;
  AVLNode *f = nullptr;
  stack<AVLTree> s;

  while(p != nullptr){
    if(newKey == p->key) return;
    
    q = p;
    s.push(q);

    if(newKey < p->key){
      p = p->left;
    }else{
      p = p->right;
    }
  }

  AVLNode *y = getAVLNode();
  y->key = newKey;

  if(T == nullptr){
    *T = y;
  }else if(newKey < q->key){
    q->left = y;
  }else{
    q->right = y;
  }

  while(!s.empty()){
    q = s.top();
    s.pop();
    q->height <- 1 + max(q->left->height, q->right->height);
    q->bf <- q->left->height - q->right->height;

    if(1 < q->bf || q->bf < -1){
      if(x == NULL){
        x = q;
        f = s.top();
      }
    }
  }

  // if(1 < x->bf){
  //   if(x->left->bf < 0){
  //     rotateLR(T, x, f);
  //   }else{
  //     rotateLL(T, x, f);
  //   }
  // }else{
  //   if(x->right->bf < 0){
  //     rotateRL(T, x, f);
  //   }else{
  //     rotateRR(T, x, f);
  //   }
  // }
}

void deleteAVL(AVLTree *T, int deleteKey){

}

void inorderAVL(AVLTree T){
  if(T == NULL) return;
  inorderAVL(T->left);
  printf(T->key + " ");
  inorderAVL(T->right);
}

int main(){
  int testCases[] = {
        40, 11, 77, 33, 20, 
        90, 99, 70, 88, 80, 
        66, 10, 22, 30, 44, 
        55, 50, 60, 25, 49
        };

  AVLTree T = NULL;
  
  for(int i = 0; i < 20; i++){
    insertAVL(&T, testCases[i]);
    inorderAVL(T);
    printf("\n");
  }

  // for(int i = 0; i < 20; i++){
  //   deleteAVL(&T, testCases[i]);
  //   inorderAVL(T);
  //   printf("\n");
  // }

  // for(int i = 0; i < 20; i++){
  //   insertAVL(&T, testCases[i]);
  //   inorderAVL(T);
  //   printf("\n");
  // }

  // for(int i = 19; 0 <= i; i--){
  //   deleteAVL(&T, testCases[i]);
  //   inorderAVL(T);
  //   printf("\n");
  // }
}