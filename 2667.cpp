#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void DFS(int, int);
const int MAX = 100;
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> graph(MAX, vector<int>(MAX, 0));
int moveCoor[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int x, y, cnt;

int main(){
  cin >> x;
  y = x;
  vector<int> area;
  cin.ignore();

  for(int i = 0; i < y; i++){
    string p;
    getline(cin, p);
    for(int j = 0; j < x; j++){
      if(p[j] == '0'){
        graph[i][j] = 0;
      }else{
        graph[i][j] = 1;
      }
    }
  }

  for(int i = 0; i < y; i++){
    for(int j = 0; j < x; j++){
      cnt = 0;
      if(graph[i][j] == 1 && !visited[i][j]){
        DFS(i, j);
        area.push_back(cnt);
      }
    }
  }
  sort(area.begin(), area.end());

  cout << area.size() << endl;
  for(int i = 0; i < area.size(); i++){
    cout << area[i] << endl;
  }
}

void DFS(int b, int a){
  visited[b][a] = true;
  cnt++;
  for(int i = 0; i < 4; i++){
    int newX = a + moveCoor[i][0];
    int newY = b + moveCoor[i][1];
    if(0 <= newX && newX < x && 0 <= newY && newY < y){
      if(graph[newY][newX] == 1 && !visited[newY][newX]){
        DFS(newY, newX);
      }
    }
  }
}