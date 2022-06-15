#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

vector<int> vec(8001, 0);

int main(){
  int cnt, temp;
  cin >> cnt;
  long long sum = 0;

  for(int i = 0; i < cnt; i++){
    cin >> temp;
    sum += temp;
    vec[temp+4000]++;
  }

  int minNum, maxNum, middleNum, mostNum;
  for(int i = 0; i < vec.size(); i++){
    if(vec[i] > 0){
      minNum = i-4000;
      break;
    }
  }

  for(int i = vec.size()-1; i >= 0; i--){
    if(vec[i] > 0){
      maxNum = i-4000;
      break;
    }
  }

  for(int i = 0; i < vec.size(); i++){
    middleNum += vec[i];
    if(middleNum >= cnt / 2 + 1){
      middleNum = i - 4000;
      break;
    }
  }

  vector<int> vec2;
  vector<int> vec3;
  copy(vec.begin(), vec.end(), back_inserter(vec2));
  sort(vec2.begin(), vec2.end(), greater<int>());
  if(vec2[0] != vec2[1]){
    mostNum = find(vec.begin(), vec.end(), vec2[0]) - vec.begin();
  }
  for(int i = 0; i < vec.size(); i++){
    if(vec[i] == vec2[0]){
      if(vec2[0] != vec2[1]){
        mostNum = i-4000;
        break;
      }else{
        vec3.push_back(i-4000);
      }
    }
  }
  if(vec2[0] == vec2[1]){
    sort(vec3.begin(), vec3.end(), greater<int>());
    mostNum = vec3[vec3.size() - 2];
  }

  long long avg = sum * 10 / cnt;
  if(avg % 10 >= 5){
    avg += 10;
  }else if(avg % 10 <= -5){
    avg -=10;
  }

  cout << avg / 10 << endl;
  cout << middleNum << endl;
  cout << mostNum << endl;
  cout << maxNum - minNum << endl;
}