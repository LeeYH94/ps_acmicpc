#include <iostream>
#include <vector>
using namespace std;

void DFS(int, int);
int moveCoor[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

const int MAX = 21;
int y, x, ans, cnt;
vector<vector<int>> graph(MAX, vector<int>(MAX));
vector<bool> visited(26, false);

int main(){
  cin >> y >> x;
  cin.ignore();
  string temp;
  cnt = ans = 0;
  for(int i = 0; i < y; i++){
    getline(cin, temp);
    for(int j = 0; j < x; j++){
      graph[i][j] = (char) temp[j] - 'A';
    }
  }
  DFS(0, 0);
  cout << ans << endl;
}

void DFS(int b, int a){
  visited[graph[b][a]] = true;
  cnt++;
  ans = ans > cnt ? ans : cnt;
  for(int i = 0; i < 4; i++){
    int newX = a + moveCoor[i][0];
    int newY = b + moveCoor[i][1];
    if(0 <= newX && newX < x && 0 <= newY && newY < y){
      if(!visited[graph[newY][newX]]){
        DFS(newY, newX);
      }
    }
  }
  visited[graph[b][a]] = false;
  cnt--;
}