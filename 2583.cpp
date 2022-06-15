#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void DFS(int, int);
const int MAX = 101;
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> graph(MAX, vector<int>(MAX, 1));
int moveCoor[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int x, y, cnt;

int main(){
  int num;
  cin >> y >> x >> num;
  vector<int> area;
  cin.ignore();

  int x1, y1, x2, y2;

  for(int r = 0; r < num; r++){
    cin >> x1 >> y1 >> x2 >> y2;
    for(int i = y1; i < y2; i++){
      for(int j = x1; j < x2; j++){
        graph[i][j] = 0;
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
  cout << area.size() << endl;
  sort(area.begin(), area.end());
  for(int i = 0; i < area.size(); i++){
    cout << area[i] << " ";
  }
  cout << '\n';
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