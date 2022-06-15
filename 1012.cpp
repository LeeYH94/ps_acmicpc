#include <iostream>
#include <vector>
#include <string>
using namespace std;

void DFS(int, int);
const int MAX = 51;
vector<vector<bool>> visited(MAX, vector<bool>(MAX, false));
vector<vector<int>> graph(MAX, vector<int>(MAX, 0));
int moveCoor[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int x, y, cnt;

int main(){
  int k;
  cin >> k;
  for(int q = 0; q < k; q++){
    fill(visited.begin(), visited.end(), vector<bool>(MAX, false));
    fill(graph.begin(), graph.end(), vector<int>(MAX, 0));
    int num;
    cin >> x >> y >> num;
    vector<int> area;
    cin.ignore();
    int num1, num2;

    for(int r = 0; r < num; r++){
      cin >> num1 >> num2;
      graph[num2][num1] = 1;
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