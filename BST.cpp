#include <iostream>


class TreeNode{
  int key;
  int height;

  public:

  TreeNode* leftChild;
  TreeNode* rightChild;

  TreeNode(){
    leftChild = rightChild = nullptr;
  }

  TreeNode(int newKey){
    key = newKey;
    height = 0;
    leftChild = rightChild = nullptr;
  }

  int getKey() {return key;}
  int getHeight() {return height;}
};

class BST{
  TreeNode* root;

  public:

  BST(){
    root = nullptr;
  }

  void insertBST(TreeNode T, int newKey){
    TreeNode* p = &T;
    TreeNode* q = nullptr;

    while(p != nullptr){
      if(newKey == p->getKey()) return;
      q = p;

      if(newKey < p->getKey()){
        p = p->leftChild;
      }else{
        p = p->rightChild;
      }
    }

    TreeNode* newNode = new TreeNode(newKey);
    TreeNode* temp;
    temp = &T;
    if(temp == nullptr){
      temp = newNode;
    }else if(newKey < q->getKey()){
      q->leftChild = newNode;
    }else{
      q->rightChild = newNode;
    }

    return;
  }

  void inorderBST(TreeNode* T){
    if(T != nullptr){
      inorderBST(T->leftChild);
      std::cout << T->getKey() + " ";
      inorderBST(T->rightChild);
    }
  }

};