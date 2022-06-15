#include <iostream>
using namespace std;

template <typename T>
class Tree;

template <typename T>
class Node{
  friend class Tree<T>;
  T data;
  Node<T>* left;
  Node<T>* right;
  public:
    Node(T data, Node<T>* left = nullptr, Node<T>* right = nullptr){
      this->data = data;
      this->left = left;
      this->right = right;
    }
};

template <typename T>
class Tree{
  private:
  Node<T>* root;
  public:
    Tree() : root(NULL){}

    void insert(T data, T leftData, T rightData){
      if(root == nullptr){
        root = new Node<T>(data); 
        if(leftData != '.') root->left = new Node<T>(leftData);
        if(rightData != '.') root->right = new Node<T>(rightData);
      }else{
        search(root, data, leftData, rightData);
      }
    }

    void search(Node<T>* node, T data, T leftData, T rightData){
      if(node == nullptr){
        return;
      }else if(node->data == data){
        if(leftData != '.') node->left = new Node<T>(leftData);
        if(rightData != '.') node->right = new Node<T>(rightData);
      }else{
        search(node->left, data, leftData, rightData);
        search(node->right, data, leftData, rightData);
      }
    }
    
    Node<T>* rootNode(){
      return root;
    }

    void prefix(Node<T>* node){
      if(node == nullptr) return;
      cout << node->data;
      prefix(node->left);
      prefix(node->right);
    }

    void infix(Node<T>* node){
      if(node == nullptr) return;
      infix(node->left);
      cout << node->data;
      infix(node->right);
    }

    void postfix(Node<T>* node){
      if(node == nullptr) return;
      postfix(node->left);
      postfix(node->right);
      cout << node->data;
    }
};

int main(){
  int n;
  cin >> n;
  char x, y, z;
  Tree<char> tree{};

  for(int i = 0; i < n; i++){
    cin >> x >> y >> z;
    tree.insert(x, y, z);
  }
  tree.prefix(tree.rootNode());
  cout << '\n';
  tree.infix(tree.rootNode());
  cout << '\n';
  tree.postfix(tree.rootNode());
  cout << '\n';
}